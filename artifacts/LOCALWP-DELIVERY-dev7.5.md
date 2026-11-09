# dev.7.5 — Fondasi keputusan tolak/tunda, tetap NONAKTIF

Engine tolak/tunda dibuat dengan capability, nonce WordPress, rencana terikat
reviewer/versi, pemeriksaan konflik, transaksi, audit append-only dan receipt
pengulangan aman. Hanya status kandidat Discovery berubah; profil, evidence,
source, nilai usulan dan data lama tidak ditulis. Approve/edit/publish/reopen
belum tersedia. Ditolak bersifat final pada modul ini; tunda tidak otomatis
melanjutkan pengayaan. Jangan mengubah status/versi atau menghapus audit manual.

## Kondisi paket standar

Fitur tulis OFF, handler tidak terdaftar, tidak ada formulir penyimpanan.
Panel tetap baca-saja dan menampilkan riwayat keputusan negatif bila ada.
Tidak ada yang perlu Anda aktifkan atau ulangi dari demo CLI sebelumnya.
Jangan mengubah wp-config, role/opsi atau memasang helper pengaktif sekarang.
Belum ada penulisan ke LocalWP Anda, sumber nyata atau profil yang diperkaya.

Jika ingin meninjau paket terbaru setelah backup lokal: WP Admin > Plugins >
Add New Plugin > Upload Plugin > pilih ZIP7.5 > Install Now > Replace current
with uploaded untuk Discovery saja. Pastikan versi0.1.0-dev.7.5 aktif. Jangan
mengganti Directory, uninstall, menghapus tabel, reimport, rebuild atau memasang
skema ulang. Buka AHDA Discovery > Kandidat (baca-saja). Daftar/riwayat kosong
normal karena demo tidak disimpan. Tidak perlu memasang ulang hanya untuk demo.

## Bukti tes

20suite/1121checks offline per PHP8.2/8.4 dengan DOM;1068tanpa DOM (HTML extraction
tidak dijalankan di mode itu).68file PHP lint tiap versi.146checks MySQL8.4.13
sungguhan lulus dengan WordPress/wpdb/nonce stub, bukan full LocalWP PASS.
Dua container/storage sintetis telah dihapus.21checks Chromium actual PHP view
under WP/backend/CSS stubs lulus; screenshot mode opt-in adalah sintetis, bukan
fitur aktif di situs Anda. Server fixture dihentikan, tanpa request eksternal.
84hash baseline dan6suite regresi asli tidak berubah. Bukti di docs/qa/dev7.5;
checkpoint di docs/PROGRESS.md, kontrak di docs/M3_NEGATIVE_REVIEW.md.

Tes mencakup rollback status+audit+receipt ketika gagal, replay tanpa audit ganda,
commit nyata dengan simulasi konfirmasi hilang, nonce/actor/versi/aksi, controller
GET405/invalid403/stale409, mutex M2/M3/NOWAIT, dan writer tidak menambahkan bukti
di belakang keputusan tunda/tolak. Nonce/session/routing WordPress sebenarnya
belum diuji. Snapshot/review tidak berarti fakta terverifikasi atau diterbitkan.

## Berikutnya dan batas keselamatan

Perlu kontrak sumber/izin dan arsip bukti, review persetujuan, reopen kompensasi,
worker resumable, publisher/rollback, serta pengujian WordPress penuh. Operasi
write LocalWP hanya setelah rencana kandidat konkret+backup+persetujuan terpisah.
Izin MySQL sintetis cloud bukan izin write LocalWP. Respons transaksi gagal bisa
berarti commit sudah tersimpan; periksa status/riwayat sebelum mengulang. Rollback
transaksi berbeda dari membatalkan keputusan sesudah commit (belum ada).

Sumber katalog masih diblokir kebijakan cloud, sisa riset18/20 tidak dipakai.
Tidak ada perubahan SEO frontend atau janji ranking Google/rekomendasi AI.
Jangan unggah ke ahda.sch.id. Rollback file ke7.4 tanpa migrasi; pertahankan
semua audit/receipt/data, gunakan7.5 untuk membaca riwayat kembali.

SHA-256 ZIP: 72394e9eebc21fe7ca3a276c9cae8986edda8beae4707719404e69b97a42ce1b
