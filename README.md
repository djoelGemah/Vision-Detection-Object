# Membuat Pendeteksi Objek memanfaatkan Miniconda3, LabelStudio, GoogleCollab, VisualStudioCode 

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
    - raw_dataset/
      - ├── images/
        - │   ├── img1.jpg
        - │   ├── img2.jpg
        - │   ├── img3.jpg
        - │   └── ...
      - ├── labels/
        - │   ├── img1.txt
        - │   ├── img2.txt
        - │   ├── img3.txt
        - │   └── ...
      - ├── classes
      - └── notes.json

## Split Data Set
1. Extract raw_dataset untuk di split ke folder baru.
2. Buat Folder baru untuk menjadi wadah hasil pembagian data untuk train 80% dan val 20%.
3. Bisa dinamai "dataset" foldernya.
   - └── dataset/
      - ├── images/train
      - ├── images/val
      - ├── labels/train
      - └── labels/val
5. Buka VS code.
6. Buka folder yang menyimpan keseluruhan folder file project agar folder raw_dataset dan lainnya juga terhubung.
7. Buat file python split dataset dengan cara file --> new text file --> set sebagai type python --> isi baris kode bisa diambil pada file github dengan nama split_dataset.py
8. Jalankan kode split_dataset itu dan secara otomatis membagi data 80% sesuai yang dibutuhkan dari raw_dataset ke dataset.
9. Dalam folder dataset akan terdapat file data.yaml
10. JIKA data.yaml tidak ada, anda bisa menuliskan manual dengan note dan berikut isinya :
   
- path: dataset

- train: images/train
- val: images/val

- names:
-   0: ceres
-   1: parfume


7. Untuk bagian "names :" Bisa diliat dari isi folder raw_dataset di file classes.txt. -- >Urutannya dan nama-namanya memang berasal dari LabelStudio yang kita buat dan nantinya untuk .yaml di folder "dataset" kita tambahkan no urut "0,1,2, dst" seperti di contoh step no 6 yang bisa digunakan sebagai patokan contoh benar.   Lalu Save as dengan file name "data.yaml" jangan lupakan tulis .yaml --> Save as type diganti "All files(*.*)" lalu save.
8. Ambil kode python dengan nama "split_dataset.py" untuk membantu melakukan split data. Run kode itu. Untuk python saya sepenuhnya menggunakan VisualCode Studio dan langsung membuka folder projeknya.
9. Compress dataset menjadi Zip untuk dimasukkan kedalam gooogle colab nantinya.
10. Setelah itu dataset siap untuk di train.
   
## Training menggunakan google colab.
1. Buat Note Baru pada google Colab.
2. Tekan "runtime".
3. Tekan "Ubah jenis runtime".
4. Pada bagian "Akselerator hardware" pilih "GPU T4".
5. Simpan.
6. Masukkan folder dataset.zip kedalam file google colab.
7. jalankan beberapa kode berikut ini bergantian di google colab. Berikut urutan file file kode colabnya:
   - colab 1
   - colab 2
   - colab 3
   - colab 4
   - Simpan pada folder yang sama diluar folder dataset atau bisa dibilang folder yang menyimpan keseluruhan projek.

## Menjalankan Objek Deteksi
1. Buka VS code kembali.
2. Buka folder yang menyimpan keseluruhan projek di VScode.
3. Buat File python atau kode python baru dengan cara --> File --> New Text file --> buat tipe python.
4. Untuk isinya bisa dicopy dari file di github yang bernama "Kode Objek Detektion Simulasi Toko.py"
5. Untuk bagian Path Konfigurasi di kodenya itu saya menyesuaikan set up saya dan bisa kalian sesuaikan. untuk folder keseluruhan folder file project disitu saya namai deteksi. lalu ada folder tambahan yang saya siapkan untuk menyimpan perhitungan dan foto pembeli serta orangnya di folder "rekap_penjualan" yang saya siapkan di data "D:\deteksi" lokasinya dan penjualan didalam note penjualan.txt.
