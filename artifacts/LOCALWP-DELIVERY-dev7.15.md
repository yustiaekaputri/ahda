# AHDA Discovery Engine 0.1.0-dev.7.15 — review admin dan paket lebih ringan

Persetujuan satu klaim kini tersedia melalui dashboard dengan dua tahap eksplisit:
pemeriksaan kelayakan, lalu konfirmasi catatan/backup. Persetujuan tidak menerbitkan
profil. Semua fitur penulisan tetap OFF secara bawaan; tidak perlu mengaktifkannya
atau membuat data demo pada situs Anda sekarang.

## Unduh dari GitHub

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/admin-review-dev7.15/artifacts
2. Klik `AHDA_Discovery_Engine_Admin_Review_0.1.0-dev.7.15.zip`.
3. Klik **Download raw file** / ikon unduh, bukan **Code > Download ZIP**.
4. Simpan ZIP. Tidak perlu diekstrak untuk upload melalui WordPress.

SHA-256: `c29cfeebd1f6b98ef8dd5e486a11d8518445e04befa3df4d378a18468fef82f8`.
Ukuran ZIP 1484741 byte, turun 77.6% dari dev.7.14. Ukuran berkas setelah
ekstraksi turun 66.7%. Penghematan berasal dari QA historis yang
tidak lagi disalin ke instalasi; kode runtime, semua tes dan fixture tetap ada.
Bukti historis tetap tersimpan di workspace pengembangan dan riwayat GitHub.
Ini penghematan transfer/disk, bukan janji kecepatan frontend/VPS.

## Memasang opsional, hanya ahda.local

1. Di Local, pilih **ahda > Start site**. Backup situs dan folder plugin dahulu.
2. Buka **WP Admin**, login admin.
3. **Plugins > Add New Plugin > Upload Plugin > Choose File**.
4. Pilih ZIP dev.7.15 > **Install Now > Replace current with uploaded**, bila diminta.
5. Ganti AHDA Discovery Engine saja; AHDA School Directory 0.8.9 tetap.
6. Biarkan penulisan/crawler/publisher OFF. Jangan mengubah wp-config.php.

Upload Replace mengganti folder plugin, sehingga QA lama tidak ikut menumpuk.
Upload WinSCP secara merge dapat meninggalkan QA lama dan tidak memberikan
penghematan disk yang sama. Jangan menghapus file pengguna secara manual atau
mengunggah ke ahda.sch.id. Tidak ada migrasi/reimport/penghapusan profil/badge.
Rollback memakai backup lokal dev.7.14 tanpa menghapus tabel/data/event/audit.
Delivery aktif hanya ZIP terbaru dan panduan ini. Riwayat Git tidak dihapus;
pembersihan daftar aktif tidak menghilangkan ukuran riwayat lama.

## Alur dashboard setelah data/izin yang sah tersedia

Saat ini tidak perlu mencoba writer: demo lama tidak disimpan dan sumber sekolah
nyata belum tersedia. Jangan memasukkan data contoh untuk mengisi dashboard.
Jika sudah ada record sah dan persetujuan pengaktifan lokal yang spesifik:

1. **AHDA Discovery > Kandidat**, pilih sekolah dan buka kandidat.
2. Pilih evidence berbasis raw dan ID deklarasi sumber untuk kandidat/bukti sama.
3. Klik **Periksa kelayakan persetujuan**. Langkah ini baca-saja.
4. Halaman konfirmasi menampilkan nilai lama, usulan, versi, bukti, deklarasi,
   masa berlaku, reviewer serta catatan/referensi identitas dan izin.
5. Isi catatan, cek backup dan persetujuan satu klaim, lalu konfirmasi.
6. Status tersimpan menjadi approved, tetapi publish_status tetap not_ready.
   Riwayat positif menampilkan reviewer, waktu, versi, deklarasi dan catatan.

Gate yang digunakan tetap ADE_LOCAL_POSITIVE_REVIEW_ENABLED. Bila operator pernah
mengaktifkan flag service dev.7.14, handler web baru ini juga akan aktif; tindakan
baru tetap memerlukan capability, nonce form dan persetujuan eksplisit. Paket ini
tidak menambah/mengaktifkan flag di konfigurasi Anda.

Normal GET tidak memuat raw. Preview dan apply masing-masing membaca raw sekali;
apply wajib memeriksa ulang sumber/izin/versi/hash dalam transaksi. Controller
menghindari preflight skema duplikat, sedangkan pemeriksaan layanan tetap wajib.
Nonce tidak valid ditolak sebelum pemeriksaan mahal. Tidak ada cache izin lintas
request, crawl otomatis, bulk/edit approval atau penerbitan. Referensi deklarasi
hanya teks operator; tidak diakses atau disahkan sistem. Pencabutan izin menahan
penggunaan selanjutnya walaupun keputusan lama tetap tercatat sebagai sejarah.

## Bukti tes dan batasnya

- 26 suite / 1.599 pemeriksaan masing-masing PHP 8.2 dan 8.4 dengan DOM lulus.
- 1.531 tanpa DOM; ekstraksi HTML tidak dijalankan pada konfigurasi itu.
- 91 file PHP lint; 84 hash baseline dan 6 regresi asli tetap utuh.
- 151 pemeriksaan layanan WordPress/MySQL sintetis + 89 pemeriksaan browser lulus.
- Form nyata diuji untuk editor/anonim, nonce/session, input array/field asing,
  HTTP method, versi lama, pencabutan setelah preview, XSS, checkbox, safe redirect,
  audit, retry, default OFF, mobile dan hitungan raw-read/write.
- Semua25 tabel lama sintetis tetap utuh; seluruh resource uji milik sesi dibersihkan.
- Satu percobaan gagal pada login admin kedua karena timeout30s, tanpa login POST
  atau pesan login_error. Bukti FAIL disimpan. Harness menunggu autofocus awal
  WordPress sebelum mengisi kredensial; pengujian selanjutnya lulus. Dugaan race
  autofocus belum membuktikan penyebab kegagalan atau perbaikan login situs Anda.

Log, screenshot, diff dan angka query ada dalam ZIP `docs/qa/dev7.15`.
Pengukuran HTTP sintetis dimulai setelah bootstrap WordPress; bukan benchmark
VPS, concurrent traffic, sumber nyata atau full official WP-CLI runner.
Tidak mengakses database LocalWP pengguna, wp-config, sumber eksternal atau produksi.

Checkpoint `docs/PROGRESS.md`. Pengayaan fakta nyata masih0/200; fondasi ~55% tetap
perkiraan kasar. Berikutnya worker ekstraksi yang tahan putus/resume, publisher
lokal dengan rollback dan sumber sah untuk profil faktual. Artikel lengkap/ranking
Google/rekomendasi AI belum terbukti dan tidak dijanjikan.
