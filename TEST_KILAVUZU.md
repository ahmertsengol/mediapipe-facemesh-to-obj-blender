# 🧪 Test Kılavuzu - Adım Adım

Bu kılavuz, MediaPipe Face Mesh to OBJ projesini nasıl test edeceğinizi adım adım açıklar.

## 📋 Ön Hazırlık

### Adım 1: Proje Dizinine Git
```bash
cd mediapipe-facemesh-to-obj
```

### Adım 2: Mevcut Dosyaları Kontrol Et
```bash
ls -la
```

Şu dosyaları görmelisiniz:
- `mediapipe_to_obj.py` - Ana program
- `requirements.txt` - Bağımlılıklar
- `examples/` - Örnek görüntüler
- `data/` - Model dosyaları

### Adım 3: Örnek Görüntüleri Kontrol Et
```bash
ls examples/
```

Şu görüntüleri görmelisiniz:
- `gakki.jpg` - Fotoğraf örneği
- `illustrated.png` - İllüstrasyon örneği
- `landmarks.jpg` - Landmark örneği

## 🚀 Test Senaryoları

### Test 1: Temel Kullanım (En Basit)

**Adım 1:** Programın çalışıp çalışmadığını kontrol edin:
```bash
python3 mediapipe_to_obj.py --help
```

**Beklenen Çıktı:**
```
usage: Mediapipe to OBJ [-h] [-i INPUT] [-o OUTPUT]

Covert 2D pictures to 3D meshes

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The path for the face image
  -o OUTPUT, --output OUTPUT
                        The output directory. Defaults to 'results/<name of image>.obj'
```

**Adım 2:** Örnek görüntü ile test edin:
```bash
python3 mediapipe_to_obj.py -i examples/gakki.jpg
```

**Beklenen Sonuç:**
- Program çalışır ve "Process Complete!" mesajı görünür
- `results/` klasörü oluşturulur
- `results/gakki.obj`, `results/gakki.mtl`, `results/gakki_texture.jpg` dosyaları oluşturulur

**Adım 3:** Oluşturulan dosyaları kontrol edin:
```bash
ls -lh results/
```

### Test 2: Özel Çıktı Yolu Belirtme

**Adım 1:** Özel bir çıktı yolu ile test edin:
```bash
python3 mediapipe_to_obj.py -i examples/gakki.jpg -o results/test_model
```

**Beklenen Sonuç:**
- `results/test_model.obj`
- `results/test_model.mtl`
- `results/test_model_texture.jpg`

**Adım 2:** Dosyaların içeriğini kontrol edin:
```bash
head -20 results/test_model.obj
```

OBJ dosyasında şunları görmelisiniz:
- `v` ile başlayan satırlar (vertex/koordinatlar)
- `vt` ile başlayan satırlar (texture koordinatları)
- `f` ile başlayan satırlar (face/yüzler)

### Test 3: İnteraktif Mod

**Adım 1:** Programı parametre olmadan çalıştırın:
```bash
python3 mediapipe_to_obj.py
```

**Adım 2:** Program görüntü yolunu soracak:
```
Filename: 
```

**Adım 3:** Görüntü yolunu girin:
```
examples/gakki.jpg
```

**Beklenen Sonuç:** Test 1 ile aynı sonuç

### Test 4: Farklı Görüntü Formatları

**PNG Formatı Testi:**
```bash
python3 mediapipe_to_obj.py -i examples/illustrated.png -o results/illustrated_test
```

**Beklenen Sonuç:**
- PNG otomatik olarak işlenir (bazı durumlarda JPG'ye dönüştürülür)
- Sonuç dosyaları oluşturulur

### Test 5: Dosya Boyutlarını Kontrol Etme

**Adım 1:** OBJ dosyasının boyutunu kontrol edin:
```bash
ls -lh results/*.obj
```

**Beklenen:** Her OBJ dosyası yaklaşık 50-100 KB arasında olmalı

**Adım 2:** Texture dosyasını görüntüleyin:
```bash
open results/gakki_texture.jpg
```

macOS'ta görüntü otomatik açılır. Texture dosyası 512x512 piksel olmalı.

### Test 6: Hata Durumları

**Test 6.1: Olmayan Dosya**
```bash
python3 mediapipe_to_obj.py -i olmayan_dosya.jpg
```

**Beklenen:** Hata mesajı (FileNotFoundError veya benzeri)

**Test 6.2: Yüz Olmayan Görüntü**
```bash
# Eğer yüz içermeyen bir görüntü varsa
python3 mediapipe_to_obj.py -i yuz_olmayan.jpg
```

**Beklenen:** AssertionError veya "No face detected" benzeri hata

## 🔍 Detaylı Kontrol

### OBJ Dosyasını İnceleme

**Adım 1:** OBJ dosyasının ilk satırlarını görüntüleyin:
```bash
head -50 results/gakki.obj
```

**Beklenen Format:**
```
mtllib gakki.mtl

v 0.123456 0.234567 0.345678
v 0.234567 0.345678 0.456789
...
vt 0.123456 0.234567
vt 0.234567 0.345678
...
usemtl FaceTexture
f 1/1 2/2 3/3
f 4/4 5/5 6/6
...
```

**Adım 2:** Vertex sayısını kontrol edin:
```bash
grep "^v " results/gakki.obj | wc -l
```

**Beklenen:** Yaklaşık 468 vertex (MediaPipe 468 landmark kullanır)

**Adım 3:** Face sayısını kontrol edin:
```bash
grep "^f " results/gakki.obj | wc -l
```

**Beklenen:** Binlerce face (yüz mesh'i)

### MTL Dosyasını İnceleme

```bash
cat results/gakki.mtl
```

**Beklenen İçerik:**
```
newmtl FaceTexture
map_Kd gakki_texture.jpg
```

### Texture Dosyasını Kontrol Etme

**Adım 1:** Texture dosyasının boyutunu kontrol edin:
```bash
file results/gakki_texture.jpg
```

**Beklenen:** `JPEG image data, ... 512 x 512, ...`

**Adım 2:** Python ile texture boyutunu kontrol edin:
```python
from PIL import Image
img = Image.open('results/gakki_texture.jpg')
print(f"Boyut: {img.size}")  # Beklenen: (512, 512)
```

## 🎨 3D Yazılımda Görüntüleme

### Blender'da Açma

**Adım 1:** Blender'ı açın

**Adım 2:** File > Import > Wavefront (.obj) seçin

**Adım 3:** `results/gakki.obj` dosyasını seçin

**Beklenen:** 3D yüz modeli görüntülenir ve texture otomatik yüklenir

### Online Görüntüleyici Kullanma

**Adım 1:** [https://3dviewer.net](https://3dviewer.net) gibi bir online görüntüleyici açın

**Adım 2:** OBJ dosyasını yükleyin

**Adım 3:** Texture dosyasını da yükleyin (otomatik yüklenmeyebilir)

## 📊 Performans Testi

### İşlem Süresini Ölçme

```bash
time python3 mediapipe_to_obj.py -i examples/gakki.jpg -o results/performance_test
```

**Beklenen:** 
- CPU'da: 1-5 saniye
- GPU varsa: Daha hızlı

### Farklı Görüntü Boyutları ile Test

**Küçük görüntü:**
```bash
python3 mediapipe_to_obj.py -i kucuk_resim.jpg -o results/kucuk_test
```

**Büyük görüntü:**
```bash
python3 mediapipe_to_obj.py -i buyuk_resim.jpg -o results/buyuk_test
```

## ✅ Başarı Kriterleri

Test başarılı sayılır eğer:

1. ✅ Program hatasız çalışır
2. ✅ OBJ, MTL ve texture dosyaları oluşturulur
3. ✅ OBJ dosyası geçerli formatta
4. ✅ Texture dosyası 512x512 piksel
5. ✅ 3D yazılımda model görüntülenebilir
6. ✅ Yüz özellikleri (gözler, burun, ağız) tanınabilir

## 🐛 Sorun Giderme

### Sorun: "No module named 'mediapipe'"
**Çözüm:**
```bash
pip install mediapipe
```

### Sorun: "No face detected"
**Çözüm:**
- Görüntüde net bir yüz olduğundan emin olun
- Farklı bir görüntü deneyin
- Görüntü kalitesini artırın

### Sorun: "Unable to use a PNG"
**Çözüm:**
- PNG dosyasını JPG'ye dönüştürün:
```bash
convert input.png output.jpg
# veya Python ile:
from PIL import Image
img = Image.open('input.png')
img.convert('RGB').save('output.jpg')
```

### Sorun: Texture görünmüyor
**Çözüm:**
- OBJ ve texture dosyalarının aynı klasörde olduğundan emin olun
- MTL dosyasındaki texture dosya adını kontrol edin

## 📝 Test Raporu Şablonu

Test yaptıktan sonra şu bilgileri not edin:

```
Test Tarihi: ___________
Test Eden: ___________

Test 1 (Temel Kullanım): [ ] Başarılı [ ] Başarısız
Test 2 (Özel Çıktı): [ ] Başarılı [ ] Başarısız
Test 3 (İnteraktif Mod): [ ] Başarılı [ ] Başarısız
Test 4 (PNG Formatı): [ ] Başarılı [ ] Başarısız
Test 5 (Dosya Kontrolü): [ ] Başarılı [ ] Başarısız

Kullanılan Görüntü: ___________
İşlem Süresi: ___________
Oluşturulan Dosyalar: ___________

Notlar: ___________
```

