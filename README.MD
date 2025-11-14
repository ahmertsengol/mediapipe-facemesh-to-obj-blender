# MediaPipe Face Mesh to OBJ Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A Python tool that converts 2D face images to 3D OBJ models using MediaPipe's 468 facial landmarks. Perfect for creating 3D face models for Blender, Unity, or other 3D software.

**Author:** [Ahmet Mert Şengöl](https://github.com/ahmertsengol)

## 🎬 Demo

### 3D Model Animation

<div align="center">
  <img src="naruto/naruto.gif" alt="Naruto 3D Model Animation" width="400"/>
</div>

### Input & Output Comparison

<table>
  <tr>
    <td align="center">
      <strong>Generated Texture Map</strong><br/>
      <img src="naruto/naruto_texture.jpg" alt="Naruto Original" width="300"/>
    </td>
    <td align="center">
      <strong>Original 2D Image</strong><br/>
      <img src="naruto/naruto.png" alt="Naruto Texture" width="300"/>
    </td>
  </tr>
</table>

## Features

- 🎯 Converts 2D photos to 3D face models (OBJ format)
- 🚀 Fast processing on CPU
- 🎨 Generates texture maps automatically
- 🖼️ Works with both photos and illustrations

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Web Interface

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

### Command Line

```bash
python simplified_mp_to_obj.py -i <input_image.jpg> -o <output_name>
```

**Output:** Generates `*.obj`, `*.mtl`, and `*_texture.jpg` files.

## Scripts

- `app.py` - Web interface (recommended)
- `simplified_mp_to_obj.py` - Command-line version

## License

MIT License - see [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Ahmet Mert Şengöl
