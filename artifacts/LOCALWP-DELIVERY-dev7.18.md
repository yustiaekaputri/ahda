# AHDA Discovery Engine dev7.18 — inventaris arsip baca-saja

Melanjutkan dev7.17, menambah pemantauan ukuran arsip per halaman tanpa membaca
isi dokumen, menghapus arsip, mengambil URL, atau mengubah database. Writer dan
publisher tetap OFF. Dashboard, worker dan publisher/undo7.17 tetap tersedia.

## Unduh dan pasang opsional — hanya ahda.local

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/raw-inventory-dev7.18/artifacts
2. Klik `AHDA_Discovery_Engine_Raw_Inventory_0.1.0-dev.7.18.zip`.
3. Klik **Download raw file** atau ikon unduh, bukan Code > Download ZIP.
4. Local > ahda > Start site; backup situs dan plugin lokal dahulu.
5. WP Admin > Plugins > Add New Plugin > Upload Plugin > Choose File.
6. Pilih ZIP > Install Now > Replace current with uploaded, bila diminta.
7. Ganti Discovery Engine saja; Directory0.8.9 tetap. Jangan edit wp-config.php.

SHA-256: `85ffbb83f7f95de367961932a491c5bf0c3f1e8685dd160409393298010d5be0`. Ukuran 1476697 byte. Root ZIP `ahda-discovery-engine`.
Tidak ada migrasi, reimport, rebuild atau penghapusan profil. Jangan pasang di
ahda.sch.id sekarang. Rollback file ke backup7.17 tanpa menghapus tabel/audit;
7.17 masih memiliki undo publisher. Paket memuat QA terbaru; bukti lama di riwayat.

## Pemeriksaan opsional yang aman

Buka Local > ahda > Open site shell, jalankan:

```
wp --user="admin" ade pilot raw_inventory --limit=25 --after=0 --dry-run
```

Ini SELECT-only dan tanpa jaringan, bukan instruksi menjalankan writer. Bila
has_more=true, ganti --after=0 dengan angka cursor hasil untuk halaman berikutnya.
Bila entries kosong, belum ada receipt raw tersimpan; itu bukan error dan jangan
mengisi dengan data buatan. Tidak perlu mengulang demo atau menyalin ID fixture.

Hasil page_bytes hanya menjumlahkan payload+summary pada baris yang ditampilkan,
bukan total database/index/backup atau kuota. age_days adalah umur receipt, bukan
umur fakta sekolah maupun izin menghapus. Metadata terlalu besar/tanggal masa depan
ditandai; isi dokumen tidak divalidasi lewat daftar ini. Limit maksimal100.
Pagination bukan snapshot konsisten; jangan mengklaim total global dari halaman
saat writer bersamaan. Batas hasil bukan batas keras IO/rows examined MySQL.

**Kuota total, enkripsi, dan retensi/penghapusan belum diterapkan.** Jangan aktifkan
bulk capture nyata. Rancang aturan dependensi evidence/audit dan persetujuan
operator sebelum menghapus raw. Detail: docs/RAW_INVENTORY.md dalam ZIP.

## Bukti

28 suite offline/1.680 pemeriksaan masing-masing PHP8.2+8.4DOM;1.612 tanpaDOM
(ekstraksi HTML tidak dijalankan),97PHP lint,84hash baseline/6regresi asli utuh.
WordPress7.1.4/Directory0.8.9/MySQL8.4 sintetis:212layanan sebelumnya+inventaris,
69publisher/undo,99browser/HTML. Proyeksi byte/cursor dibandingkanSQLnative; seluruh
hash Discovery dan25tabel lama sebelum/sesudah inventaris sama. Semua resource tes
milik sesi dibersihkan. Bukan LocalWP pengguna,200profil faktual atau benchmarkVPS.
Log/diff docs/qa/dev7.18; checkpoint docs/PROGRESS.md.

Pengayaan fakta nyata masih0/200. Akses katalog masih terblokir pengaturan cloud.
Tambahkan dua domain berikut pada pengaturan lingkungan cloud > jaringan/domain
yang diizinkan, dengan mempertahankan domain/preset lama:

- referensi.data.kemendikdasmen.go.id
- referensi.data.kemdikbud.go.id

Tidak ada konfigurasi jaringan disimpan/dipublikasikan oleh sesi ini. Izin terbatas
sebelumnya masih berlaku:18request tersisa/10sekolah pertama, satu proses,5detik/host,
robots/ToS. Tidak ada request katalog baru. Detail docs/NETWORK_RESEARCH_PENDING.md.
Artikel lengkap, rankingGoogle dan rekomendasiAI belum terbukti/tidak dijanjikan.
