# AHDA Discovery Engine 0.1.0-dev.7.9 — LocalWP

Hasil inspect7.8 yang Anda kirim sesuai harapan:2dokumen,3kandidat,6bukti,
3bagian draf dan9topik yang belum dinilai, tanpa error/konflik/write/network.
Penanda fixture/stale/missingbinding normal untuk demo. **Tidak perlu mengulangnya.**

7.9 menambahkan modul arsip raw-pending, **default OFF**, dengan konfirmasi
backup/privasi/operator, transaksi, batas1MiB dan perlindungan duplikat. Ini belum
menyimpan evidence/candidate arsip, menyetujui fakta atau menerbitkan profil.
Jangan mengaktifkan write atau menyimpan demo sebagai data nyata.

## Unduh dari GitHub

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/raw-vault-dev7.9/artifacts
2. Klik `AHDA_Discovery_Engine_Raw_Vault_0.1.0-dev.7.9.zip`.
3. Klik **Download raw file**/ikon unduh; bukan Code > Download ZIP.
4. Simpan ZIP di komputer. Untuk upload lewat WordPress tidak perlu diekstrak.

SHA-256 ZIP: `5ac87f5709305bda0cf9d544e0d23a571a7ecdcfd16f46332bfeee839bb3cd7e`.

## Memasang (opsional, hanya situs lokal)

Pembaruan ini boleh disimpan dulu sambil pengembangan berikutnya; tidak perlu
segera dipasang atau mengulang seluruh tes lama.

1. Local > **ahda > Start site**, buat backup situs lokal Anda terlebih dahulu.
2. **WP Admin**, login admin.
3. **Plugins > Add New Plugin > Upload Plugin > Choose File**.
4. Pilih ZIP7.9 > **Install Now** > **Replace current with uploaded** jika diminta.
5. Hanya ganti AHDA Discovery Engine. Directory0.8.9 tetap.
6. Aktifkan companion jika diperlukan. Jangan mengaktifkan flag write/network/publisher atau mengubah wp-config.php.

Folder root `ahda-discovery-engine/`; tidak ada migrasi/tabel/role baru, data lama
tidak diimpor atau dihapus. Jangan unggah ke ahda.sch.id melalui WinSCP.

## Apa yang sudah berfungsi dan belum

Raw archive storage memakai satu row di tabel Discovery jobs untuk satu sekolah
terpilih (<=3dokumen). Raw199sekolah lain tidak ikut. Menyimpan raw plus jejak
kutipan/hash/snapshot/actor; receipt baca hanya metadata, tidak HTML mentah.
Tidak ada raw viewer/web endpoint atau network fetch.

Command baru menggunakan underscore: vault_stage (read-only), vault_store
(write defaultOFF), vault_receipt (historical metadata). Stage perlu arsip nyata
dan bindings source sah, bukan demo. Fixture/stale/mismatch/conflict/unbound
selalu ditolak. Tidak ada perintah mutasi untuk dijalankan pada situs Anda dalam
panduan ini. Izin database nyata dan rencana dokumen/backup tetap diperlukan.

Lihat docs/RAW_ARCHIVE_VAULT.md dalam ZIP untuk kontrak, scope, pengujian, batas
privasi/retensi dan rollback. Privacy-reviewed merupakan pernyataan operator,
bukan pemindai otomatis. Raw belum dienkripsi aplikasi; kuota total/retensi/
export/delete belum dibuat, sehingga modul tetap OFF sampai kebijakan siap.

## Bukti tes

- 23suite/1416pemeriksaan masing-masing PHP8.2 dan8.4 dengan DOM.
- 1348tanpaDOM; ekstraksi HTML tidak dijalankan pada konfigurasi itu.
- 78filePHP lint;84hash baseline dan6file tes asli utuh.
- 195pemeriksaan MySQL8.4.13 pada data sintetis sementara dengan adapter WP/wpdb stub. Container milik sesi sudah dihapus.
- Diuji insert atomic, rollback, same-school lock, NOWAIT source lock, token stale, dedupe, commit-ackloss recovery, corruption detection dan8tabel non-jobs sintetis tetap utuh.

Writer baru belum diuji di WordPress nyata/LocalWP Anda. Laporan inspect7.8 Anda
membuktikan demo baca-saja, bukan penulisan atau verifikasi sumber faktual.
Tidak ada perubahan database pengguna/produksi atau source fetch baru dari cloud.
Log/diff/checkpoint: docs/qa/dev7.9 dan docs/PROGRESS.md dalam ZIP.

Rollback kode: ganti folder companion dengan ZIP7.8 dari branch
`delivery/archive-review-dev7.8`. Tidak menghapus tabel/import ulang. Jika kelak
ada rawreceipt yang disimpan dengan izin, rollback kode tidak menghapus arsipnya.

Tahap berikutnya menghubungkan receipt arsip ke evidence/candidate secara atomik,
kemudian worker/review positif/publisher lokal berizin. Belum ada200artikel faktual
lengkap atau janji ranking Google/rekomendasiAI. Akses katalog resmi masih dibatasi
kebijakan jaringan cloud; tidak diulang atau dilewati.
