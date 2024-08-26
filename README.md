# Prototyping-Sistem-Keamanan-berbasis-Face-Recognition
Proyek ini bertujuan untuk mengembangkan sebuah prototipe sistem keamanan yang menggunakan teknologi pengenalan wajah (face recognition). Sistem ini dirancang untuk meningkatkan keamanan pada area akses terbatas seperti rumah, kantor, laboratorium, dan ruangan khusus lainnya. 
Memanfaatkan kamera untuk menangkap gambar wajah pengguna dan menggunakan algoritma pengenalan wajah untuk memverifikasi identitas mereka. Jika wajah yang terdeteksi sesuai dengan data yang telah terdaftar, sistem akan memberikan akses masuk atau keluar. Dengan demikian, sistem ini dapat mencegah akses tidak sah dan meningkatkan keamanan keseluruhan.

# Fitur
•	Real Time Face Recognition  
•	Face Detection  
•	Attandaces(Pencatatan Akses) Database pada Excel  
•	Access Control melalui Sign Up untuk User baru dan Sign In/Buka Pintu untuk User yang sudah terdaftar  
•	Anti spoofing untuk memastikan: Your Human or Img/Vidio melalui Validasi 2 langkah; Kedip 3  kali dan Wajah menghadap ke kamera  
•	Antarmuka Pengguna(UI) yang Interaktif 

# Teknologi yang digunakan
•	**Python**: Bahasa Pemrogramanan utama untuk pengembangan  
•	**OpenCV**: Library untuk pemrosesan gambar dan deteksi wajah  
•	**MediaPipe**: Library untuk deteksi dan landmarks pada wajah  
•	**Pillow**: Library untuk manipulasi gambar  
•	**Numpy**: Library untuk Komputasi ilmiah.  
•	**Face Recognition**: Library untuk pengenalan wajah  
•	**Tkinter**: Library untuk pembuatan antarmuka pengguna  
•	**Openpyxl**: Library untuk mengelola file Excel  
•	**Datetime**: Library untuk pengelolaan tanggal dan waktu

# struktur Directory
- **Database:** Berisi file database wajah dan pengguna (Data Inputan)
  - **Faces**
  - **Users**
  - Attandances.xlsx
- **SetUp:** Berisi Desain keperluan sistem (UI)
- faceRecognition.py
- Libraries.txt

# Instalasi
1. Clone repositori ini:
   ```bash
   git clone
   https://github.com/Perseferanda/Prototyping-Sistem-Keamanan-berbasis-face-Recognition.git
   
   cd Prototyping-Sistem-Keamanan-berbasis-face-Recognition
2. Instal dependensi:

**Catatan:**
-  Saat menginstal Libraries, pastikan agar librari Protobuf versi-nya di sesuaikan dengan Face-Recognition jika saat di install dan di rekomendasikan untuk mengupgred ke versi tertentu, maka install lah versi yang di rekomendasikan, Karena akan sangat berpengaruh saat menjalankan programnya.
-  jika tidak bisa menginstal dlib, pastikan untuk anda mengistal CMake terlebih dahulu dan juga menginstal Visual Studio Installer serta mendownload Workloads: Python development dan Dekstop development with C++. (lebih jelasnya tonton tutorial ini: https://youtu.be/eaEndTeUiSU?si=XN8guk4y4o_r0wvp)

   ```bash
   pip install -r Libraries.txt
3. Jalankan Aplikasi
   ```bash
   python faceRecognition.py

# Tampilan Sistem
![Home](https://github.com/Perseferanda/Prototyping-Sistem-Keamanan-berbasis-Face-Recognition/blob/main/UI.png?row=true)
![Home](https://github.com/Perseferanda/Prototyping-Sistem-Keamanan-berbasis-Face-Recognition/blob/main/Testing.png?row=true)

   
