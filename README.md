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
   ```bash
   pip install -r requirements.txt
4. Jalankan Aplikasi
   ```bash
   python faceRecognition.py

# Tampilan Sistem
![Home](https://www.google.com/imgres?q=ui%20ux&imgurl=https%3A%2F%2Fosccdn.medcom.id%2Fimages%2Fcontent%2F2022%2F09%2F13%2F21ab8e8d512e1b613a5c8dec5ed481c9.jpg&imgrefurl=https%3A%2F%2Fosc.medcom.id%2Fcommunity%2Fmengenal-ui-ux-design-dan-perbedaannya-4122&docid=qLR3NJIjWxUXtM&tbnid=9DdD5VYUBTrl_M&vet=12ahUKEwjByqbht-aHAxV1n2MGHeGLCN0QM3oECB0QAA..i&w=1280&h=720&hcb=2&ved=2ahUKEwjByqbht-aHAxV1n2MGHeGLCN0QM3oECB0QAA?row=true)

   
