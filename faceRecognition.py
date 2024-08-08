# ___LIBRARY___#
from tkinter import *
import cv2
import numpy as np
import mediapipe as mp
import face_recognition as fr
from PIL import Image, ImageTk
import imutils
import math
import os
from openpyxl import load_workbook
from datetime import datetime


# ___Function Attendaces
def add_attendance(Names, Ids, Statuss):
    """
    Fungsi ini digunakan untuk mencatat kehadiran pengguna dalam file Excel dan
    menerima tiga parameter: Names, Ids, dan Statuss.
    Fungsi ini akan menambahkan baris baru ke worksheet Excel dengan informasi pengguna dan waktu akses.
    """
    # Path file Excel
    file_path = 'E:/AccessControl System/DataBase/Attandances.xlsx'

    # Load workbook dan pilih worksheet aktif
    workbook = load_workbook(file_path)
    sheet = workbook.active

    # Ambil waktu saat ini
    Times = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    # Menambahkan baris baru ke worksheet
    new_row = [Names, Ids, Statuss, Times]
    sheet.append(new_row)

    # Save workbook
    workbook.save(file_path)


# ___Function Profile
def Profile():
    """
    Fungsi ini digunakan untuk menampilkan profil pengguna dan mencatat akses pengguna.

    Langkah-langkah yang dilakukan dalam fungsi ini:
    1. Menginisialisasi variabel global `step` dan `count` menjadi 0.
    2. Membuka jendela baru (screen4) dengan judul "PROFILE" dan ukuran 1280x720 piksel.
    3. Menampilkan gambar latar belakang dengan menggunakan `Imagebc`.
    4. Membaca informasi pengguna dari file teks yang tersimpan berdasarkan nama pengguna (`UserName`).
    5. Mengambil informasi pengguna (Nama, Id, dan Status) dari file teks.
    6. Menambahkan data kehadiran pengguna menggunakan fungsi `add_attendance`.
    7. Mengecek apakah ID pengguna ada dalam daftar `clases`.
    8. Jika ID ditemukan:
        - Menampilkan informasi pengguna (Nama, Id, Status) di lokasi tertentu pada jendela baru.
        - Menampilkan gambar wajah pengguna berdasarkan ID yang disimpan.
    9. Jika ID tidak ditemukan, fungsi ini tidak melakukan tindakan tambahan.
    """

    global step, count, UserName, OutFolderPathUsers
    # Reset Variables
    step = 0
    count = 0

    # Window
    screen4 = Toplevel(screen)
    screen4.title("PROFILE")
    screen4.geometry("1280x720")

    # Image
    bc = Label(screen4, image=Imagebc, text="SIGN IN")
    bc.place(x=0, y=0, relheight=1, relwidth=1)

    # File
    Userfile = open(f"{OutFolderPathUsers}/{UserName}.txt", "r")
    InfoUser = Userfile.read().split(",")
    Name = InfoUser[0]
    Id = InfoUser[1]
    Status = InfoUser[2]

    add_attendance(Name, Id, Status)

    # Check ID
    if Id in clases:
        # Interface
        text01 = Label(screen4, text=f"{Name}")
        text01.place(x=620, y=447)
        text02 = Label(screen4, text=f"{Id}")
        text02.place(x=620, y=516)
        text03 = Label(screen4, text=f"{Status}")
        text03.place(x=620, y=585)

        # Label IMG
        lblimage = Label(screen4)
        lblimage.place(x=540, y=144)

        # Image
        ImgId = cv2.imread(f"{OutFolderPathFaces}/{Id}.png")
        ImgId = cv2.cvtColor(ImgId, cv2.COLOR_RGB2BGR)
        ImgId = Image.fromarray(ImgId)

        IMG = ImageTk.PhotoImage(image=ImgId)

        lblimage.configure(image=IMG)
        lblimage.image = IMG


# ___FaceCode Funtion
def Code_Face(images):
    """
    Fungsi ini digunakan untuk mengonversi gambar wajah menjadi encoding wajah menggunakan
    library face_recognition. Encoding wajah adalah representasi vektor dari fitur-fitur
    wajah yang dapat digunakan untuk membandingkan dan mencocokkan wajah.
    Langkah-langkah yang dilakukan dalam fungsi ini:
    1. Membuat daftar kosong `listcode` untuk menyimpan encoding wajah.
    2. Untuk setiap gambar dalam daftar `images`:
        a. Mengonversi gambar dari format BGR (default OpenCV) ke RGB.
        b. Menghasilkan encoding wajah menggunakan `face_recognition.face_encodings`.
        c. Menambahkan encoding wajah ke daftar `listcode`.
    3. Mengembalikan daftar encoding wajah `listcode`.
    """
    # list
    listcode = []

    # Alternative
    for img in images:
        # Color
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Img Code
        cod = fr.face_encodings(img)[0]
        # Save List
        listcode.append(cod)
    return listcode


# ___Close Window Funtion
def Close_Window():
    """
    Fungsi ini digunakan untuk menutup jendela `screen2` dan mereset variabel global `step` dan `count`.

    Langkah-langkah yang dilakukan dalam fungsi ini:
    1. Mengatur variabel global `step` dan `count` menjadi 0.
    2. Menghancurkan (menutup) jendela `screen2`.
    """
    global step, count
    # Reset
    count = 0
    step = 0
    screen2.destroy()


# Close Window Funtion
def Close_Window2():
    """
    Fungsi ini digunakan untuk menutup jendela `screen3` dan mereset variabel global `step` dan `count`.

    Langkah-langkah yang dilakukan dalam fungsi ini:
    1. Mengatur variabel global `step` dan `count` menjadi 0.
    2. Menghancurkan (menutup) jendela `screen3`.
    """
    global step, count
    # Reset
    count = 0
    step = 0
    screen3.destroy()


# ___Function to crop and save face, also draws rectangle
def crop_and_save_face(frame, bbox, RegId, color=(128, 0, 255)):
    """
    Fungsi ini digunakan untuk memotong dan menyimpan wajah dari frame yang diberikan berdasarkan bounding box (bbox)
    dan menggambar persegi panjang di sekitar wajah.

    Args:
        frame (numpy.ndarray): Gambar/frame yang berisi wajah.
        bbox (tuple): Bounding box yang mendefinisikan area wajah dalam bentuk (xi, yi, w, h).
        RegId (str or None): ID registrasi untuk menyimpan gambar wajah. Jika None, wajah tidak disimpan.
        color (tuple): Warna persegi panjang yang digambar di sekitar wajah (default: (128, 0, 255)).

    Langkah-langkah dalam fungsi ini:
    1. Mendapatkan dimensi gambar/frame (aimg, bimg) dan bounding box (xi, yi, w, h).
    2. Mengatur offset untuk bounding box berdasarkan persentase offsetx dan offsety.
    3. Menyesuaikan bounding box dengan offset yang dihitung.
    4. Menggambar persegi panjang di sekitar wajah pada frame.
    5. Memotong dan menyimpan gambar wajah jika RegId tidak None.
    """
    aimg, bimg, _ = frame.shape
    xi, yi, w, h = bbox
    xi, yi, w, h = int(xi * bimg), int(yi * aimg), int(w * bimg), int(h * aimg)

    # Width
    offsetb = (offsetx / 100) * w
    xi = int(xi - int(offsetb / 2))
    w = int(w + offsetb)
    xf = xi + w

    # Height
    offseta = (offsety / 100) * h
    yi = int(yi - offseta)
    h = int(h + offseta)
    yf = yi + h
    print(f"Adjusted bounding box: (xi: {xi}, yi: {yi}, xf: {xf}, yf: {yf})")

    # Error
    if xi < 0: xi = 0
    if yi < 0: yi = 0
    if w < 0: w = 0
    if h < 0: h = 0

    # Draw rectangle
    cv2.rectangle(frame, (xi, yi, w, h), color, 2)

    # Crop and save face
    if RegId is not None:
        cut = frame[yi:yf, xi:xf]
        cv2.imwrite(f"{OutFolderPathFaces}/{RegId}.png", cut)
        print(f"Saved cropped face image to {OutFolderPathFaces}/{RegId}.png")


# ___Function SignIn Access Control System
def SignIn_ACSystem():
    """
    Fungsi ini menangani proses masuk dengan menangkap frame dari kamera, mendeteksi landmark wajah menggunakan FaceMesh, dan melakukan pengenalan wajah menggunakan encoding wajah dari gambar yang disimpan.
    Ini mencakup langkah-langkah untuk deteksi wajah, ekstraksi landmark, penghitungan kedipan untuk otentikasi pengguna, dan menampilkan umpan balik UI yang sesuai selama proses masuk.
    """
    global OutFolderPathFaces, cap, lblvideo, screen, screen2, FaceCode, clases, images, screen3, step, blink, count, UserName
    # Check if The Camera Capture is Initialized
    if cap is not None:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # make a Copy of the frame for later use, and
        frameCopy = frame.copy()
        # Resize the frame for processing efficiency
        frameFR = cv2.resize(frameCopy, (0, 0), None, 0.25, 0.25)

        # Convert the frame to RGB color space
        rgb = cv2.cvtColor(frameFR, cv2.COLOR_BGR2RGB)

        # Resize the frame to fit the screen
        frame = imutils.resize(frame, width=1280)

        # Convert frame to RGB for Processing
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Show the original Frame in RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if ret:
            # Process the frame to detect face Landmarks using FaceMesh
            res = FaceMesh.process(frameRGB)

            # Result List to store landmarks positions
            px = []
            py = []
            listf = []

            if res.multi_face_landmarks:
                # Extract Face Mesh
                for wajah in res.multi_face_landmarks:
                    # Draw
                    mpDraw.draw_landmarks(frame, wajah, FacemeshObject.FACEMESH_CONTOURS, ConfigDraw, ConfigDraw)

                    # Extract KeyPoints and their positions
                    for id, point in enumerate(wajah.landmark):
                        # Get image dimensions
                        a, b, c = frame.shape
                        x, y = int(point.x * b), int(point.y * a)
                        px.append(x)
                        py.append(y)
                        listf.append([id, x, y])

                        # If all 468 KeyPoint are captured
                        if len(listf) == 468:
                            # Calculate distances between specific facial points for eye blinking detection
                            x1, y1 = listf[145][1:]  # Right Eye
                            x2, y2 = listf[159][1:]  # Right Eye
                            longitude1 = math.hypot(x2 - x1, y2 - y1)

                            x3, y3 = listf[374][1:]  # Left Eye
                            x4, y4 = listf[386][1:]  # Left Eye
                            longitude2 = math.hypot(x4 - x3, y4 - y3)

                            x5, y5 = listf[139][1:]  # Right temple
                            x6, y6 = listf[368][1:]  # Left temple

                            x7, y7 = listf[70][1:]  # Right Eye Brow
                            x8, y8 = listf[300][1:]  # Left Eye Brow

                            # Detect faces in the frame using the face detection model
                            faces = detector.process(frameRGB)

                            if faces.detections:
                                for face in faces.detections:
                                    # Get Bounding Box and Score for the detected face
                                    score = face.score[0]
                                    bbox = face.location_data.relative_bounding_box

                                    # Check if the detection score is above a Threshold
                                    if score > conThreshold:
                                        # Calculate adjusted bounding box coordinates for cropping
                                        crop_bbox = (bbox.xmin, bbox.ymin, bbox.width, bbox.height)

                                        # Steps to process the detected face
                                        if step == 0:
                                            # Draw a Rectangle around the face and Crop the image
                                            crop_and_save_face(frame, crop_bbox, None, (128, 0, 255))

                                            # Display Instructional Images for the user
                                            # IMG Step0
                                            as0, bs0, c = img_step0.shape
                                            frame[50:50 + as0, 50:50 + bs0] = img_step0

                                            # IMG Step1
                                            as1, bs1, c = img_step1.shape
                                            frame[50:50 + as1, 1030:1030 + bs1] = img_step1

                                            # IMG Step2
                                            as2, bs2, c = img_step2.shape
                                            frame[270:270 + as2, 1030:1030 + bs2] = img_step2

                                            # Check if the Face is Centered properly for processing
                                            if x7 > x5 and x8 < x6:
                                                # Count Blinks for User Authentication
                                                if longitude1 <= 10 and longitude2 <= 10 and not blink:
                                                    count += 1
                                                    blink = True
                                                elif longitude1 > 10 and longitude2 > 10 and blink:
                                                    blink = False

                                                # Display UI for blink counting and verification
                                                ach, bch, c = img_check.shape
                                                frame[150:150 + ach, 1118:1118 + bch] = img_check

                                                cv2.putText(frame, f'Blink: {int(count)}', (1118, 400),
                                                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

                                                # And check if enough blink( Authentication Criteria )
                                                if count >= 3:
                                                    # IMG Check
                                                    ach, bch, c = img_check.shape
                                                    frame[150:150 + ach, 1120:1120 + bch] = img_check

                                                    # Open Eyes
                                                    if longitude1 > 14 and longitude2 > 14:
                                                        # Step 1
                                                        step = 1
                                            else:
                                                count = 0

                                        if step == 1:
                                            # Draw Rectangle and Crop
                                            crop_and_save_face(frame, crop_bbox, None, (0, 255, 0))

                                            # IMG Check Complete
                                            acom, bcom, c = img_comp.shape
                                            frame[50:50 + acom, 50:50 + bcom] = img_comp

                                            # Match the detected face with the stored face encodings
                                            facess = fr.face_locations(frameRGB)
                                            facescod = fr.face_encodings(frameRGB, facess)

                                            # Alternative
                                            for facescod, facessign in zip(facescod, facess):
                                                # Matching Face
                                                Match = fr.compare_faces(FaceCode, facescod)

                                                # Find the most similar face and authenticate the user
                                                same = fr.face_distance(FaceCode, facescod)
                                                min = np.argmin(same)
                                                if Match[min]:
                                                    # Set the authenticated User's Name
                                                    UserName = clases[min].upper()
                                                    # Proceed to User Profile Display
                                                    Profile()
                                                else:
                                                    # Draw a Red Rectangle dab view Alert "User Not Registered"
                                                    crop_and_save_face(frame, crop_bbox, None, (255, 0, 0))
                                                    cv2.putText(frame, "Wajah Tidak Dikenali", (650, 300),
                                                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                                                                cv2.LINE_AA)
                                                    # cv2.putText(frame, "User Not Registered", (50, 50),
                                                    #             cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                                                    break

                                # Handle window closing evenyt for screen3(Sign In Interface)
                                close = screen3.protocol("WM_DELETE_WINDOW", Close_Window)

                            # Draw keypoints for eyebrows
                            cv2.circle(frame, (x7, y7), 2, (255, 0, 0), cv2.FILLED)
                            cv2.circle(frame, (x8, y8), 2, (255, 0, 0), cv2.FILLED)

        # Convert frame to PIL format
        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)

        # Show Video
        lblvideo.configure(image=img)
        lblvideo.image = img
        lblvideo.after(10, SignIn_ACSystem)
    else:
        cap.release()


# ___Function SignUp Access Control System
def SignUp_ACSystem():
    """
    Fungsi ini bertanggung jawab untuk menangani proses Registration pengguna baru dalam Access Control System.
    Proses ini melibatkan beberapa langkah, termasuk Frame Capute dari kamera, mendeteksi wajah pengguna,
    menghitung jumlah kedipan mata sebagai metode verifikasi, dan menyimpan gambar wajah yang telah dipotong.
    """
    global screen2, count, blink, img_comp, step, cap, lblvideo, RegId

    # Camera HP
    # cap = cv2.VideoCapture("https://192.168.1.16:8080/video")

    # Check if the Camera is active
    if cap is not None:
        ret, frame = cap.read()

        #  Make a copy of the frame for later use
        frameSave = frame.copy()

        # Resize
        frame = imutils.resize(frame, width=1280)

        # RGB
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Frame Show
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if ret:
            # Process the frame using FaceMesh to detect facial landmarks
            res = FaceMesh.process(frameRGB)

            # Initialize lists for storing facial landmark positions
            px = []
            py = []
            listf = []

            # If  Faces are detect in the frame
            if res.multi_face_landmarks:
                # Extract Face Mesh
                for wajah in res.multi_face_landmarks:
                    # Draw
                    mpDraw.draw_landmarks(frame, wajah, FacemeshObject.FACEMESH_CONTOURS, ConfigDraw, ConfigDraw)

                    # Extract KeyPoint
                    for id, point in enumerate(wajah.landmark):
                        # Get the position of each landmark relative to image size
                        a, b, c = frame.shape
                        x, y = int(point.x * b), int(point.y * a)
                        px.append(x)
                        py.append(y)
                        listf.append([id, x, y])

                        # Once all 468 KeyPoints are collected
                        if len(listf) == 468:
                            # Right Eye
                            x1, y1 = listf[145][1:]
                            x2, y2 = listf[159][1:]
                            longitude1 = math.hypot(x2 - x1, y2 - y1)

                            # Left Eye
                            x3, y3 = listf[374][1:]
                            x4, y4 = listf[386][1:]
                            longitude2 = math.hypot(x4 - x3, y4 - y3)

                            # Kening Kanan
                            x5, y5 = listf[139][1:]
                            # Kening Kiri
                            x6, y6 = listf[368][1:]

                            # Eye Brow
                            x7, y7 = listf[70][1:]
                            x8, y8 = listf[300][1:]

                            # Face Detect
                            faces = detector.process(frameRGB)

                            if faces.detections:
                                for face in faces.detections:
                                    # Bbox: "ID, BBOX, SCORE"
                                    score = face.score[0]
                                    bbox = face.location_data.relative_bounding_box

                                    # Threshold
                                    if score > conThreshold:
                                        # Adjusted bounding box calculation for cropping
                                        crop_bbox = (bbox.xmin, bbox.ymin, bbox.width, bbox.height)

                                        # Steps
                                        if step == 0:
                                            # Draw Rectangle and Crop
                                            crop_and_save_face(frame, crop_bbox, None, (128, 0, 255))

                                            # IMG Step0
                                            as0, bs0, c = img_step0.shape
                                            frame[50:50 + as0, 50:50 + bs0] = img_step0

                                            # IMG Step1
                                            as1, bs1, c = img_step1.shape
                                            frame[50:50 + as1, 1030:1030 + bs1] = img_step1

                                            # IMG Step2
                                            as2, bs2, c = img_step2.shape
                                            frame[270:270 + as2, 1030:1030 + bs2] = img_step2

                                            # Face Center
                                            if x7 > x5 and x8 < x6:
                                                # Blink Count
                                                if longitude1 <= 10 and longitude2 <= 10 and not blink:
                                                    count += 1
                                                    blink = True
                                                elif longitude1 > 10 and longitude2 > 10 and blink:
                                                    blink = False

                                                # IMG Check
                                                ach, bch, c = img_check.shape
                                                frame[150:150 + ach, 1118:1118 + bch] = img_check

                                                cv2.putText(frame, f'Blink: {int(count)}', (1118, 400),
                                                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

                                                # Counting Blink
                                                if count >= 3:
                                                    # IMG Check
                                                    ach, bch, c = img_check.shape
                                                    frame[150:150 + ach, 1120:1120 + bch] = img_check

                                                    # Open Eyes
                                                    if longitude1 > 14 and longitude2 > 14:
                                                        # Crop and Save
                                                        crop_and_save_face(frameSave, crop_bbox, RegId)

                                                        # Step 1
                                                        step = 1
                                            else:
                                                count = 0

                                        if step == 1:
                                            # Draw Rectangle and Crop
                                            crop_and_save_face(frame, crop_bbox, None, (0, 255, 0))

                                            # IMG Check Complete
                                            acom, bcom, c = img_comp.shape
                                            frame[50:50 + acom, 50:50 + bcom] = img_comp

                                # Close
                                close = screen2.protocol("WM_DELETE_WINDOW", Close_Window)

                            # Circle
                            cv2.circle(frame, (x7, y7), 2, (255, 0, 0), cv2.FILLED)
                            cv2.circle(frame, (x8, y8), 2, (255, 0, 0), cv2.FILLED)

        # Convert Video
        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)

        # Show Video
        lblvideo.configure(image=img)
        lblvideo.image = img
        lblvideo.after(10, SignUp_ACSystem)
    else:
        cap.release()


# __Function SignUp User Interface
def SignUp():
    """
    Fungsi ini digunakan untuk mengatur Antarmuka Pengguna(UI), Pendaftaran(Sign Up), dan melakukan pendaftaran pengguna baru.
    Fungsi ini meliputi langkah-langkah sebagai berikut:
    1. Dimulai dari pengambilan data dari Form Inputan: Nama, ID, dan Status Pengguna
    2. Memeriksa apakah form telah diisi dengan lengkap
    3. Mencetak Apakah ID pengguna sudah terdaftar atau belum
    4. Menyimpan informasi Pengguna baru ke dalam file teks dan menyimpanya dalam folder Users
    5. Menampilkan Antarmuka Kamera untuk pendaftaran Wajah pengguna.
    """
    global RegName, RegId, RegStatus, InputNameReg, InputIdReg, InputStatusReg, cap, lblvideo, screen2
    # Extract: Name = Id = Status
    RegName, RegId, RegStatus = InputNameReg.get(), InputIdReg.get(), InputStatusReg.get()

    # Uncompleted Form
    if len(RegName) == 0 or len(RegId) == 0 or len(RegStatus) == 0:
        # Print Error
        print(" Formulir Uncomplited ")
    else:
        # Check Users
        UserList = os.listdir(PathUsersCheck)
        UserName = [os.path.splitext(lis)[0] for lis in UserList]

        # Check Id
        if RegId in UserName:
            print(" Users Already Registered")
        else:
            # Save Info
            info.append(RegName)
            info.append(RegId)
            info.append(RegStatus)

            # Export Info
            with open(f"{OutFolderPathUsers}/{RegId}.txt", "w") as f:
                f.write(RegName + ",")
                f.write(RegId + ",")
                f.write(RegStatus)

            # Clean
            InputNameReg.delete(0, END)
            InputIdReg.delete(0, END)
            InputStatusReg.delete(0, END)

            # New Screen
            screen2 = Toplevel(screen)
            screen2.title("Sign Up")
            screen2.geometry("1280x720")

            # Label Video
            lblvideo = Label(screen2)
            lblvideo.place(x=0, y=0)

            # VideoCapture
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            cap.set(3, 1280)
            cap.set(4, 720)
            SignUp_ACSystem()


# ___Function SignIn
def SignIn():
    """
    Fungsi ini digunakan untuk mengatur antarmuka pengguna(UI) dan memulai proses verifikasi wajah untuk dapat mengakses System lanjutan.
    Diamana pada fungsi ini terdapat beberapa langka seperti:
    1. Membaca Gambar wajah dari Database yang tersimpan dan
    2. Mengkodekan wajah-wajah tersebut
    3. Membuat Antarmuka Pengguna(UI) untuk verifikasi wajah
    4. Membuka kamera dan memulai proses verifikasi wajah.
    """
    global OutFolderPathFaces, cap, lblvideo, screen3, FaceCode, clases, images
    # Extract: Name, Id, Status
    # DB Faces
    images = []
    clases = []
    listf = os.listdir(OutFolderPathFaces)

    # Reed Face Images
    for lis in listf:
        # Read IMG
        imagedb = cv2.imread(f"{OutFolderPathFaces}/{lis}")
        # Save IMG DB
        images.append(imagedb)
        # Name IMG
        clases.append(os.path.splitext(lis)[0])
    # FaceCode
    FaceCode = Code_Face(images)

    # Window
    screen3 = Toplevel(screen)
    screen3.title("SIGN IN")
    screen3.geometry("1280x720")

    # Label Video
    lblvideo = Label(screen3)
    lblvideo.place(x=0, y=0)

    # VideoCapture
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 1280)
    cap.set(4, 720)
    SignIn_ACSystem()


# ___Path to Access Database
OutFolderPathUsers = "E:/AccessControl System/DataBase/Users"
PathUsersCheck = "E:/AccessControl System/DataBase/Users"
OutFolderPathFaces = "E:/AccessControl System/DataBase/Faces"

# ___Info List
info = []

# Variables
blink = False
count = 0
sample = 0
step = 0

# ___Offset
offsety = 40
offsetx = 20

# ___Threshold
conThreshold = 0.5

# ___Tools Draw
mpDraw = mp.solutions.drawing_utils
ConfigDraw = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

# ___Object Face Mesh
FacemeshObject = mp.solutions.face_mesh
FaceMesh = FacemeshObject.FaceMesh(max_num_faces=1)

# ___Object Face Detect
FaceObject = mp.solutions.face_detection
detector = FaceObject.FaceDetection(min_detection_confidence=0.5, model_selection=1)

# Read IMG
img_check = cv2.imread("E:/AccessControl System/SetUp/Check.png")
img_step0 = cv2.imread("E:/AccessControl System/SetUp/InfoUncomplite.png")
img_step1 = cv2.imread("E:/AccessControl System/SetUp/Stap1.png")
img_step2 = cv2.imread("E:/AccessControl System/SetUp/Stap2.png")
img_comp = cv2.imread("E:/AccessControl System/SetUp/InfoComplite.png")

# ___Main Window
screen = Tk()
screen.title("Access Controll System")
screen.geometry("1280x720")

# __Image
ImageF = PhotoImage(file="E:/AccessControl System/SetUp/Home.png")
background = Label(image=ImageF, text="Home")
background.place(x=0, y=0, relheight=1, relwidth=1)

# __PROFILE
Imagebc = PhotoImage(file="E:/AccessControl System/SetUp/UserInterfarance.png")

# __Input Text
# Name
InputNameReg = Entry(screen)
InputNameReg.place(x=95, y=295)

# Id
InputIdReg = Entry(screen)
InputIdReg.place(x=95, y=390)

# Status
InputStatusReg = Entry(screen)
InputStatusReg.place(x=95, y=480)

# __Button
# SignUp
ImageBR = PhotoImage(file="E:/AccessControl System/SetUp/BTrainData.png")
BtReg = Button(screen, text="Registration", image=ImageBR, height="38", width="230", command=SignUp)
BtReg.place(x=160, y=550)

# SignIn
ImageSI = PhotoImage(file="E:/AccessControl System/SetUp/BUnlock.png")
BtUnlock = Button(screen, text="Unlock", image=ImageSI, height="38", width="170", command=SignIn)
BtUnlock.place(x=880, y=550)

screen.mainloop()
