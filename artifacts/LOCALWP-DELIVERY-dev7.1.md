# dev.7.1 — M2 pending store, development review only

Kode stage/store/receipt ditambahkan. Native MySQL/LocalWP write belum diuji.
JANGAN JALANKAN store sekarang. Tidak ada source/doc nyata berizin yang sudah
tersedia untuk pilot, dan izin uji MySQL disposable masih menunggu jawaban.
Tidak perlu memasang ulang plugin hanya untuk mengatasi akses katalog cloud.

15 suite offline lulus PHP8.2/8.4,695 checks masing-masing;45 PHP files lint.
Scope/role/backup/confirmation/token gates, transaksi, dedupe, receipt, review/
version race dan rollback diuji pada fake DB, bukan bukti engine MySQL nyata.
Snapshot pengamatan native user sebelumnya tetap dicatat untuk6.1/6.2 saja.
SHA-256 ZIP: 44966b3f84d18b8120ae2786d58e59ab8e5205c9ba02747fc442eaed241c05f9.

Isi ZIP: source/tests, docs/M2_STORE.md, M2_PREVIEW.md, PROGRESS.md dan rencana uji
MySQL sementara. Daftar200, skema1 dan Directory lama tetap. Source/profile tidak
diubah; kandidat baru tetapnew/not_ready, score0 dan approved_valueNULL. Data demo
secara eksplisit ditolak oleh writer. Tidak ada crawler, approval atau publisher.

Untuk review/uji preview saja setelah backup dan persetujuan pemasangan lokal:
Plugins > Add New > Upload > pilihZIP7.1 > Install > Replace Discovery saja.
Buka Open site shell AHDA, preview demo lama tetap tersedia:
```sh
wp --user="admin" ade pilot extract --demo --dry-run
```
Ini sintetis dan tidak menyimpan data. Jangan mengganti fixture_only agar demo
bisa disimpan. Stage membutuhkan dokumen nyata dan source relation terdaftar;
parameter/concrete impact ada di docs/M2_STORE.md. Jangan mengeksekusi write
hanya berdasarkan berhasilnya preview. LocalWP writes memerlukan persetujuan
tersendiri setelah backup, native tests dan rencana konkret diperiksa.

Uji MySQL cloud yang diminta: database baru sementara, synthetic only,1CPU/1GiB,
portloopback, tanpa wp-config/data pengguna/LocalWP/produksi. Izin ini tidak
mencakup penulisan LocalWP. Belum ada container atau DB uji dibuat.

Cloud tetap memblokir dua domain katalog. Sisa riset18/20; izin operator sebelumnya
masih berlaku dan tidak diminta ulang. M2worker/HTMLCSV/M3review/M4publish belum
selesai. Tidak untuk ahda.sch.id. Rollback file ke7.0 tidak perlu migrasi; jangan
hapus receipt/data. Sesudahcommit tidak ada delete/revoke otomatis pada modul ini.
