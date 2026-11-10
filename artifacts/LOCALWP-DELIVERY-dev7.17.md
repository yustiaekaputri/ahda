# AHDA Discovery Engine dev7.17 — publisher lokal dan rollback

Rilis ini menyertakan dashboard persetujuan dua tahap, worker batch yang dapat
dilanjutkan, serta publisher CLI lokal untuk satu sekolah dengan undo. Semua
writer/crawler/publisher tetap OFF. Ini belum izin menerapkan perubahan ke DB Anda.

## Unduh dan pasang opsional di ahda.local

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/local-publisher-dev7.17/artifacts
2. Klik `AHDA_Discovery_Engine_Local_Publisher_0.1.0-dev.7.17.zip`.
3. Klik **Download raw file** atau ikon unduh. Jangan pilih Code > Download ZIP.
4. Local > ahda > Start site. Backup situs dan folder plugin lokal terlebih dahulu.
5. WP Admin > Plugins > Add New Plugin > Upload Plugin > Choose File.
6. Pilih ZIP > Install Now > Replace current with uploaded, bila diminta.
7. Ganti Discovery Engine saja. AHDA School Directory 0.8.9 tetap.
8. Biarkan seluruh gate penulisan dan jaringan OFF; jangan edit wp-config.php.

SHA-256: `446ed31ba5f02069b76ea305c3357544ffea48c594fdc3be4e572b8c294b6fda`. Ukuran 1618043 byte. Folder ZIP `ahda-discovery-engine`.
Tidak perlu mengulang demo lama. Jangan unggah ke ahda.sch.id atau produksi.
Penggantian melalui WordPress menghindari file lama tertinggal dari upload merge.
Paket hanya memuat QA terkini; bukti historis tetap di workspace/riwayat Git.

## Fungsi yang tersedia dan batasnya

Dashboard **AHDA Discovery > Kandidat** mendukung preview dan persetujuan admin
terpisah dengan nonce, capability, backup dan konfirmasi. Approved belum published.
Worker lokal menerima manifest 1–200 NPSN pilot dan receipt raw sah yang sudah
tersimpan. Satu run maksimal tiga entri; checkpoint/kandidat/evidence/receipt
berkomit bersama. Lease, retry terbatas, cancel/recover dan audit tersedia.
Completed juga bisa memuat blocked; bukan berarti semua profil sudah diperkaya.
Kontrak: `docs/ARCHIVE_BATCH.md` di ZIP.

Publisher baru hanya CLI di LocalWP, default OFF, satu NPSN pilot yang sengaja
dikonfigurasi. Hanya programs, curriculum atau hours yang sudah approved, dengan
profile_source_url yang sesuai evidence. Sumber lama berbeda menyebabkan blok.
Tidak menyentuh badge verifikasi, nama, NPSN atau indeks. Bukan publisher artikel
lengkap dan tidak berjalan otomatis setelah approval/worker.

Command memakai underscore: `publish_stage`, `publish_apply`, `publish_undo_stage`,
`publish_undo`, `publish_receipt` di bawah `wp --user="admin" ade pilot`.
Ini daftar fitur, bukan instruksi menjalankan write sekarang. Parameter, JSON,
konfirmasi, preview dan rollback lengkap di `docs/LOCAL_PUBLICATION.md` dalam ZIP.
Jangan memakai ID fixture cloud pada database Anda. Uji satu sekolah nyata perlu
sumber sah dan persetujuan tindakan khusus sebelum dijalankan; perluasan 20 sekolah
menunggu hasil serta izin berikutnya.

Transaksi menerapkan klaim, kutipan, kandidat dan audit/receipt bersama. Konflik
identitas/versi/nilai lama/izin menahan apply. Undo hanya mengembalikan image yang
persis milik receipt, menjaga edit admin lain, dengan urutan terbalik per sekolah.
Izin kedaluwarsa/dicabut tidak otomatis menghapus klaim yang terlanjur diterapkan:
operator perlu review/undo. Receipt historis bukan bukti hak sumber masih berlaku.
Raw retention/enkripsi/kuota total masih gate sebelum bulk capture nyata.

Rollback file: gunakan backup dev7.16 tanpa menghapus tabel/jobs/audit. Pertahankan
7.17 untuk menjalankan undo publikasi miliknya sebelum downgrade; 7.16 tidak punya
modul undo M4. Tidak ada migrasi, reimport, rebuild atau penghapusan profil lama.

## Bukti pengujian

- 27 suite: 1.643 pemeriksaan masing-masing PHP8.2/8.4 dengan DOM;1.575 tanpa DOM.
- 96 PHP lint;84 hash baseline dan6 tes regresi asli utuh.
- WordPress7.1.4, Directory0.8.9, MySQL8.4 sintetis:205 layanan sebelumnya +69 publisher/undo =274, serta99 browser/HTTP HTML.
- Uji defaultOFF, capability, JSON/input, konflik, pencabutan izin, konkurensi dua sesi, fault tiap write/COMMIT, receipt retry, sumber dan rollback.
- Klaim/kutipan terlihat pada template/reader Directory asli setelah apply, hilang setelah undo; canonical dan node JSON-LD School dengan NPSN diperiksa.
- Semua25 tabel lama sintetis kembali ke hash awal. Container, situs dan server milik tes dibersihkan; log PHP bersih.

Ini pengujian salinan cloud dengan data sintetis dan tema minimal khusus tes,
bukan LocalWP Anda, benchmark VPS,200 sekolah faktual, atau full runner resmi CLI.
Kesalahan ekspektasi tes awal beserta perbaikannya tetap dicatat pada QA; tidak
mengendurkan guard. COMMIT lalu respons error disuntikkan, bukan putus TCP nyata.
Log/diff: `docs/qa/dev7.17`; checkpoint: `docs/PROGRESS.md` di ZIP.

## Langkah sumber nyata berikutnya

Pengayaan fakta nyata tetap **0/200**. Ranking Google atau rekomendasi AI belum
terbukti dan tidak dapat dijanjikan. Tidak ada akses DB pengguna/produksi.

Izin katalog terbatas Anda masih berlaku, tetapi pengaturan cloud belum mengizinkan
host. Tambahkan di pengaturan lingkungan cloud > jaringan/domain yang diizinkan:

- `referensi.data.kemendikdasmen.go.id`
- `referensi.data.kemdikbud.go.id`

Pertahankan domain/preset yang sudah ada. Draft konfigurasi gagal diverifikasi dua
kali sehingga tidak ada perubahan yang disimpan/dipublikasikan oleh sesi ini.
Sesudah settings berlaku, validasi akses baru sebelum riset:18 dari20 request
tersisa,10 sekolah pertama, satu proses, jeda minimal5detik/host, patuhi robots/ToS.
Detail blocker dan aturan skill: `docs/NETWORK_RESEARCH_PENDING.md`.
