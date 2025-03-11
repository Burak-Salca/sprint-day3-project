# 📺 Insider QA Bootcamp Sprint-3 Gün-3 Projesi

Bu proje, Insider QA Bootcamp'in 3. sprint'inde geliştirilen bir Python uygulamasıdır. Proje, temel programlama konseptlerini ve OOP (Nesne Yönelimli Programlama) prensiplerini içeren 8 farklı soru/görev içermektedir.

## 🎯 Proje İçeriği

Proje aşağıdaki soruları/görevleri içermektedir:
1. Restoran hesap bölüşme hesaplayıcı
2. Popülasyon hesaplama simülasyonu
3. Vücut Kitle İndeksi (BMI) hesaplayıcı
4. Tekrar eden/etmeyen sayı analizi
5. Öğrenci not sistemi
6. FizzBuzz implementasyonu
7. Quiz uygulaması
8. Akıllı TV Kumanda sistemi

## 🏗️ Proje Yapısı

Proje, OOP prensiplerini takip eden modüler bir yapıya sahiptir:

```
project/
├── interfaces/
│   └── remote.py
├── models/
│   └── remote.py
├── questions/
│   ├── question1.py
│   ├── question2.py
│   └── ...
├── utils/
│   ├── InputValidator.py
│   └── WaitForUserInput.py
└── main/
    └── main.py
```

## 📦 Paketler ve Görevleri

### 1. interfaces/
- `remote.py`: TV kumandası için soyut metodları tanımlar

### 2. models/
- `remote.py`: TV kumandası implementasyonunu içerir

### 3. utils/
- `InputValidator.py`: Kullanıcı girişi validasyonu için yardımcı fonksiyonlar
- `WaitForUserInput.py`: Kullanıcı etkileşimi için bekleme fonksiyonu

### 4. questions/
- Her bir soru için ayrı modüller içerir
- Kod organizasyonu ve bakımı kolaylaştırır

## 📺 8. Soru - Akıllı TV Kumanda Sistemi

8. soru, projenin OOP prensiplerini en kapsamlı şekilde uygulayan bölümüdür. Bu bölümde:

- Abstract metodlar kullanarak TV kumandası fonksiyonlarının tanımlanması
- Kanal yönetimi (ekleme, silme, arama)
- Ses kontrolü
- Favori kanal yönetimi
- TV açma/kapama işlemleri

gibi gerçek bir TV kumandasının fonksiyonları implemente edilmiştir.

## 🚀 Projeyi Çalıştırma

1. Python 3.x'in yüklü olduğundan emin olun

2. Projeyi çalıştırma:
```bash
python main/main.py
```
