# WhatIf
Learn

## Pengumpulan Data
1. Lakukan pengumpulan data foto. Data dikumpulkan secara mandiri dengan saran minimal 100 foto per objek dengan berbagai kondisi sudut pengambilan gambar, berbagai kondisi pencahayaan dan background bebas.
2. Untuk foto disarankan untuk dinamai ber urutan seperti img1, img2 dst. Hal itu untuk mempermudah pembacaan manual atau pencarian.
## Instalasi Anaconda dan Label Studio
1. Install Miniconda3 untuk menjadi tempat mendownload dan mengaktifkan Label Studio untuk memisahkan dari file-file seperti py agar tidak terdampak.
2. Lakukan Instalasi pada pc anda.
3. Buka Anaconda Prompt atau miniconda prompt.
4. Tuliskan Prompt dan dijalankan bergantian :
  - conda create -n labelstudio python=3.9 -y
  - conda activate labelstudio
  - Kalau berhasil, prompt berubah jadi: (labelstudio)
  - pip install --upgrade pip
  - pip install label-studio
  - label-studio
5. Secara otomatis web LabelStudio akan terbuka dan disitulah kalian akan melakukan Labeling pada data yang sudah dikumpulkan.
6. Kedepannya untuk membuka Label Studio, kita tinggal menuliskan 2 promp berikut pada anaconda prompt :
  - conda activate labelstudio
  - label-studio
## Labeling Data dengan Label Studio membuat file YOLO
1. Pilih Create
2. Project Name dan Deskripsi silakan diisi sesuai yang anda inginkan.
3. Import semua data.
4. pencet id yang sudah ter import dan nanti akan diarahkan untuk "go to setup" klik saja.
5. Di Labeling Interface, pilih Browse Template.
6. Pilih "Object Detection with Bounding Boxes".
7. Pada bagian "Add label names" silakan tuliskan nama label yang ingin digunakan.
   contoh:
     parfume
     ceres
8. Lalu "Add".
9. pada bagian "Labels" kalian bisa menghapus Label default atau bawaan yang menurut kalian tidak dibutuhkan.
10. setelah selesai mensetting, Pilih "Save". Lalu kita kembali ke Project.
11. Pilih kembali id atau foto yang sudah masuk di dari import tadi.
12. pilihan label dibawah bisa dipilih. contoh ingin melabeli parfume maka pencet label bertuliskan "parfume" dibawah foto lalu tekan dan tarik untuk meng-kotakkan objek pada foto.
13. lalu "Submit".
14. Lakukan kembali labeling pada semua fata yang sudah di import.
15. Jika sudah selesai meLabeli semua data, kembali ke nama project dan pilih "Export".
16. pilih "YOLO".
17. Data Zip silakan di instal pada folder atau tempat penyimpanan yang anda inginkan. Biasanya saya namai "raw_dataset".
18. Hasil Export akan memiliki struktur seperti :
    raw_dataset/
    ├── images/
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   ├── img3.jpg
    │   └── ...
    ├── labels/
    │   ├── img1.txt
    │   ├── img2.txt
    │   ├── img3.txt
    │   └── ...
    ├── classes
    └── notes.json

## Split Data Set
1. Buat Folder baru untuk menjadi wadah hasil pembagian data untuk train 80% dan val 20%.
2. Bisa dinamai "dataset" foldernya.
   └── dataset/
    ├── images/train
    ├── images/val
    ├── labels/train
    └── labels/val
3. 
## Training menggunakan google colab.
