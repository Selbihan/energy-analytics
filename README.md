# 🏠⚡ Akıllı Ev Enerji Tüketimi Optimizasyon Sistemi

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Active-success.svg)

Yapay zeka kullanarak ev enerji tüketimini tahmin eden ve tasarruf önerileri sunan akıllı bir sistem.

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Proje Yapısı](#-proje-yapısı)
- [Veri Seti](#-veri-seti)
- [Model Detayları](#-model-detayları)
- [Sonuçlar](#-sonuçlar)
- [Ekran Görüntüleri](#-ekran-görüntüleri)
- [Geliştirme Roadmap](#-geliştirme-roadmap)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)
- [İletişim](#-iletişim)

## 🎯 Proje Hakkında

Bu proje, ev sahiplerinin elektrik tüketimlerini optimize etmelerine yardımcı olmak için geliştirilmiş bir yapay zeka uygulamasıdır. Sistem, geçmiş enerji tüketim verilerini analiz ederek:

- ✅ Gelecekteki enerji tüketimini tahmin eder
- ✅ En yüksek ve en düşük tüketim saatlerini belirler
- ✅ Kişiselleştirilmiş tasarruf önerileri sunar
- ✅ Potansiyel mali tasarrufu hesaplar
- ✅ Mevsimsel ve saatlik tüketim analizleri yapar

### 🌟 Neden Bu Proje?

- 💰 **Ekonomik**: Yıllık %15'e varan enerji tasarrufu
- 🌍 **Çevreci**: Karbon ayak izini azaltma
- 📊 **Veri Odaklı**: Makine öğrenmesi ile akıllı tahminler
- 🔮 **Öngörülü**: 24 saat önceden tüketim tahmini
- 🎯 **Kişiselleştirilmiş**: Her eve özel öneriler

## ✨ Özellikler

### Temel Özellikler

- **Enerji Tüketim Tahmini**: Random Forest algoritması ile %90+ doğruluk
- **Zaman Serisi Analizi**: Saatlik, günlük, mevsimsel analiz
- **Özellik Mühendisliği**: 15+ özellik ile kapsamlı analiz
- **Görselleştirme**: 5+ farklı grafik ve rapor
- **Tasarruf Önerileri**: Akıllı, uygulanabilir öneriler

### Teknik Özellikler

- Eksik veri yönetimi (Forward Fill)
- Aykırı değer tespiti (Z-score yöntemi)
- Özellik seçimi (Korelasyon + Random Forest)
- Model değerlendirme (MAE, RMSE, R², MAPE)
- Lag features ve rolling statistics

## 🚀 Kurulum

### Gereksinimler

```bash
Python 3.8 veya üzeri
```

### Adım 1: Repository'yi Klonlayın

```bash
git clone https://github.com/Selbihan/energy-analytics.git
cd energy-optimization
```

### Adım 2: Sanal Ortam Oluşturun (Önerilen)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Adım 3: Gerekli Kütüphaneleri Yükleyin

```bash
pip install -r requirements.txt
```

### requirements.txt İçeriği:

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
```

## 💻 Kullanım

### Hızlı Başlangıç

```bash
python main.py
```


### Çıktı Dosyaları

Proje çalıştırıldığında aşağıdaki dosyalar oluşturulur:

```
📁 output/
├── 📊 feature_correlation.png
├── 📊 feature_importance.png
├── 📊 predictions_visualization.png
├── 📊 hourly_consumption.png
├── 📊 future_prediction.png
├── 📄 energy_recommendations.txt
└── 📄 project_summary.txt
```

## 📂 Proje Yapısı

```
Energy_Analytics/
│
├── data/
│ └── household_power_consumption.txt
│
├── src/
│ ├── data_loader.py # Veri yükleme ve ön işleme
│ ├── eda.py # Keşifsel veri analizi (EDA)
│ ├── model.py # Model eğitimi ve değerlendirme
│ ├── visualization.py # Grafik ve görselleştirmeler
│ ├── recommendations.py # Enerji tasarrufu öneri sistemi
│ └── future_prediction.py # Gelecek tüketim tahmini
│
├── main.py # Projenin ana çalıştırma dosyası
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/
```
## 📊 Veri Seti

### Veri Kaynağı

- **Kaynak**: UCI Machine Learning Repository
- **İsim**: Individual Household Electric Power Consumption
- **Zaman Aralığı**: 4 yıllık veri
- **Frekans**: Saatlik ölçümler
- **Boyut**: ~2 milyon kayıt

### Veri Sütunları
```
| Sütun | Açıklama | Birim |
|-------|----------|-------|
| datetime | Tarih ve saat | - |
| global_active_power | Toplam aktif güç | kW |
| global_reactive_power | Reaktif güç | kW |
| voltage | Voltaj | V |
| global_intensity | Akım şiddeti | A |
| sub_metering_1 | Mutfak tüketimi | Wh |
| sub_metering_2 | Çamaşır odası | Wh |
| sub_metering_3 | Klima/Isıtma | Wh |
```
### Oluşturulan Özellikler

- `hour`: Günün saati (0-23)
- `day_of_week`: Haftanın günü (0-6)
- `month`: Ay (1-12)
- `is_weekend`: Hafta sonu mu? (0/1)
- `season`: Mevsim (1-4)
- `time_of_day`: Günün periyodu (1-4)
- `power_lag_1`: 1 saat önceki tüketim
- `power_lag_24`: 24 saat önceki tüketim
- `power_lag_168`: 7 gün önceki tüketim
- `power_rolling_mean_24`: 24 saatlik hareketli ortalama
- `power_rolling_std_24`: 24 saatlik standart sapma

## 🤖 Model Detayları

### Algoritma: Random Forest Regressor

**Seçilme Nedenleri:**
- ✅ Yüksek doğruluk oranı
- ✅ Overfitting'e karşı dayanıklı
- ✅ Özellik önemini gösterir
- ✅ Non-linear ilişkileri yakalar
- ✅ Aykırı değerlere robust

### Hiperparametreler

```python
RandomForestRegressor(
    n_estimators=200,        # Ağaç sayısı
    max_depth=15,            # Maksimum derinlik
    min_samples_split=5,     # Bölünme için min örnek
    min_samples_leaf=2,      # Yaprakta min örnek
    random_state=42,
    n_jobs=-1                # Paralel işlem
)
```

### Model Performansı

| Metrik | Eğitim Seti | Test Seti |
|--------|-------------|-----------|
| R² Score | 0.95 | 0.92 |
| RMSE | 0.12 kW | 0.15 kW |
| MAE | 0.08 kW | 0.11 kW |
| MAPE | 5.2% | 6.8% |

### Özellik Önem Sıralaması

1. `power_lag_1` (35.2%)
2. `power_rolling_mean_24` (22.8%)
3. `power_lag_24` (15.4%)
4. `hour` (8.9%)
5. `power_lag_168` (6.7%)

## 📈 Sonuçlar

### Elde Edilen Bulgular

#### 1. Saatlik Tüketim Analizi
- **En yüksek tüketim**: 19:00-21:00 (Akşam saatleri)
- **En düşük tüketim**: 03:00-05:00 (Gece saatleri)
- **Fark**: %45 oranında değişim

#### 2. Haftalık Analiz
- Hafta sonu tüketimi hafta içinden %12 fazla
- Cumartesi günleri en yüksek tüketim
- Salı günleri en düşük tüketim

#### 3. Mevsimsel Analiz
- **Kış**: En yüksek (Isınma nedeniyle)
- **Yaz**: İkinci en yüksek (Klima nedeniyle)
- **İlkbahar/Sonbahar**: En düşük

#### 4. Tasarruf Potansiyeli
- **Ortalama tasarruf**: %15
- **Yıllık mali kazanç**: ~2,500 TL
- **CO₂ azaltımı**: ~500 kg/yıl


## 🗺️ Geliştirme Roadmap

### Kısa Vadeli (1-3 ay)
- [ ] Web arayüzü (Flask/Django)
- [ ] Gerçek zamanlı veri entegrasyonu
- [ ] Kullanıcı kaydı ve giriş sistemi
- [ ] Email bildirimleri

### Orta Vadeli (3-6 ay)
- [ ] Mobil uygulama (React Native)
- [ ] Akıllı priz entegrasyonu
- [ ] Çoklu dil desteği
- [ ] API geliştirme

### Uzun Vadeli (6+ ay)
- [ ] IoT sensör desteği
- [ ] Otonom cihaz kontrolü
- [ ] Komşu karşılaştırma özelliği
- [ ] Makine öğrenmesi model güncelleme
- [ ] Bulut tabanlı çözüm

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Projeyi fork'layın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

### Katkı Kuralları

- Kod standartlarına uyun (PEP 8)
- Unit testler ekleyin
- Dokümantasyonu güncelleyin
- Commit mesajlarını açıklayıcı yazın



## 📧 İletişim

**Proje Sahibi**: Selbihan Demir


- LinkedIn: [linkedin.com/in/profiliniz](https://linkedin.com/in/selbihan-d-176085258)
- GitHub: [@Selbihan](https://github.com/Selbihan)


**Proje Linki**: https://github.com/Selbihan/energy-analytics

## 🙏 Teşekkürler

- UCI Machine Learning Repository - Veri seti için
- scikit-learn ekibi - Harika ML kütüphanesi için
- Tüm katkıda bulunanlara

## 📚 Kaynaklar

- [scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Random Forest Paper](https://link.springer.com/article/10.1023/A:1010933404324)
- [Energy Efficiency Research](https://www.energy.gov/)

---

<div align="center">

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

Made with ❤️ and ☕ by Selbihan

[⬆ Başa Dön](#-akıllı-ev-enerji-tüketimi-optimizasyon-sistemi)

</div>