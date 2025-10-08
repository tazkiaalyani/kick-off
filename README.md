https://tazkia-nur41-kickoff.pbp.cs.ui.ac.id/

TUGAS 6
Apa perbedaan antara synchronous request dan asynchronous request?
---> Synchronous request adalah permintaan ke server yang mengharuskan browser menunggu hingga server merespon sebelum pengguna dapat berinteraksi kembali dengan halaman. Sedangkan asynchronous request, seperti AJAX, memungkinkan browser tetap responsif karena request dikirim dan diproses di latar belakang tanpa harus me-refresh seluruh halaman.

Bagaimana AJAX bekerja di Django (alur request–response)?
---> AJAX mengirim permintaan ke server melalui JavaScript tanpa mereload halaman. Django menerima permintaan tersebut melalui views, memproses data, dan mengembalikan response, biasanya berupa JSON atau HTML partial. JavaScript kemudian menggunakan response tersebut untuk memperbarui konten halaman secara langsung. Alurnya adalah: aksi pengguna -> AJAX request -> Django view -> response -> update halaman via JavaScript.

Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
---> AJAX memungkinkan halaman tidak reload penuh sehingga proses lebih cepat dan interaksi pengguna lebih lancar. Penggunaan bandwidth lebih efisien karena hanya data yang dibutuhkan yang dikirim. AJAX juga mendukung fitur interaktif seperti live search, filter dinamis, atau update konten secara real-time.

Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
---> Keamanan AJAX dapat dijaga dengan selalu menyertakan CSRF token pada setiap request POST. Validasi data harus dilakukan di server side. Gunakan HTTPS untuk mengamankan data sensitif dan hindari pengiriman password dalam bentuk plain text. Penanganan error juga harus aman agar tidak membuka celah bagi eksploitasi.

Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
---> Penggunaan AJAX membuat interaksi pengguna lebih cepat dan responsif karena halaman tidak perlu reload penuh. Pengguna dapat tetap berinteraksi dengan halaman sementara data sedang diproses, sehingga pengalaman menggunakan website menjadi lebih nyaman, modern, dan efisien.

TUGAS 5
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
---> Kalau satu elemen HTML punya beberapa CSS selector, browser akan memilih style berdasarkan tingkat spesifisitasnya. Selector elemen seperti div atau p prioritasnya paling rendah. Selector class seperti .container lebih spesifik, jadi akan menimpa element selector. Selector ID seperti #header lebih tinggi lagi, sehingga menimpa class dan element selector. Kalau style ditulis langsung di elemen dengan style="", itu lebih tinggi prioritasnya dibanding CSS di file. Terakhir, penggunaan !important akan menimpa semua aturan lain. Jadi, semakin spesifik selector, semakin besar kemungkinan browser menerapkannya ke elemen.

Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
---> Responsive design itu penting banget supaya tampilan web tidak berantakan di semua layar, mau HP, tablet, atau komputer. Kalau tidak responsive, layout bisa pecah, teks terlalu kecil atau terlalu besar, dan pengguna harus scroll horizontal yang bikin rumit. Contohnya Google dan Tokopedia udah responsive, jadi otomatis menyesuaikan layar. Tapi situs lama seperti sekolah atau instansi kadang belum responsive, jadi ketika dibuka di HP tampilannya acak-acakan dan susah dipake. Responsive bikin web nyaman untuk semua orang.

Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
---> Margin itu jarak di luar elemen, agar elemen tidak nempel dengan yang lain. Border itu garis pinggir elemen, bisa diberi warna dan tebal. Padding itu jarak di dalam elemen, antara isi elemen dan border. Cara membuatnya di CSS mudah, misal:
div {
  margin: 10px;
  border: 2px solid black;
  padding: 5px;
}
Jadi isi elemen tidak nempel ke border, dan elemen tidak nempel ke elemen lain.

Jelaskan konsep flex box dan grid layout beserta kegunaannya!
---> Flexbox itu untuk ngatur elemen dalam satu arah saja, bisa baris atau kolom. Enaknya, mudah untuk ngatur posisi dan jarak antar elemen. Grid berbeda, dia layout dua dimensi, baris sama kolom sekaligus. Cocok untuk layout kompleks seperti dashboard atau galeri. Intinya, Flexbox untuk yang simpel, Grid untuk yang lebih rumit tapi lebih rapi.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
---> 
1. Aktifkan environment virtual seperti biasa, lalu di views.py tambahkan import redirect, get_object_or_404, dan messages supaya bisa handle edit dan delete product dengan feedback ke user.
2. Modifikasi fungsi create_product di views.py supaya form product menggunakan Tailwind classes agar tampilan form lebih rapi dan modern.
3. Buat fungsi edit_product di views.py untuk nge-handle update product. Gunakan get_object_or_404 untuk ambil product sesuai id, lakukan validasi form, lalu simpan perubahan.
4. Buat fungsi delete_product di views.py untuk menghapus product berdasarkan id. Tambahkan messages supaya user dapat notifikasi sukses atau gagal.
5. Di template main.html, tampilkan semua product dalam card layout pakai Tailwind. Setiap card menampilkan nama product, harga, dan author. Tambahkan tombol Edit dan Delete di tiap card.
6. Import semua fungsi baru (edit_product, delete_product) ke urls.py, lalu tambahkan path baru, misal:

path('product/edit/<int:id>/', edit_product, name='edit_product')

path('product/delete/<int:id>/', delete_product, name='delete_product')
7. Buat navbar responsive di base.html pakai Tailwind. Untuk versi mobile, tampilkan hamburger menu yang bisa diklik; untuk desktop tampil horizontal. Tambahkan link Home, Create Product, Login, dan Logout sesuai status login user.
8. Pastikan semua tampilan pakai Tailwind classes konsisten, termasuk spacing, typography, dan warna card supaya layout rapi dan modern.
9. Cek semua halaman (main.html, create_product.html, edit_product.html) dan pastikan layout responsive di HP, tablet, dan desktop.
10. Test semua fungsi: create product, edit, delete, navigasi navbar, dan tampilannya. Pastikan tidak ada error dan semua sesuai requirement assignment.
11. Setelah semuanya berfungsi dengan baik, lakukan git add ., git commit -m "", dan git push ke repository GitHub.

TUGAS 4
Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
---> AuthenticationForm adalah form bawaan Django untuk proses login. Isinya berupa field username dan password, lalu otomatis cek apakah input valid sesuai database user. Kelebihannya: gampang digunakan, sudah ada validasi built-in, dan aman karena sesuai standar Django. 
Kekurangannya: sedikit kaku, default-nya hanya support username & password, jadi kalau mau custom login (misalnya pakai email) harus extend atau bikin form sendiri.

Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
---> Autentikasi itu untuk cek identitas user, apakah ini beneran akun user. Otorisasi itu untuk cek hak akses user, misalnya apakah user boleh akses halaman admin atau edit produk orang lain?. Di Django, autentikasi di-handle melalui sistem User, login, dan session. Sedangkan otorisasi diatur melalui permission, decorator (@login_required, @permission_required), atau atribut user.

Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
---> Session menyimpan data di server, browser user hanya pegang ID session. Aman karena user gak bisa lihat isinya, tapi lebih berat ke server. Cookies menyimpan data langsung di browser, lebih ringan untuk server tapi rawan karena bisa dimodifikasi atau dicuri. Jadi session lebih aman, cookies lebih ringan tapi beresiko.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
---> Cookies tidak sepenuhnya aman secara default. Ada resiko seperti XSS atau session hijacking yang bisa nyolong cookie user. Django dapat mengatasi dengan membuat cookie session HttpOnly (ga bisa diakses JS), bisa di-set Secure (cuma lewat HTTPS), ada CSRF token buat cegah serangan CSRF, dan session Django juga terenkripsi. Jadi lebih aman, tapi tetap harus hati-hati pas develop.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---> 
1. Aktifkan environment virtual seperti biasa, lalu di views.py tambahin import UserCreationForm dan messages.
2. Buat fungsi register di views.py untuk nge-handle form pendaftaran dan nyimpen akun baru.
3. Siapin file register.html di folder templates supaya form bisa ditampilkan.
4. Import fungsi register tadi ke urls.py, lalu tambahin path ke urlpatterns.
5. Untuk login, tambahin import authenticate, login, dan AuthenticationForm di views.py. Setelah itu bikin fungsi login_user.
6. Buat file login.html untuk nampilin form login.
7. Tambahin fungsi login tadi ke urls.py dengan path barunya.
8. Tambahkan import logout di views.py, bikin fungsi logout_user, terus di main.html kasih tombol logout.
9. Import logout_user ke urls.py dan tambahkan path barunya.
10. Import login_required lalu tempelin decorator @login_required di fungsi view yang perlu proteksi login.
11. Tambahin import HttpResponseRedirect, reverse, dan datetime. Edit fungsi login biar nyimpen cookie last_login, masukin juga ke context show_main, dan pas logout cookie itu dihapus.
12. Supaya produk terhubung dengan user, import User di models.py, tambahin field user di model Product, lalu makemigrations & migrate. Setelah itu modifikasi create_product, show_main, tambahin tombol filter My/All di main.html, serta tampilkan author produk di detail.


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
