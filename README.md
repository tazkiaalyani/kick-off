https://tazkia-nur41-kickoff.pbp.cs.ui.ac.id/Jelaskan 

TUGAS 3
 Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 ---> Data delivery itu penting biar data bisa dikirim dan diterima antar bagian sistem atau bahkan antar aplikasi. Kalo nggak ada data delivery, frontend sama backend nggak bisa saling komunikasi. Contohnya, pas frontend butuh data produk, backend harus ngasih data dengan format yang bisa dipahami. Jadi data delivery ini kayak jembatan komunikasi.

 Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
 ---> Menurutku JSON lebih nyaman untuk digunakan, karena cenderung lebih simple, lebih ringan, mudah dibaca, dan langsung nyambung dengan JavaScript atau bahasa lain. XML sebenarnya juga bisa, tapi formatnya lebih rumit, banyak tag, sehingga lebih boros. JSON lebih populer karena lebih praktis dan cocok untuk web modern.

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
---> is_valid() digunakan untuk meriksa data dari form sudah sesuai aturan atau belum. Misalnya field wajib isi, tipe datanya angka, panjang minimal, dan lain-lain. Kalau datanya tidak valid, otomatis akan dikasih tau error. Ini penting agar data yang salah atau aneh tidak masuk ke database.

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
---> csrf_token itu untuk menjaga form dari serangan CSRF (Cross-Site Request Forgery). Kalau token ini tidak ada, penyerang bisa memanfaatkan celah untuk membuat user tanpa sadar melakukan aksi berbahaya, seperti submit form palsu, transaksi, atau menghapus data. Dengan csrf_token, request bisa divalidasi secara menyeluruh dari aplikasi kita, bukan dari luar.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
--->
1. Buat folder `templates` di root project `kick off`, lalu tambahkan file `base.html` sebagai kerangka dasar halaman web.
2. Tambahkan `BASE_DIR / 'templates'` ke bagian `TEMPLATES` di `settings.py` agar `base.html` bisa dikenali oleh Django.
3. Ubah `main.html` supaya menggunakan `base.html` dengan memanfaatkan `{% extends %}` dan `{% block content %}`.
4. Tambahkan file `forms.py` di folder `main` yang berisi form untuk input data produk baru.
5. Perbarui `views.py` dengan menambahkan fungsi `create_product` untuk menyimpan data produk dari form serta menyesuaikan fungsi lain yang diperlukan.
6. Import fungsi baru ke `urls.py` lalu tambahkan route pada `urlpatterns`.
7. Sesuaikan kembali `main.html` untuk menampilkan daftar produk beserta tombol Add Product.
8. Buat file `create_product.html` untuk form input produk dengan `{% csrf_token %}`, dan `product_detail.html` untuk menampilkan detail produk tertentu.
9. Tambahkan alamat ke `CSRF_TRUSTED_ORIGINS` di `settings.py`, kemudian jalankan server untuk memastikan konfigurasi berjalan.
10. Import `HttpResponse` dan `Serializer` di `views.py` untuk menyiapkan response data dalam format XML maupun JSON.
11. Tambahkan fungsi `show_xml` di `views.py`, kemudian daftarkan endpoint-nya di `urls.py` dan uji melalui browser.
12. Buat fungsi `show_json` dengan langkah yang sama lalu cek kembali hasilnya.
13. Tambahkan fungsi `show_xml_by_id` dan `show_json_by_id` dengan `try-except` untuk handle data produk berdasarkan ID, lalu daftarkan ke `urls.py`.
14. Gunakan Postman untuk mengetes semua endpoint (GET XML, JSON, dan versi by ID).
15. Lakukan push project ke GitHub dan PWS dengan perintah `git add .`, `git commit`, `git push origin master`, lalu `git push pws master`.

Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
---> Asdosnya sangat helpful 10/10
<img width="1346" height="874" alt="Screenshot 2025-09-17 082700" src="https://github.com/user-attachments/assets/e15bd0ac-3243-4bd1-b5c9-52cf05351141" />
<img width="1351" height="869" alt="Screenshot 2025-09-17 082645" src="https://github.com/user-attachments/assets/dba32ac1-d3ba-4439-a820-40de2e119b0e" />
<img width="1349" height="879" alt="Screenshot 2025-09-17 082557" src="https://github.com/user-attachments/assets/0856ef64-da69-47d8-abcb-2977e3c2e8d2" />
<img width="1352" height="876" alt="Screenshot 2025-09-17 082536" src="https://github.com/user-attachments/assets/8a413427-3158-4a64-b27b-391691b3b60a" />


TUGAS 2
bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Buat folder baru kick off sebagai direktori project
2. Mengaktifkan virtual environment dengan python -m venv env dan env\Scripts\activate
3. Buat requirements.txt lalu install dengan pip install -r requirements.txt
4. Inisialisasi proyek Django
5. Buat file .env dan .env.prod untuk simpan variabel penting
6. sesuaikan ALLOWED_HOSTS untuk development
7. Konfigurasi database
8. Lakukan migrasi untuk setup database
9. Tes server lokal dengan python manage.py runserver
10. Buat repository Git, .gitignore, dan push ke Github dengan branch master
11. Setup project baru di PWS, isi environment dari .env.prod
12. Tambahkan domain PWS ke ALLOWED_HOSTS
13. Hapus file sensitif dari Git dan push ulang
14. Buat app baru bernama main
15. Daftarkan main di INSTALLED_APPS
16. Buat file main.html dan isi dengan data diri
17. Tampilkan main.html lewat fungsi view di views.py
18. Buat model di models.py dengan atribut wajib dan tambahan
19. Lakukan migrasi ulang agar model masuk ke database
20. Buat file urls.py di main lalu atur routing view
21. Sambungkan routing main ke urls.py proyek utama
22. Commit dan push semua perubahan ke Github dan PWS

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img width="280" height="204" alt="Diagram" src="https://github.com/user-attachments/assets/74328fb9-55c6-4fc0-9976-9aa483501fcf" />

Saat user mengirim request lewat browser, Django akan mengecek urls.py untuk mencari URL yang sesuai dan menentukan fungsi di views.py mana yang harus dijalankan. Di dalam views.py, jika perlu data, maka akan ambil dari models.py yang berinteraksi langsung dengan database. Setelah datanya siap, view akan mengirim data tersebut ke template HTML untuk dirender jadi tampilan. Hasil akhirnya dikirim kembali ke browser sebagai respon dan ditampilkan ke user.

Jelaskan peran settings.py dalam proyek Django!
settings.py adalah file konfigurasi utama dalam proyek Django. File ini berfungsi untuk mengatur bagaimana proyek Django berjalan baik saat development maupun production. Django gak akan tahu bagaimana menjalankan proyek tanpa settings.py, karena merupakan pusat kontrol semua konfigurasi penting di Django.

Bagaimana cara kerja migrasi database di Django?
Migrasi di Django itu proses nyesuain model di models.py sama database. Setelah buat atau ubah model, kita jalanin makemigrations untuk bikin file migrasi yang berisi perubahan. Lalu, dengan migrate, perubahan itu diterapin ke database, misalnya bikin tabel atau kolom baru. Jadi, migrasi bikin kita nggak perlu otak atikdatabase manual.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django jadi pilihan awal buat belajar karena dia framework yang lengkap dan terstruktur. Semua kebutuhan dasar kayak database, autentikasi, dan tampilan sudah disediain, jadi kita bisa fokus buat belajar konsep pemrograman web tanpa harus bikin semuanya dari nol. Selain itu, Django pakai Python yang gampang dipahami dan banyak dipakai di dunia nyata, jadi skillnya juga berguna banget. Struktur kodenya juga ngajarin kita cara bikin aplikasi yang terorganisir dan scalable. Makanya, banyak yang mulai belajar web development pake Django.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
10/10
