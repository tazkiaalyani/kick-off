https://tazkia-nur41-kickoff.pbp.cs.ui.ac.id/Jelaskan 
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
