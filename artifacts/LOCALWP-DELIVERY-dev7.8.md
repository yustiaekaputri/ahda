# AHDA Discovery Engine 0.1.0-dev.7.8 — LocalWP

Pembaruan ini menambahkan pemeriksaan arsip satu sekolah: kandidat vs nilai
profil saat ini, relasi sumber terdaftar, dan draf artikel dari beberapa dokumen
dengan kutipan serta daftar informasi yang masih perlu bukti. Semuanya baca-saja.
Belum mengambil sumber internet, menyimpan kandidat arsip, atau menerbitkan profil.

## Unduh

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/archive-review-dev7.8/artifacts
2. Klik `AHDA_Discovery_Engine_Archive_Review_0.1.0-dev.7.8.zip`.
3. Klik **Download raw file**/ikon unduh. Jangan Code > Download ZIP.
4. Simpan ZIP; untuk upload WordPress tidak perlu diekstrak.

SHA-256: `68337d17a981c51982ed17250fb5176576e8f969f9b2e58c424f22063870a845`.

## Memasang (opsional, hanya ahda.local)

1. Di Local pilih **ahda > Start site**, buat backup situs lokal Anda.
2. Klik **WP Admin**, login admin.
3. **Plugins > Add New Plugin > Upload Plugin > Choose File**.
4. Pilih ZIP7.8 > **Install Now** > **Replace current with uploaded** jika ditanya.
5. Pastikan hanya companion AHDA Discovery Engine diganti; Directory0.8.9 tetap.
6. Aktifkan companion bila diperlukan. Jangan mengaktifkan write/network/publisher atau mengubah wp-config.php.

Tidak ada migrasi/role/tabel baru. Jangan gunakan WinSCP untuk memasang ke
ahda.sch.id; produksi tidak masuk cakupan. Tidak perlu mengulang semua demo lama.

## Coba fitur baru

Di aplikasi Local > ahda > **Open Site Shell**:

```bat
wp --user="admin" ade pilot inspect --demo --npsn=20210711 --dry-run
```

NPSN itu anggota200 pilihan, dipakai untuk **contoh sintetis**. Isi contoh bukan
fakta sekolah tersebut. Dengan DOM dan identitas sesuai, hasil berisi3kandidat,
6bukti dari2dokumen,3bagian artikel dan9topik belum dinilai. Tidak ada informasi
biaya/fasilitas/prestasi yang dikarang untuk melengkapi draf. Tanpa DOM, HTML
contoh ditahan dan artikel tidak dibuat. Konflik dokumen juga menahan artikel.

Periksa mode `READ_ONLY_ARCHIVE_REVIEW_PLAN`, database_writes0,
network_requests0, storage_enabled false, approval_enabled false,
publication_enabled false. `article_draft` berisi HTML yang sudah di-escape,
kutipan URL/waktu/hash raw dan usulan metadata pencarian yang belum diterapkan.

Tidak adanya binding sumber pada demo adalah hasil normal:
`missing_operator_binding`. Fitur tidak menebak bahwa domain sama berarti resmi.
Relasi pending/verified di database juga tidak menjadi persetujuan publikasi.
Jangan ubah flag fixture pada demo untuk memaksanya menjadi fakta atau disimpan.

Untuk dokumen nyata, format arsip/bindings/perintah lengkap ada dalam ZIP:
`docs/ARCHIVE_REVIEW.md` dan `docs/LOCAL_ARCHIVE_WORKER.md`. Perintah inspect
mem-parse ulang raw, tidak menerima checkpoint sebagai bukti. Hash rencana bukan
token approval/store. Jangan mengirim output inspect/work ke store lama.
Simpan sumber privat/report di luar webroot dan jangan unggah ke GitHub.

## Bukti pengujian

- 22suite/1371pemeriksaan lulus masing-masing PHP8.2 dan8.4 dengan DOM.
- 1304pemeriksaan tanpaDOM; ekstraksi HTML tidak dijalankan pada konfigurasi itu.
- 76filePHP lint;84hash baseline serta6file tes asli utuh.
- 164pemeriksaan MySQL8.4.13 pada database sementara sintetis, dengan adapter WordPress/wpdb stub; seluruh container uji milik sesi ini sudah dihapus.
- Query baru benar-benar dijalankan di MySQL; hash9tabel sintetis tetap sama setelah pemeriksaan. Ini bukan pengujian25tabel pengguna Anda.
- Fitur inspect baru belum diuji pada WordPress nyata/LocalWP Anda. Bukti39tes WordPress7.6 tetap berstatus versi sebelumnya.

Log/diff: `docs/qa/dev7.8` dalam ZIP; run MySQL final di subfolder native-final.
Belum ada200profil faktual lengkap atau jaminan peringkat Google/rekomendasiAI.

Rollback cukup ganti folder companion dengan ZIP7.7 dari branch
`delivery/local-worker-dev7.7`; tidak menghapus tabel atau mengimpor sekolah ulang.
Checkpoint/report milik operator tetap disimpan. Langkah berikutnya adalah
storage raw-pending yang atomik dengan bukti dan persetujuan, kemudian worker
transaksional/review positif/publisher lokal. Akses sumber nyata masih memerlukan
kebijakan jaringan yang mengizinkan host dan persetujuan sumber yang sesuai.
