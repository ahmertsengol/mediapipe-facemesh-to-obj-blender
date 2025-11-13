# MediaPipe Face Mesh to OBJ - Kullanım Kılavuzu

Bu proje, MediaPipe kullanarak 2D fotoğraflardan 3D yüz modelleri (OBJ formatında) oluşturmanıza olanak sağlar.

## 📋 Gereksinimler

- Python 3.10 veya üzeri
- pip (Python paket yöneticisi)

## 🚀 Kurulum

### 1. Bağımlılıkları Yükle

Proje dizininde şu komutu çalıştırın:

```bash
pip install -r requirements.txt
```

Eğer bu komut başarısız olursa, gerekli kütüphaneleri manuel olarak yükleyebilirsiniz:

```bash
pip install mediapipe==0.9.0 numpy==1.23.5 opencv-contrib-python==4.6.0.66 scikit-image==0.19.3
```

**Not:** macOS'ta OpenCV kurulumu için şu komutu kullanabilirsiniz:
```bash
pip install opencv-python opencv-contrib-python
```

## 💻 Kullanım

### Temel Kullanım

Bir görüntüyü 3D modele dönüştürmek için:

```bash
python mediapipe_to_obj.py -i <görüntü_yolu> -o <çıktı_yolu>
```

### Örnekler

**Örnek 1:** Görüntü yolunu belirtme
```bash
python mediapipe_to_obj.py -i examples/gakki.jpg -o results/gakki_model
```

**Örnek 2:** Sadece görüntü yolunu belirtme (çıktı otomatik oluşturulur)
```bash
python mediapipe_to_obj.py -i examples/gakki.jpg
```
Bu durumda çıktı `./results/gakki.obj` olarak kaydedilir.

**Örnek 3:** İnteraktif mod (görüntü yolunu program sorar)
```bash
python mediapipe_to_obj.py
```
Program çalıştığında görüntü yolunu girmeniz istenir.

## 📁 Çıktı Dosyaları

Program çalıştığında şu dosyalar oluşturulur:

- `*.obj` - 3D model dosyası
- `*.mtl` - Materyal dosyası
- `*_texture.jpg` - Yüz dokusu (texture) görüntüsü

## ⚠️ Önemli Notlar

1. **Yüz Tespiti:** Program tek bir yüz tespit eder. Görüntüde birden fazla yüz varsa ilk tespit edilen yüz kullanılır.

2. **Görüntü Formatları:** 
   - JPG formatı önerilir
   - PNG formatı otomatik olarak JPG'ye dönüştürülmeye çalışılır

3. **Bilinen Sorunlar:**
   - Burun tespiti her zaman mükemmel olmayabilir
   - Açık gözler daha iyi tespit edilir

4. **Sonuçlar:** Çıktı dosyaları varsayılan olarak `./results/` klasörüne kaydedilir.

## 🎨 Kullanım Senaryoları

- Fotoğraflardan 3D avatar oluşturma
- Karakter modelleme
- Yüz animasyonu için 3D modeller
- İllüstrasyonlardan 3D modeller (açık gözlerle daha iyi çalışır)

## 🔧 Sorun Giderme

**Hata: "Unable to use a PNG"**
- PNG dosyasını JPG formatına dönüştürüp tekrar deneyin

**Hata: "No face detected"**
- Görüntüde net bir yüz olduğundan emin olun
- Görüntü kalitesini artırın
- Farklı bir açıdan çekilmiş görüntü deneyin

**Bağımlılık Hataları:**
- Python sürümünüzün 3.10+ olduğundan emin olun
- Virtual environment kullanmanız önerilir:
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # macOS/Linux
  pip install -r requirements.txt
  ```

## 📚 Ek Bilgiler

- MediaPipe 468 yüz landmark noktası kullanır
- Model mobil cihazlar için optimize edilmiştir, bu yüzden CPU'da da hızlı çalışır
- Oluşturulan OBJ dosyaları Blender, Maya, Unity gibi 3D yazılımlarda açılabilir

