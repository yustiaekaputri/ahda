# Perbaikan WP-CLI dev.7.1.1

Paket ini memperbaiki error invalid synopsis/unknown --dry-run pada extract dan
stage. Ini kesalahan deklarasi pada paket sebelumnya; perintah Anda sudah benar.
Tidak ada perubahan skema, data Directory, crawler atau penerbitan otomatis.

1. Di Local, pilih situs AHDA dan pastikan berjalan. Backup situs/database lokal.
2. Klik WP Admin, login admin. Masuk Plugins > Add New Plugin > Upload Plugin.
3. Pilih AHDA_Discovery_Engine_M2_Pending_0.1.0-dev.7.1.1.zip > Install Now.
4. Pilih Replace current with uploaded untuk AHDA Discovery Engine saja.
   Jangan mengganti/menghapus AHDA School Directory dan jangan uninstall Discovery.
5. Pastikan versi Discovery 0.1.0-dev.7.1.1. Jika nonaktif, Activate.
6. Kembali ke Local > AHDA > Open site shell, jalankan:

```sh
wp --user="admin" ade pilot extract --demo --dry-run
```

Hasil yang diharapkan: mode FIXTURE_ONLY_READ_ONLY, tiga kandidat sintetis,
network_requests 0 dan database_writes 0. Kirim keluaran untuk verifikasi LocalWP.
Tidak perlu mengulang impor, pemasangan skema atau membangun ulang data sekolah.
Jangan jalankan store atau unggah ke ahda.sch.id pada tahap ini.

16 suite offline/745 checks lulus pada masing-masing PHP8.2/8.4;55 file PHP lint.
Regresi baru menggunakan parser/dispatcher resmi WP-CLI v2.12.0, dengan WordPress
& database simulasi. Ini belum bukti native LocalWP/MySQL. File MIT upstream dan
hash tersedia dalam tests/vendor/wp-cli-2.12.0; tidak dimuat runtime plugin.
Semua84 baseline file dan6 suite regresi asli tidak berubah. Log dan checkpoint
ada di docs/qa/dev7.1.1 dan docs/PROGRESS.md dalam ZIP.

Rollback file plugin ke paket lama tidak membutuhkan migrasi, tetapi error flag
akan kembali. Pertahankan seluruh tabel/data. Native writer, sumber nyata,
worker ekstraksi, dashboard review dan publisher belum selesai/tervalidasi.

SHA-256 ZIP: 05ea32032f5c347a0619c2dd245cba79e83bc4f95605572fa1d121d72b6eca1a
