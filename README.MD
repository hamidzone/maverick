Soal Nomor 1
Untuk mengimplementasikan checklist di atas, berikut langkah-langkah yang saya lakukan:

1. **Mempersiapkan Lingkungan Pengembangan**:
   - Pertama-tama, saya membuat virtual environment menggunakan `python -m venv env` untuk memastikan semua dependensi terisolasi.
   - Setelah itu, saya menginstal Django dengan menjalankan `pip install django`.
   - Saya memulai proyek baru dengan perintah `django-admin startproject pws_project`.
   - Kemudian, saya membuat aplikasi dengan `python manage.py startapp pws_app`, yang akan menjadi inti dari aplikasi ini.

2. **Membangun Model**:
   - Saya mendefinisikan model di `models.py`, yang merupakan representasi dari data yang akan digunakan dalam aplikasi ini. Saya menggunakan ORM Django untuk menghubungkan model dengan database.
   - Setelah model selesai, saya menjalankan `python manage.py makemigrations` dan `python manage.py migrate` untuk membuat dan menerapkan skema database.

3. **Mengatur URL dan Views**:
   - Saya menambahkan URL patterns di `urls.py`, yang berfungsi menghubungkan URL yang diminta oleh pengguna dengan view yang sesuai.
   - Di `views.py`, saya menulis logika bisnis yang mengambil data dari model dan mengirimkannya ke template HTML.
   - Saya juga memastikan bahwa setiap view terkait dengan template yang tepat di folder `templates`.

4. **Membuat dan Menampilkan Template**:
   - Saya membuat berkas HTML di folder `templates` dan menggunakan Django Template Language (DTL) untuk menampilkan data yang dikirimkan dari views.
   - Dengan ini, saya bisa memastikan bahwa antarmuka pengguna menampilkan informasi yang relevan dengan baik.

Soal Nomor 2
erikut adalah bagan sederhana yang menggambarkan bagaimana request dari client diproses oleh aplikasi Django dan bagaimana komponennya saling terkait:

```mermaid
graph TD;
    A[Client Request] --> B[urls.py]
    B --> C[views.py]
    C --> D[models.py]
    C --> E[HTML Template]
    D --> C
    E --> A[Response to Client]

    click A href "https://tautan-aplikasi-anda.com" "Client"
    click B href "https://docs.djangoproject.com/en/4.1/topics/http/urls/" "Django URLs"
    click C href "https://docs.djangoproject.com/en/4.1/topics/http/views/" "Django Views"
    click D href "https://docs.djangoproject.com/en/4.1/topics/db/models/" "Django Models"
    click E href "https://docs.djangoproject.com/en/4.1/topics/templates/" "Django Templates"

Soal Nomor 3- Penjelasan Fungsi-Fungsi Git dalam Perangkat Lunak
a. Terdapat versi kontrol yang berperan sebagai melacak tiap perubahan sehingga bisa melihat timeline pengembangan antara versi terbaru dan versi sebelumnya.

b. Mampu meningkatkan kolaborasi dengan teman atau tim dengan cara memisahkan pekerjaan dalam cabang (branch) dan menggabungkan (merge) tanpa merusak kode.

c. Git berperan sebagai penyimpanan terpusat sehingga bisa akses dan bagi kode dengan mudah karena sifatnya yang open source.

4. Mengapa Django cocok sebagai Framework Pembelajaran?
Django cocok sebagai framework pembelajaran karena memiliki struktur yang jelas yaitu mengikuti pola MVC (Model-View Controller) yang membantu kita memahami komponen applikasi web yang saling berinteraksi

5. Django disebut sebagai ORM (Object Relational Mapping) karena bisa berinteraksi dengan database menggunakan Python tanpa menulis query SQL sehingga dijamin efisien.