# dev.7.2 — Draf artikel berbukti dan pemeriksaan kualitas

## Yang sudah dibuat

Perintah article menghasilkan draf pratinjau dengan paragraf program, kurikulum,
jam layanan dan kutipan sumber. Checklist12topik menunjukkan9topik yang belum
bisa dinilai adapter (penerimaan, biaya, fasilitas, ekstrakurikuler, akreditasi,
sejarah, kontak, aksesibilitas, prestasi). Ini bukan klaim bahwa data lama kosong.
Belum ada profil sekolah nyata yang diperkaya. Semua klaim baru belum diverifikasi,
menunggu review. Judul/deskripsi SEO hanya usulan; canonical dan schema School
Directory lama tidak diubah atau digandakan. Tidak menjanjikan peringkat Google
atau rekomendasi AI. Baca docs/CONTENT_QUALITY.md di dalam ZIP.

## Cara memasang di LocalWP

1. Buka Local, pilih AHDA, Start Site. Buat backup situs/database lokal dahulu.
2. Klik WP Admin dan login admin.
3. Pilih Plugins > Add New Plugin > Upload Plugin > Choose File.
4. Pilih AHDA_Discovery_Engine_M2_Article_0.1.0-dev.7.2.zip > Install Now.
5. Pilih Replace current with uploaded untuk AHDA Discovery Engine saja.
   Jangan mengganti Directory, uninstall Discovery atau menghapus tabel.
6. Pastikan Discovery aktif dan versi0.1.0-dev.7.2.
7. Kembali ke Local > AHDA > Open site shell. Jalankan:

```sh
wp --user="admin" ade pilot article --demo --dry-run
```

Hasil: mode EDITORIAL_DRAFT_READ_ONLY, fixture_only true,3sections/3sources,
9information_gaps, topics_approved0, network_requests0, database_writes0,
publication_enabled false. article_html berisi label CONTOH SINTETIS — BUKAN
FAKTA SEKOLAH. Kirim keluaran untuk memeriksa kompatibilitas LocalWP. Ini bukan
artikel siap tayang; jangan salin contoh ke halaman publik. Tidak perlu reimport,
rebuild indeks, reinstall schema atau mengulang demo extract yang sudah lulus.
Tidak ada admin viewer baru; hasil masih JSON di shell.

## Pengujian dan batasan

17suite offline/822checks lulus pada masing-masing PHP8.2 dan8.4;58file PHP lint.
Parser/dispatcher resmi WP-CLI diuji under stubs.84file baseline dan6suite regresi
asli tidak berubah. Dengan izin eksplisit operator,70checks MySQL8.4.13 sungguhan
lulus: transaksi, rollback, dedupe, lock dua koneksi, NOWAIT, receipt dan reviewed
row preservation. WordPress/wpdb/preflight tetap stub, bukan full LocalWP PASS.
Container/storage uji sintetis sudah dihapus. Izin ini tidak mengizinkan write ke
LocalWP/produksi. Log/checkpoint ada di docs/qa/dev7.2 dan docs/PROGRESS.md.

Jangan jalankan store atau unggah ke ahda.sch.id. Sumber nyata berizin masih
belum tersedia; lingkungan cloud belum mengizinkan dua domain katalog pemerintah.
Di pengaturan jaringan lingkungan cloud perlu ditambahkan, tanpa menghapus domain
lain, referensi.data.kemendikdasmen.go.id dan referensi.data.kemdikbud.go.id.
Jangan ubah robots/keamanan WordPress untuk mengatasi pembatasan jaringan cloud.
Izin riset terdahulu tetap dibatasi20request total, kini sisa18; bukan izin crawl
seluruh pilot. Belum ada perubahan konfigurasi cloud yang terkonfirmasi.

Berikutnya: validasi sumber/izin, parser tambahan dan worker, review admin, lalu
publisher lokal dengan persetujuan terpisah. Kelengkapan artikel mengikuti bukti;
info yang belum ada tidak diisi tebakan. Rollback file Discovery ke7.1.1 tanpa
migrasi; pertahankan seluruh data. Produksi belum disentuh.

SHA-256 ZIP: 4dd8c23b76fde29d17f0d1558ee0e4f6f304004749d4ab20468a20fa49a274c4
