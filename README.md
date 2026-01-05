# AWS AI League - Jakarta Tourist Information Virtual Assistant

## 📋 Project Overview

Project ini dibuat untuk kompetisi **AWS AI League** dengan fokus membuat asisten virtual wisata Jakarta yang cerdas dan berbudaya menggunakan fine-tuning model AI.

## 🎯 Tujuan Utama

Mengembangkan asisten virtual yang dapat memberikan rekomendasi wisata Jakarta yang:
- ✅ Akurat dan terkini
- ✅ Mencerminkan budaya lokal
- ✅ Ramah dan informatif
- ✅ Berfokus pada informasi harga dan tempat

## 📁 Struktur Project

```
AI League/
├── 📄 Dataset Files
│   ├── 1.1.jakarta_tourism_dataset_50.jsonl      # Dataset awal 50 entries
│   ├── 1.2.jakarta_tourism_pricing_2025.jsonl    # Dataset fokus harga 2025
│   ├── 1.ai-focus-on-price-and-place.jsonl        # Dataset sintetis fokus harga & tempat
│   ├── 2.ai-league-datashet.jsonl                 # Dataset utama 118KB
│   ├── 3.ai-league-datashet 200 -> 250 edited.jsonl # Dataset edit 200-250 entries
│   ├── 4.ai-league-datashet 250.jsonl             # Dataset 250 entries
│   ├── 5.ai-league-datashet 300.jsonl             # Dataset 300 entries
│   ├── template_dataset.jsonl                     # Template dataset
│   └── train.jsonl                                # Dataset training
├── 📚 Documentation
│   └── Pre-Event - AWS AI League Introduction.pdf  # Dokumentasi resmi
├── 🛠️ Utilities
│   └── read_pdf.py                                # Script untuk ekstrak PDF
└── 📖 README.md                                   # File ini
```

## 📊 Format Dataset

Semua dataset menggunakan format **JSONL** dengan struktur triplet:

```json
{
  "instruction": "Pertanyaan pengguna",
  "context": "Konteks tambahan dari pengguna",
  "response": "Jawaban yang informatif dan ramah"
}
```

### 📝 Contoh Entry

```json
{
  "instruction": "Berapa harga tiket masuk Taman Mini Indonesia Indah untuk wisatawan domestik?",
  "context": "Saya berencana mengajak keluarga berlibur akhir pekan ini.",
  "response": "Selamat siang, Pak/Bu! Untuk wisataan domestik, harga tiket masuk TMII per Agustus 2025 adalah Rp30.000 per orang untuk dewasa dan Rp15.000 untuk anak-anak (usia 3-12 tahun). Ada juga paket keluarga seharga Rp75.000 untuk 2 dewasa dan 2 anak."
}
```

## 🔧 Teknologi yang Digunakan

- **AWS SageMaker** - Fine-tuning model
- **AWS SageMaker Unified Studio** - Development environment
- **Amazon S3** - Storage dataset
- **AWS PartyRock** - Generate dataset sintetis
- **Amazon Q CLI** - Generate dataset berkualitas tinggi

## 📈 Progress Dataset

| File | Ukuran | Jumlah Entries | Fokus |
|------|--------|----------------|-------|
| 1.1.jakarta_tourism_dataset_50.jsonl | 25KB | 50 | Dataset awal |
| 1.2.jakarta_tourism_pricing_2025.jsonl | 15KB | ~30 | Harga 2025 |
| 1.ai-focus-on-price-and-place.jsonl | 64KB | ~100 | Harga & tempat |
| 2.ai-league-datashet.jsonl | 118KB | ~200 | Dataset utama |
| 3.ai-league-datashet 200 -> 250 edited.jsonl | 208KB | 50 | Edit lanjutan |
| 4.ai-league-datashet 250.jsonl | 176KB | 250 | Versi 250 |
| 5.ai-league-datashet 300.jsonl | 233KB | 300 | Versi final |

## 🚀 Cara Penggunaan

### 1. Persiapan Environment
```bash
# Install dependencies
pip install PyPDF2

# Setup AWS CLI (jika belum)
aws configure
```

### 2. Ekstrak Documentation
```bash
python read_pdf.py
```

### 3. Training Model
```bash
# Upload dataset ke S3
aws s3 cp train.jsonl s3://your-bucket/dataset/

# Start training di SageMaker
# (Lihat dokumentasi AWS untuk detail setup)
```

## 📋 Best Practices

1. **Validasi Dataset** - Selalu test dengan model baseline
2. **Kualitas > Kuantitas** - Fokus pada pertanyaan yang tidak bisa dijawab model dasar
3. **Budaya Lokal** - Pastikan respons mencerminkan budaya Jakarta
4. **Bahasa Ramah** - Gunakan bahasa yang informatif dan friendly

## 🎨 Karakteristik Respons

- **Ramah**: Menggunakan sapaan seperti "Pak/Bu", "Kak", "Bang"
- **Informatif**: Memberikan detail harga, jam buka, transportasi
- **Praktis**: Include tips dan alternatif
- **Budaya**: Menggunakan istilah lokal yang tepat

## 🔍 Fokus Utama

Dataset ini dirancang untuk menjawab pertanyaan tentang:
- 🎫 **Harga tiket** masuk tempat wisata
- 🚗 **Transportasi** umum dan alternatif
- 🏛️ **Tempat wisata** dengan fasilitas spesifik
- 🍜 **Kuliner** khas Betawi
- 🛍️ **Oleh-oleh** dan belanja
- 📍 **Lokasi** dan aksesibilitas

## 📞 Contact & Support

Untuk informasi lebih lanjut tentang AWS AI League:
- 📧 Email: support@aws.ai-league
- 📚 Documentation: Lihat file PDF yang disertakan
- 🌐 Website: AWS AI League Official

## 📄 License

Project ini dibuat untuk kompetisi AWS AI League. Dataset dan code dapat digunakan untuk tujuan edukasi dan pengembangan AI.

---

**Made with ❤️ for AWS AI League 2025**
