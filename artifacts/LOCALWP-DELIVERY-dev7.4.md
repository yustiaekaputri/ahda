# dev.7.4 — Pemeriksaan kandidat di WordPress (baca-saja)

CSV dan HTML demo Anda sudah lulus di LocalWP, masing-masing3kandidat tanpa
request jaringan/perubahan DB. Tidak perlu mengulang perintah demo sebelumnya.
Versi ini menambahkan panel untuk melihat kandidat tersimpan, bukan menyimpan
contoh atau mengaktifkan approval/publish. Belum ada profil nyata diperkaya.

## Memasang Discovery saja di LocalWP

1. Backup situs/database lokal. Buka Local > AHDA > Start Site > WP Admin.
2. Login admin, pilih Plugins > Add New Plugin > Upload Plugin > Choose File.
3. Pilih AHDA_Discovery_Engine_M3_Inspector_0.1.0-dev.7.4.zip > Install Now.
4. Pilih Replace current with uploaded untuk AHDA Discovery Engine saja.
5. Pastikan Discovery aktif/versi0.1.0-dev.7.4. Jangan mengganti Directory,
   uninstall plugin, menghapus tabel, reimport, rebuild atau memasang skema ulang.

## Membuka panel

1. Di sidebar WP Admin, klik AHDA Discovery > Kandidat (baca-saja).
2. Pada NPSN sekolah pilot, pilih sekolah, misalnya20268071 (SMP, KAB.TASIKMALAYA).
3. Biarkan Status=Semua lalu klik Tampilkan.
4. Jika tertulis Belum ada kandidat tersimpan, itu kondisi yang diharapkan:
   demo/preview CLI tidak menyimpan kandidat. Jangan menjalankan store untuk
   mengisi daftar dengan contoh. Tidak perlu mengubah opsi/flag atau database.
5. Jika kelak sudah ada kandidat nyata yang disimpan secara berizin, klik Lihat
   nilai dan evidence. Panel membandingkan nilai terverifikasi saat ini, nilai
   saat usulan dibuat, usulan, dan nilai disetujui tersimpan. Kutipan/sumber dan
   konflik ditampilkan.20kandidat/evidence per halaman, lanjut lewat tautan.

Tidak ada tombol approve/edit/reject/defer/publish. Status approved yang mungkin
terbaca adalah data tersimpan, bukan perintah menerbitkan. Panel tidak memeriksa
izin/otoritas sumber secara independen. Sebab itu source/evidence tetap perlu
pemeriksaan manusia. URL bercredential/token/IP tidak ditampilkan, source links
lain tidak diakses otomatis. Alasan kesiapan hanya untuk evidence yang dimuat,
bukan sertifikasi penuh. Jangan klik sumber yang belum Anda izinkan aksesnya.

Panel dibatasi reviewer di ahda.local dan preflight aman. Jika menu tidak muncul,
atau403/M3_PREFLIGHT_BLOCKED, kirim pesan/tangkapan layar; jangan menambah role,
mengaktifkan flag review atau mengubah database diam-diam. UI belum diverifikasi
native di LocalWP Anda. Tidak ada operasi di ahda.sch.id.

## Bukti pengujian dan batas

19suite/1010checks offline lulus masing-masing PHP8.2/8.4 dengan DOM;957tanpa DOM
(HTML extraction tidak dijalankan di mode itu).65file PHP lint tiap versi.
110checks native MySQL8.4.13/PHP8.2 lulus, WordPress/wpdb/preflight masih stub.
Container/storage uji sintetis sudah dihapus.16checks Chromium desktop/mobile
lulus pada actual PHP view dengan backend/WordPress stub dan CSS minimal, bukan
halaman LocalWP sesungguhnya. Screenshot sintetis dalam docs/qa/dev7.4. Server
fixture sudah dihentikan; browser tidak mengakses domain eksternal.84baseline
hashes dan6suite regresi asli tidak berubah. Checkpoint di docs/PROGRESS.md.

M3 baru panel baca-saja, belum keputusan/audit, verifikasi izin sumber, worker
resumable atau publisher/rollback. Sumber nyata masih diblokir kebijakan jaringan
cloud, sisa izin riset18/20 tidak dipakai. Tidak ada perubahan canonical/schema/
SEO frontend atau janji ranking/rekomendasi AI. Semua penulisan nyata LocalWP
memerlukan persetujuan konkret terpisah setelah backup; izin uji cloud bukan izin
write LocalWP. Rollback file Discovery ke7.3 tanpa migrasi; pertahankan semua data.

SHA-256 ZIP: 82981947956b7de8a6669c31ff9b3946cc3996d43787e18db25d199f704ce9d0
