<div align="center">
  <h1 align="center">🎯 CS:GO Python Memory Glow & ESP Script</h1>
  <p align="center">
    <b>Counter-Strike: Global Offensive (Legacy) bellek yapıları ve nesne taraması inceleme aracı.</b>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
    <img src="https://img.shields.io/badge/Win32_API-Memory-blueviolet?style=for-the-badge" />
    <img src="https://img.shields.io/badge/License-MIT-crimson?style=for-the-badge" />
  </p>
</div>

---

### 📖 Proje Hakkında
Bu proje; CS:GO Legacy sürümünün bellek haritası, oyuncu varlık dizileri (`dwEntityList`), glow nesne yöneticisi (`dwGlowObjectManager`) ve bellek içi işaretçi zincirlerini (pointer chains) Python ve Win32 API kullanarak analiz etmek amacıyla yazılmıştır.

> ⚠️ **Disclaimer:** Bu repo yalnızca oyun güvenliği, bellek manipülasyonu ve tersine mühendislik eğitim araştırmaları için hazırlanmıştır.

---

### 🚀 Özellikler
- **Glow / ESP Nesne Analizi:** `client.dll` modül tabanını dinamik olarak okuyarak düşman/takım ayrımı yapar.
- **Düşük Kaynak Tüketimi:** Optimize edilmiş döngü gecikmeleri ve işlemci dostu bellek okuma/yazma.
- **Dinamik Modül Çözümleme:** `client.dll` ve `engine.dll` adreslerini runtime sırasında yakalar.

---

### 📂 Proje Yapısı
```text
Csgo-Python-Wallhack-Script/
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── requirements.txt
