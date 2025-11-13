#!/usr/bin/env python3
"""
MediaPipe Face Mesh to OBJ Converter - Web Interface
Flask web application for converting 2D face images to 3D OBJ models

Author: Ahmet Mert Şengöl
GitHub: https://github.com/ahmertsengol
"""

from flask import Flask, render_template, request, send_file, jsonify
import os
import json
import math
import numpy as np
import mediapipe as mp
import skimage
from skimage.transform import PiecewiseAffineTransform, warp
import tempfile
from werkzeug.utils import secure_filename
import warnings

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'results'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)

# Import functions from simplified_mp_to_obj
from simplified_mp_to_obj import (
    load_obj,
    write_obj,
    normalize_keypoints,
    align_keypoints_to_grid
)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def process_image(img_path, output_name="output"):
    """Process image and generate OBJ files"""
    uv_path = "data/uv_map.json"
    uv_map_dict = json.load(open(uv_path))
    uv_map = np.array([(uv_map_dict["u"][str(i)], uv_map_dict["v"][str(i)]) for i in range(468)])
    
    img_ori = skimage.io.imread(img_path)
    
    # Handle RGBA images
    if len(img_ori.shape) == 3 and img_ori.shape[2] == 4:
        img_ori = skimage.color.rgba2rgb(img_ori)
        img_ori = (img_ori * 255).astype(np.uint8)
    
    img = img_ori
    H, W, _ = img.shape
    
    # Run facial landmark detection
    with mp.solutions.face_mesh.FaceMesh(
            static_image_mode=True,
            refine_landmarks=True,
            max_num_faces=1,
            min_detection_confidence=0.5) as face_mesh:
        try:
            results = face_mesh.process(img)
        except ValueError:
            # PNG conversion if needed
            tmp_path = os.path.join(app.config['UPLOAD_FOLDER'], 'converted.jpg')
            png_img = skimage.io.imread(img_path)
            rgb_img = skimage.color.rgba2rgb(png_img)
            skimage.io.imsave(tmp_path, rgb_img, quality=100)
            img = skimage.io.imread(tmp_path)
            results = face_mesh.process(img)
    
    if not results.multi_face_landmarks:
        raise Exception("No face detected in the image.")
    
    face_landmarks = results.multi_face_landmarks[0]
    keypoints = np.array([(W*point.x, H*point.y) for point in face_landmarks.landmark[0:468]])
    
    # Generate texture
    H_new, W_new = 512, 512
    keypoints_uv = np.array([(W_new*x, H_new*y) for x, y in uv_map])
    
    tform = PiecewiseAffineTransform()
    tform.estimate(keypoints_uv, keypoints)
    texture = warp(img_ori, tform, output_shape=(H_new, W_new))
    texture = (255*texture).astype(np.uint8)
    
    # Get 3D keypoints
    width_ratio = W / H
    keypoints3d = np.array([(width_ratio * point.x, point.y, width_ratio * point.z) 
                           for point in face_landmarks.landmark[0:468]])
    
    # Load canonical face model
    obj_filename = "./data/canonical_face_model.obj"
    canonical_verts, uvcoords, faces, uv_faces = load_obj(obj_filename)
    
    # Normalize and align
    vertices = normalize_keypoints(keypoints3d)
    vertices = align_keypoints_to_grid(vertices)
    
    # Save files
    obj_name = os.path.join(app.config['RESULTS_FOLDER'], f"{output_name}.obj")
    texture_name = os.path.join(app.config['RESULTS_FOLDER'], f"{output_name}_texture.jpg")
    
    write_obj(obj_name, vertices, faces, texture_name, 
             texture=texture, uvcoords=uvcoords, uvfaces=uv_faces)
    
    return obj_name, texture_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Generate output name
        output_name = os.path.splitext(filename)[0]
        
        try:
            obj_path, texture_path = process_image(filepath, output_name)
            
            return jsonify({
                'success': True,
                'message': 'Conversion completed successfully!',
                'obj_file': f'/download/obj/{output_name}',
                'texture_file': f'/download/texture/{output_name}',
                'mtl_file': f'/download/mtl/{output_name}'
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/download/obj/<filename>')
def download_obj(filename):
    obj_path = os.path.join(app.config['RESULTS_FOLDER'], f"{filename}.obj")
    if os.path.exists(obj_path):
        # Check if it's a preview request
        if request.args.get('preview') == 'true':
            return send_file(obj_path, mimetype='text/plain')
        return send_file(obj_path, as_attachment=True, download_name=f"{filename}.obj")
    return jsonify({'error': 'File not found'}), 404

@app.route('/download/texture/<filename>')
def download_texture(filename):
    texture_path = os.path.join(app.config['RESULTS_FOLDER'], f"{filename}_texture.jpg")
    if os.path.exists(texture_path):
        # Check if it's a download request or preview
        if request.args.get('preview') == 'true':
            return send_file(texture_path, mimetype='image/jpeg')
        return send_file(texture_path, as_attachment=True, download_name=f"{filename}_texture.jpg")
    return jsonify({'error': 'File not found'}), 404

@app.route('/download/mtl/<filename>')
def download_mtl(filename):
    mtl_path = os.path.join(app.config['RESULTS_FOLDER'], f"{filename}.mtl")
    if os.path.exists(mtl_path):
        # Check if it's a preview request
        if request.args.get('preview') == 'true':
            return send_file(mtl_path, mimetype='text/plain')
        return send_file(mtl_path, as_attachment=True, download_name=f"{filename}.mtl")
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    import socket
    
    # Port kontrolü - önce 5000'i dene, yoksa 8080 kullan
    port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 5000))
    sock.close()
    
    if result == 0:
        # Port 5000 kullanımda, 8080 kullan
        port = 8080
        print("⚠️  Port 5000 kullanımda (muhtemelen macOS AirPlay), port 8080 kullanılıyor...")
        print("💡 macOS'ta AirPlay'i kapatmak için: Sistem Ayarları > Genel > AirDrop ve Handoff > AirPlay Alıcı")
    else:
        port = int(os.environ.get('PORT', 5000))
    
    print(f"🚀 Server starting on http://localhost:{port}")
    print(f"📝 Tarayıcınızda http://localhost:{port} adresini açın")
    app.run(debug=True, host='0.0.0.0', port=port)

