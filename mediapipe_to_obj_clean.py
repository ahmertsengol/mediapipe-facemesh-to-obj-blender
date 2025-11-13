#!/usr/bin/env python3
"""
Temiz çıktılı MediaPipe Face Mesh to OBJ dönüştürücü
Uyarıları bastırarak sadece önemli mesajları gösterir
"""

import subprocess
import sys
import os

def main():
    """Ana script'i uyarıları filtreleyerek çalıştırır"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, 'mediapipe_to_obj.py')
    
    # Komut satırı argümanlarını al
    args = sys.argv[1:]
    
    # Script'i çalıştır ve çıktıyı filtrele
    try:
        result = subprocess.run(
            [sys.executable, script_path] + args,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Sadece önemli çıktıları göster
        output_lines = result.stdout.split('\n')
        error_lines = result.stderr.split('\n')
        
        # "Process Complete!" mesajını göster
        for line in output_lines + error_lines:
            if 'Process Complete' in line or 'Complete' in line:
                print(line)
            elif line.strip() and not any(x in line for x in [
                'WARNING', 'INFO', 'W0000', 'I0000', 
                'gl_context', 'TensorFlow', 'inference_feedback',
                'landmark_projection', 'NORM_RECT'
            ]):
                print(line)
        
        print("✅ İşlem başarıyla tamamlandı!")
        
    except subprocess.CalledProcessError as e:
        # Hata durumunda tüm çıktıyı göster
        print("❌ Hata oluştu:", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        print(e.stdout, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

