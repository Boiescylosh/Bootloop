# Diagnostics & System Flow

Dokumentasi ini menjelaskan mekanisme kegagalan sistem yang menyebabkan siklus booting tanpa akhir.

---

# Siklus Kerja (The Bootloop Cycle)

| Tahap | Status | Aksi Sistem |
| :--- | :--- | :--- |
| **Power On** | *Start* | Bootloader menginisialisasi Hardware. |
| **Kernel Load** | *Processing* | Sistem mencoba memuat Kernel & Partisi `/system`. |
| **Validation** | *Critical* | Terdeteksi file korup, hilang, atau *permission error*. |
| **Watchdog** | *Panic* | Sistem keamanan mendeteksi kegagalan 'init' process. |
| **Reboot** | *Loop* | Perangkat dipaksa restart dan kembali ke Tahap 1. |

---

# Dampak Terhadap Perangkat 

Kondisi bootloop yang dibiarkan terus-menerus akan mengakibatkan:

1. **Battery Exhaustion:** Konsumsi daya melonjak drastis karena proses booting adalah fase terberat bagi CPU.
2. **Thermal Overheat:** Beban kerja konstan tanpa jeda pendinginan membuat komponen internal panas.
3. **Data Inaccessible:** Enkripsi partisi data tidak bisa terbuka, sehingga file user terkunci di dalam.
4. **Hardware Stress:** Potensi kerusakan permanen pada memori internal (eMMC/UFS) akibat siklus baca/tulis yang gagal.

---

> **Catatan Teknis:** Bootloop seringkali disebabkan oleh modifikasi sistem yang tidak kompatibel atau kegagalan saat proses *OTA Update*.


# WHAT IS A BOOTLOOP 
**Bootloop** itu sebenarnya kondisi di mana perangkat (kayak HP atau PC) gagal masuk ke sistem dan malah restart terus-menerus di tampilan awal. Nah, tools Bootloop ini fungsinya buat ngetes lewat file biner (.exe). hasil rancangan ini biar bisa eksperimen atau prank "error" di Virtual Box, biar lu bisa paham gimana sistem bereaksi tanpa perlu ngerusak device asli.

# Installation ( Termux )

1. pkg update && pkg upgrade -y
2. pkg install python -y
3. pkg install git -y
4. termux-setup-storage
5. git clone https://github.com/Boiescylosh/Bootloop
6. cd Bootloop
7. python Bootloop.py

---

# Installation ( Linux )

1. sudo apt update && sudo apt upgrade -y
2. sudo apt install python3 -y
3. sudo apt install git -y
4. git clone https://github.com/Boiescylosh/Bootloop
5. cd Bootloop
6. python3 Bootloop.py

---

# Installation ( MacOS )

1. brew install python
2. brew install git
3. git clone https://github.com/Boiescylosh/Bootloop
4. cd Bootloop
5. python3 Bootloop.py

---

# Installation ( Windows )

1. Install [Python](https://www.python.org/downloads/) (Wajib centang "Add Python to PATH")
2. Install [Git for Windows](https://git-scm.com/download/win)
3. Buka CMD atau PowerShell, lalu ketik:
   - git clone https://github.com/Boiescylosh/Bootloop
   - cd Bootloop
   - python Bootloop.py

---

![preview](https://d.top4top.io/p_372387fqj0.jpg)

![preview](https://e.top4top.io/p_3723cpy8q1.jpg)

# Information
> **BACA:** Alat ini dibuat hanya untuk tujuan edukasi dan pengujian sistem pribadi (Self-Testing). Penggunaan alat ini untuk tujuan ilegal atau merugikan pihak lain. Author tidak bertanggung jawab atas segala kerusakan yang ditimbulkan.

---

