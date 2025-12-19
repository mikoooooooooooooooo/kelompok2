# Kelompok Dua – Aplikasi Streamlit

Player:
1. Jessica OS
2. Alma Dewi
3. Jatmiko
4. Chika

Repositori ini berisi kode sumber untuk aplikasi Streamlit yang dapat diakses di:

👉 **https://kelompokdua.streamlit.app/**

Aplikasi ini dikembangkan sebagai bagian dari tugas penganti UAS Matkul Prakbigdata menggunakan Streamlit oleh **Kelompok Dua** untuk menyajikan visualisasi interaktif data ekonomi makro, khususnya indikator negara-negara ASEAN.

---

## 1. Deskripsi Singkat

Aplikasi ini merupakan **dashboard interaktif berbasis web** yang dibangun menggunakan **Streamlit**.  
Tujuan utamanya adalah untuk:

- Menyajikan visualisasi data indikator ekonomi antar negara secara mudah dan informatif.
- Memudahkan pengguna mengeksplorasi data melalui filter interaktif (negara, indikator, tahun).
- Menjadi contoh sederhana penerapan Python + Streamlit untuk analisis data sekunder berbasis World Bank.

Pengguna dapat mengakses aplikasi langsung melalui browser tanpa perlu instalasi tambahan.

---

## 2. Fitur Utama

- ✅ **Halaman Beranda (Home Page)**
  - Menampilkan pengantar singkat tentang aplikasi dan navigasi fitur.

- 📊 **Visualisasi Data Ekonomi**
  - Grafik garis/bar untuk melihat tren pertumbuhan indikator antar negara.
  - Tabel data yang dapat di-*scroll*, dipilih, dan difilter.

- 🌍 **Filter / Pemilihan Negara & Tahun**
  - Pilih satu atau beberapa negara ASEAN.
  - Pilih rentang tahun.
  - Pilih indikator spesifik (misalnya: GDP per kapita, inflasi, FDI, suku bunga, nilai tukar, ekspor, dsb).

- ⚙️ **Pengaturan / Sidebar**
  - Kontrol visualisasi (tipe grafik, tampilan agregat, mode perbandingan negara).

- ℹ️ **Halaman Tentang (Tentang / About Page)**
  - Informasi tugas, identitas anggota, tujuan aplikasi, dan deskripsi singkat ekonomi ASEAN.

Aplikasi ini dirancang ringan, intuitif, dan siap dipakai melalui browser desktop maupun mobile.

---

## 3. Teknologi yang Digunakan

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — UI berbasis browser
- [Pandas](https://pandas.pydata.org/) — pengolahan data tabular
- [Plotly / Altair / Matplotlib] — visualisasi interaktif
- Sumber data:
  - **World Bank Data CSV**
    
Jika kamu ingin menambah dependensi lain (sklearn, numpy, seaborn, dsb), tuliskan pada `requirements.txt`.

---

## 4. Cara Menjalankan Secara Lokal

Jika kamu ingin menjalankan aplikasi ini di komputer sendiri:

### 4.1. Prasyarat
Pastikan sudah menginstal:

- Python 3.8+
- pip
- Koneksi internet (untuk pemanggilan data World Bank)

### 4.2. Clone Repositori

```bash
git clone https://github.com/USERNAME/kelompok-dua-streamlit.git
cd kelompok-dua-streamlit
