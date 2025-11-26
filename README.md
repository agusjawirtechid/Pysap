
<div align="center">

# **PySAP**
### **Python Simple Chat Application**
Realtime Terminal Chat App built with **Python** & **Firebase Realtime Database**

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python)
![Firebase](https://img.shields.io/badge/Firebase-Realtime%20Database-orange?style=for-the-badge&logo=firebase)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## ✨ **Fitur Utama**

| Fitur | Deskripsi |
|--------|-----------|
| 💬 **Chat Real-time** | Pesan muncul seketika tanpa refresh |
| 🎨 **UI Terminal Modern** | Tampilan berwarna & nyaman digunakan |
| 💾 **Local Storage** | Simpan riwayat chat pada `history.txt` |
| 🔐 **Auto-Login** | Username tersimpan otomatis |
| 👥 **Notifikasi User** | Info user Join / Leave |
| 🔁 **Auto-Reconnect** | Koneksi stabil & recovery otomatis |
| 🔔 **Notifikasi sistem** | Untuk status server & aktivitas chat |

---

## 📌 **Prasyarat**
- Python **3.6+**
- `requests` package
- Koneksi internet aktif

---

## 🛠 **Instalasi**

### 📱 **Termux (Android)**
```bash
pkg update && pkg upgrade
pkg install python git
pip install requests
git clone https://github.com/agusjawirtechid/Pysap.git
cd Pysap
python pysap.py

🐧 Linux (Ubuntu/Debian)

sudo apt update
sudo apt install python3 python3-pip git
pip3 install requests
git clone https://github.com/agusjawirtechid/Pysap.git
cd Pysap
python3 pysap.py

🪟 Windows

pip install requests
git clone https://github.com/agusjawirtechid/Pysap.git
cd Pysap
python pysap.py

🍎 macOS

brew install python git
pip3 install requests
git clone https://github.com/agusjawirtechid/Pysap.git
cd Pysap
python3 pysap.py


---

🚀 Cara Menggunakan

1. Jalankan aplikasi


2. Masukkan username


3. Pilih auto-login jika diinginkan


4. Ketik pesan lalu Enter untuk mengirim


5. Gunakan:



/logout  → Keluar dari akun
/exit    → Keluar dari aplikasi


---

📁 File Output

File	Fungsi

history.txt	Menyimpan riwayat chat lokal
user_config.txt	Menyimpan username & auto-login



---

🐛 Troubleshooting

Masalah	Solusi

Module Not Found: requests	pip install requests
git not found	Install git sesuai OS
Koneksi lambat / putus	Sistem akan mencoba reconnect otomatis



---

🤝 Kontribusi

Pull request & issue sangat diterima!
Silakan fork dan bantu kembangkan fitur baru 🙌


---

📄 Lisensi

Distributed under the MIT License
Free to use, modify, and distribute.


---

👨‍💻 Developer

agusjawirtechid
Repository: https://github.com/agusjawirtechid/Pysap
