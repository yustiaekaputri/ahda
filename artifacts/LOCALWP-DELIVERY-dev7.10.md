# AHDA Discovery Engine 0.1.0-dev.7.10 — LocalWP

Tahap baru: raw receipt tersimpan dapat diproses menjadi evidence dan kandidat
pending dalam satu transaksi. Seluruh sumber/dokumen tetap punya referensi hash
raw, kandidat yang sudah direview dipertahankan, retry tidak membuat duplikat.
Modul tetap **default OFF**; tidak ada penulisan pada database Anda sesi ini.

## Unduh

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/archive-candidates-dev7.10/artifacts
2. Klik `AHDA_Discovery_Engine_Archive_Candidates_0.1.0-dev.7.10.zip`.
3. Klik **Download raw file**/ikon unduh, bukan Code > Download ZIP.
4. Simpan ZIP. Untuk upload WordPress tidak perlu diekstrak.

SHA-256: `576276dc9715be4aa5c139bd59c5e8e3b400ec6382df7a44001d8d94d8a4bf96`.

## Memasang (opsional, situs lokal saja)

Tidak perlu mengulang demo inspect/batch yang sebelumnya sudah berhasil. Paket
boleh disimpan dahulu sambil pengembangan berikutnya; tidak perlu segera dipasang.

1. Di Local pilih **ahda > Start site**, buat backup situs lokal Anda.
2. Klik **WP Admin**, login sebagai admin.
3. **Plugins > Add New Plugin > Upload Plugin > Choose File**.
4. Pilih ZIP7.10 > **Install Now** > **Replace current with uploaded** jika diminta.
5. Pastikan hanya AHDA Discovery Engine yang diganti; Directory0.8.9 tetap.
6. Aktifkan companion bila diperlukan; jangan mengaktifkan flag write/network/publisher atau mengubah wp-config.php.

Tidak ada schema migration/tabel/role/opsi baru, tidak mengimpor atau menghapus
profil. Jangan memasang melalui WinSCP ke ahda.sch.id. Produksi tetap di luar scope.

## Fungsi baru

Command memakai underscore: archive_stage, archive_store, archive_receipt.
Stage hanya membaca rencana dari raw receipt yang sah dan NPSN yang cocok. Store
memerlukan flag kode opt-in terpisah, capability lokal, token segar, backup YES
dan konfirmasi STORE_ARCHIVE_CANDIDATES. Tidak ada instruksi write untuk dijalankan
pada data Anda dalam panduan ini; rencana sumber nyata/backup/izin DB belum ada.

Contoh dampak dua dokumen/3klaim:3candidate+6evidence+6link+1receipt=16row di tabel
Discovery, rawreceipt tetap. Jika kandidat pending sudah ada, dipakai ulang dengan
kenaikan versi; kandidat reviewed/approved/published tidak diubah atau ditambah
bukti di belakang reviewer. Tidak membuat confidence/verified badge atau approval.

Dashboard kandidat dapat menampilkan nomor rawreceipt, format dan SHA dokumen.
Ada penjelasan bahwa binding raw belum diperiksa ulang pada halaman tersebut;
referensi hash bukan verifikasi sumber. Tidak menampilkan rawHTML atau menambah
form persetujuan. Daftar kandidat tetap bisa kosong karena demo Anda tidak disimpan.
Jangan mengubah flag fixture demo agar bisa disimpan.

Lihat docs/ARCHIVE_CANDIDATES.md dalam ZIP untuk kontrak, batas, rollback dan gate.
Tidak ada persetujuan positif, publisher atau perubahan profil yang sudah tayang.

## Bukti pengujian

- 24suite/1504pemeriksaan lulus masing-masing PHP8.2 dan8.4 dengan DOM.
- 1436tanpaDOM; ekstraksi HTML tidak dijalankan pada konfigurasi itu.
- 81filePHP lint,84hash baseline dan6file regresi asli utuh.
- 282pemeriksaan actualMySQL8.4.13 dengan WP/wpdb adapter stub dan data sintetis; container milik sesi sudah dihapus.
- 26pemeriksaan Chromium pada tampilan PHP/WordPress+DB fixture: mobile/desktop, XSS, hash/reference, tanpa request eksternal. Server uji dihentikan.
- Runtime manual Store7.9 tidak berubah byte-for-byte; tes lama tetap lulus.

Writer baru belum diuji pada WordPress nyata/LocalWP Anda atau sumber faktual.
Bukti39tes WordPress7.6 dan hasil inspect7.8 Anda tetap scope sebelumnya.
Data lama Anda tidak diubah, source sekolah tidak diambil. Progres/log/diff ada
pada docs/PROGRESS.md dan docs/qa/dev7.10 dalam ZIP.

Rollback menggunakan backup folder plugin/situs LocalWP yang dibuat sebelum
pembaruan. Paket versi lama dan branch pengiriman lama sudah dibersihkan dari
daftar aktif GitHub; tautan branch lama dalam catatan historis ZIP mungkin tidak
berlaku lagi. Riwayat commit tetap ada dan cadangan lengkap disimpan lokal pada
lingkungan pengembangan. Jangan menghapus tabel atau mengimpor sekolah ulang.
Jika kelak sudah ada write nyata, tinjau kompatibilitas sebelum downgrade.
Retensi/privacy/enkripsi/kuota-total arsip masih menjadi gate sebelum data nyata.

Tahap berikut: integrasi WordPress nyata, validasi binding penuh dalam review,
source permission/identity dan approval positif, durable worker lalu publisher
lokal dengan rollback. Belum ada200profil faktual lengkap atau janji ranking/AI.
## Kebijakan unduhan setelah perapian

Daftar aktif hanya berisi ZIP7.10 dan panduan ini. Dokumen kontrak proyek di main
tetap dipertahankan. ZIP/plugin dan SHA-256 tidak berubah; perapian ini hanya
menghapus paket/panduan yang sudah digantikan serta branch pengiriman lama.
Versi lama tetap ada dalam riwayat Git, sehingga ukuran GitHub belum tentu
langsung turun. Tidak ada force rewrite riwayat atau perubahan database/situs.
