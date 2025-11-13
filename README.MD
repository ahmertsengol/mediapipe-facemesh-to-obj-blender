# MediaPipe Face Mesh to OBJ Converter

A Python tool that converts 2D face images to 3D OBJ models using MediaPipe's 468 facial landmarks. Perfect for creating 3D face models for Blender, Unity, or other 3D software.

**Author:** [Ahmet Mert Şengöl](https://github.com/ahmertsengol)

## Features

- 🎯 Converts 2D photos to 3D face models (OBJ format)
- 🚀 Fast processing on CPU (MediaPipe optimized for mobile/CPU)
- 🎨 Generates texture maps automatically
- 📐 Uses 468 facial landmarks for accurate detection
- 🖼️ Works with both photos and illustrations

## Requirements

- Python 3.10+
- MediaPipe
- NumPy
- OpenCV
- scikit-image

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python simplified_mp_to_obj.py -i <input_image.jpg> -o <output_name>
```

### Examples

```bash
# With input and output specified
python simplified_mp_to_obj.py -i examples/gakki.jpg -o results/my_model

# Interactive mode (prompts for input)
python simplified_mp_to_obj.py
```

### Output Files

The script generates three files:
- `*.obj` - 3D mesh file
- `*.mtl` - Material file
- `*_texture.jpg` - Face texture (512x512)

## Scripts

- `simplified_mp_to_obj.py` - Simplified version (recommended)
- `mediapipe_to_obj.py` - Full version with error handling
- `mediapipe_to_obj_clean.py` - Clean output wrapper (filters warnings)

## Documentation

- [KULLANIM.md](KULLANIM.md) - Turkish usage guide
- [KURULUM.md](KURULUM.md) - Turkish installation guide
- [TEST_KILAVUZU.md](TEST_KILAVUZU.md) - Turkish testing guide

## Known Limitations

- Nose detection may not always match the reference image perfectly
- Works best with single face images
- Open eyes are detected more accurately than closed eyes

## License

This project is open source and available for educational purposes.
