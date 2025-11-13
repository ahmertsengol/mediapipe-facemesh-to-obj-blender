# 🔒 Güvenli Kurulum Kılavuzu - Sanal Python Ortamı

Bu kılavuz, projeyi izole bir sanal ortamda güvenli bir şekilde kurmanızı sağlar.

## 📋 Ön Gereksinimler

- Python 3.10 veya üzeri
- pip (Python paket yöneticisi)

## 🚀 Adım Adım Kurulum

### Adım 1: Python Sürümünü Kontrol Et

```bash
python3 --version
```

**Beklenen Çıktı:** `Python 3.10.x` veya üzeri

Eğer Python yüklü değilse:
- macOS: `brew install python3`
- Linux: `sudo apt-get install python3 python3-pip`
- Windows: [python.org](https://www.python.org/downloads/) adresinden indirin

### Adım 2: Proje Dizinine Git

```bash
cd mediapipe-facemesh-to-obj
```

### Adım 3: Sanal Ortam Oluştur

```bash
python3 -m venv venv
```

Bu komut `venv` adında bir klasör oluşturur ve içine izole bir Python ortamı kurar.

**Önemli:** Bu klasörü `.gitignore` dosyasına eklemeniz önerilir (zaten ekli olmalı).

### Adım 4: Sanal Ortamı Aktifleştir

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

**Başarılı Aktifleştirme İşareti:**
Komut satırınızın başında `(venv)` yazısını görmelisiniz:
```
(venv) username@computer:~/mediapipe-facemesh-to-obj$
```

### Adım 5: pip'i Güncelle

```bash
pip install --upgrade pip
```

Bu adım, paket yöneticisinin en son sürümünü kullanmanızı sağlar.

### Adım 6: Bağımlılıkları Yükle

```bash
pip install -r requirements.txt
```

Bu işlem birkaç dakika sürebilir. Yüklenen paketler:
- `mediapipe` - Yüz tespiti için
- `numpy` - Sayısal işlemler için
- `opencv-contrib-python` - Görüntü işleme için
- `scikit-image` - Görüntü dönüşümleri için

### Adım 7: Kurulumu Doğrula

```bash
python -c "import mediapipe; import cv2; import numpy; import skimage; print('✅ Tüm paketler başarıyla yüklendi!')"
```

**Beklenen Çıktı:** `✅ Tüm paketler başarıyla yüklendi!`

### Adım 8: Yüklü Paketleri Kontrol Et

```bash
pip list
```

veya sadece proje paketlerini görmek için:

```bash
pip list | grep -E "(mediapipe|numpy|opencv|scikit)"
```

## ✅ Kurulum Tamamlandı!

Artık projeyi kullanmaya hazırsınız. İlk test için:

```bash
python mediapipe_to_obj.py -i examples/gakki.jpg
```

## 🔄 Sanal Ortamı Kullanma

### Her Çalıştırmada

Her yeni terminal oturumunda sanal ortamı aktifleştirmeniz gerekir:

```bash
cd mediapipe-facemesh-to-obj
source venv/bin/activate  # macOS/Linux
# veya
venv\Scripts\activate      # Windows
```

### Sanal Ortamdan Çıkma

```bash
deactivate
```

## 🗑️ Sanal Ortamı Silme

Eğer sanal ortamı tamamen kaldırmak isterseniz:

```bash
deactivate  # Önce çıkış yapın
rm -rf venv  # macOS/Linux
# veya
rmdir /s venv  # Windows
```

## 🔒 Güvenlik Avantajları

Sanal ortam kullanmanın faydaları:

1. **İzolasyon:** Sistem Python'unuzu kirletmez
2. **Versiyon Kontrolü:** Her proje için farklı paket versiyonları kullanabilirsiniz
3. **Kolay Temizlik:** Projeyi silmek yeterli
4. **Çakışma Önleme:** Farklı projelerin bağımlılıkları birbirini etkilemez

## 📦 Paket Yönetimi

### Yeni Paket Ekleme

```bash
source venv/bin/activate
pip install paket_adi
pip freeze > requirements.txt  # Güncelle
```

### Paket Güncelleme

```bash
source venv/bin/activate
pip install --upgrade paket_adi
```

### Paket Kaldırma

```bash
source venv/bin/activate
pip uninstall paket_adi
```

## 🐛 Sorun Giderme

### Sorun: "venv: command not found"

**Çözüm:** Python'un `venv` modülü yüklü olmayabilir:
```bash
python3 -m ensurepip --upgrade
python3 -m venv venv
```

### Sorun: "Permission denied"

**Çözüm:** Sanal ortamı kullanıcı dizininizde oluşturun, sudo kullanmayın.

### Sorun: Paketler yüklenmiyor

**Çözüm:**
1. İnternet bağlantınızı kontrol edin
2. pip'i güncelleyin: `pip install --upgrade pip`
3. Sanal ortamın aktif olduğundan emin olun: `which python` komutu `venv` içinde bir yol göstermeli

### Sorun: "No module named X"

**Çözüm:** Sanal ortamın aktif olduğundan emin olun:
```bash
source venv/bin/activate
which python  # venv/bin/python göstermeli
```

## 📝 Özet Komutlar

```bash
# Kurulum
cd mediapipe-facemesh-to-obj
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Kullanım
source venv/bin/activate
python mediapipe_to_obj.py -i examples/gakki.jpg

# Çıkış
deactivate
```

## 🎯 Sonraki Adımlar

Kurulum tamamlandıktan sonra:
1. [KULLANIM.md](KULLANIM.md) dosyasını okuyun
2. [TEST_KILAVUZU.md](TEST_KILAVUZU.md) ile test edin
3. Kendi görüntülerinizle deneyin!

