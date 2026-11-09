# dev.7.6 — Bukti integrasi WordPress7.1.4 nyata

39pemeriksaan admin WordPress7.1.4 lulus bersama Directory0.8.9 dan Discovery7.6,
PHP8.2/MySQL8.4. Yang digunakan adalah Core login/cookie/role/nonce/wpdb/admin-post
sesungguhnya pada situs cloud sintetis. Termasuk CSRF, nonce lintas sesi/aksi,
editor403, anonim400/login, status+audit+receipt, replay, konflik versi409, IDOR,
XSS, redirect, tampilan desktop/mobile dan hash25tabel AHDA lama sintetis utuh.

Situs memakai bootstrap uji sendiri dengan shim wp-load dan alias home/REST
loopback; tidak membaca/membuat/mengubah wp-config. WordPress resmi dipin pada
commit db96f5eaa77a8d3e8eec8923a518fa2326f0d46a. Tidak ada stub untuk auth/nonce/
wpdb yang diuji. Tidak ada request eksternal final, email diblokir. Seluruh DB,
container, situs dan server sementara dihapus; sumber resmi/tool cache disimpan.

## Anda tidak perlu mengulang demo

Runtime sama dengan7.5 selain metadata versi; pembaruan ini menambahkan harness,
bukti pengujian dan checkpoint. Jika7.5 sudah terpasang, tidak wajib memasang ulang
sekarang. Fitur tulis tetapOFF, panel default tetap baca-saja. Tidak ada sumber
nyata atau profil yang diperkaya. Jangan mengaktifkan constant/role/opsi, mengubah
wp-config, menjalankan store, atau mengunggah ke ahda.sch.id.

Jika ingin meninjau paket lengkap terbaru: backup LocalWP dahulu, lalu WP Admin >
Plugins > Add New Plugin > Upload Plugin > pilih ZIP7.6 > Install Now > Replace
current with uploaded untuk Discovery saja. Jangan mengganti Directory, uninstall,
menghapus tabel, reimport, rebuild atau memasang skema ulang. Pastikan versi7.6
aktif. Menu AHDA Discovery > Kandidat (baca-saja) tetap dapat kosong karena demo
tidak disimpan. Tidak ada perintah CLI baru atau penulisan yang diminta.

## Batas bukti dan langkah berikutnya

Ini situs cloud sintetis, belum pengujian konfigurasi LocalWP/Windows Anda,
plugin tambahan, tema publik, SEO frontend atau beban VPS. Gambar admin aktif di
folder QA berasal dari opt-in uji sintetis; bukan fitur aktif di situs Anda.
M2CLI/store WordPress penuh, masa kedaluwarsa nonce, gangguan TCP nyata/deadlock/
load belum dibuktikan oleh39kasus ini.20suite offline/1121checks lulus masing-
masing PHP8.2/8.4 dengan DOM;1068tanpa DOM (HTML tidak dijalankan),70filePHP lint.
84hash baseline dan6suite asli utuh. Folder QA menyimpan kegagalan isolasi awal
beserta perbaikan originREST dan runPASS akhir, tidak mengubahFAIL menjadiPASS.

Masih perlu sumber/izin dan arsip evidence, worker resumable, bidang tambahan,
review persetujuan, reopen kompensasi dan publisher/rollback. Sumber katalog masih
belum diizinkan kebijakan jaringan cloud; sisa riset18/20 tidak dipakai. Tidak ada
janji ranking Google atau rekomendasi AI. Penulisan nyata LocalWP tetap memerlukan
rencana kandidat konkret+backup+persetujuan operator tersendiri. Produksi dilarang.

Lihat docs/WORDPRESS_INTEGRATION.md, docs/PROGRESS.md, tests/wordpress/README.md dan
docs/qa/dev7.6 di ZIP. WordPress/Chromium tidak perlu dipasang di VPS; harness hanya
untuk lingkungan uji tersendiri yang diizinkan. Rollback file ke7.5 tanpa migrasi;
pertahankan semua tabel/audit/receipt/data.

SHA-256 ZIP: 51fc43f4a9fb9ea13a8d103f96c4e9973b105a2246f815c5cf0a571bd6c62e13
