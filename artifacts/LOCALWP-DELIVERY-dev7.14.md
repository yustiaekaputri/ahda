# AHDA Discovery Engine 0.1.0-dev.7.14 — persetujuan satu klaim

Rilis pengembangan lokal menambahkan persetujuan satu kandidat berbukti raw,
dengan deklarasi sumber/izin yang masih berlaku dan belum dicabut. Persetujuan
menyimpan nilai kandidat tanpa edit, audit dan receipt secara atomik. Status
publikasi tetap **not_ready**. Semua penulisan tetap **OFF** secara bawaan.
Deklarasi operator bukan verifikasi independen atau pengesahan hukum izin.

## Unduh

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/approve-dev7.14/artifacts
2. Klik `AHDA_Discovery_Engine_Approval_0.1.0-dev.7.14.zip`.
3. Klik **Download raw file** / ikon unduh, bukan **Code > Download ZIP**.
4. Simpan ZIP. Tidak perlu diekstrak untuk upload melalui WordPress.

SHA-256 ZIP: `259c05ca78ef6ac3d54f4e8190188e402e9c0c12f0b8e40a98b073f12804c237`.

## Memasang opsional — hanya ahda.local

Tidak perlu mengulang demo atau membuat data baru. Boleh simpan paket dahulu.

1. Di Local, pilih **ahda > Start site**, backup situs/folder plugin lokal dahulu.
2. Buka **WP Admin**, login admin.
3. **Plugins > Add New Plugin > Upload Plugin > Choose File**.
4. Pilih ZIP dev.7.14 > **Install Now > Replace current with uploaded** bila diminta.
5. Ganti AHDA Discovery Engine saja; AHDA School Directory 0.8.9 tetap.
6. Aktifkan companion bila diperlukan; biarkan penulisan/crawler/publisher OFF.

Jangan mengubah wp-config.php atau mengunggah ke ahda.sch.id melalui WinSCP.
Tidak ada migrasi/import/penghapusan profil/perubahan badge. Rollback memakai
backup plugin lokal dev.7.13, tanpa menghapus data/tabel/event/audit persetujuan.
Daftar delivery aktif GitHub menyisakan ZIP terbaru dan panduan ini; branch lama
dibersihkan. Riwayat Git tetap disimpan sehingga ukuran riwayat lama tidak hilang.

## Perilaku baru

`approve_stage` memeriksa satu kandidat dan satu bukti raw dengan deklarasi yang
tepat. Hanya bila record sah sudah tersedia, perintah baca-saja adalah:

```bat
wp --user="admin" ade pilot approve_stage --npsn=NPSN --candidate-id=CANDIDATE --evidence-id=EVIDENCE --attestation-id=GRANT --dry-run
```

Ganti placeholder dengan ID yang benar. Tidak perlu menjalankan ini sekarang bila
baru memiliki demo yang tidak disimpan. Preview tidak menulis, mengambil URL,
atau memberi persetujuan. Nilai usulan tetap data tidak tepercaya.

`approve_record` adalah writer terpisah, sengaja OFF. Dokumentasi teknis lengkap
ada di ZIP `docs/POSITIVE_REVIEW.md`; jangan menjalankannya pada data nyata sebelum
ada persetujuan tindakan/backup/konfigurasi yang spesifik. Panel admin belum
memiliki tombol approval positif; jalur baru saat ini CLI/service saja.

Di dalam transaksi, sistem memeriksa lagi grant/pencabutan/expiry, raw/source,
hash nilai lama, versi kandidat dan preview. Kandidat yang berubah atau izinnya
dicabut setelah preview harus ditolak. Retry identik tidak menggandakan audit.
Hanya tiga field teks awal didukung: program, kurikulum dan jam sekolah; ini
belum menghasilkan artikel lengkap. Edit dan bulk approval belum tersedia.

Setelah disetujui, pencabutan izin tetap membuat grant tidak berlaku. Keputusan
lama disimpan sebagai sejarah, bukan izin publikasi yang berlaku selamanya.
Publisher belum tersedia dan kelak wajib memeriksa ulang semua syarat. Tidak ada
perubahan profil lama, verifikasi sumber otomatis, atau penerbitan produksi.

## Bukti pengujian

- 26 suite / 1.597 pemeriksaan masing-masing PHP 8.2 dan 8.4 dengan DOM lulus.
- 1.529 tanpa DOM; ekstraksi HTML tidak dijalankan pada konfigurasi itu.
- 89 file PHP lint; 84 hash baseline dan 6 regresi asli tetap utuh.
- 151 pemeriksaan layanan WordPress/wpdb/MySQL sintetis dan 47 pemeriksaan browser lulus.
- Capability, nonce, scope, konfirmasi, penolakan input HTML, pencabutan sesudah
  preview, setiap kegagalan UPDATE/INSERT audit/INSERT receipt/COMMIT, rollback,
  retry dan nilai approved yang tidak bisa ditimpa diuji.
- Dua koneksi MySQL membuktikan kandidat berubah atau pencabutan baru tetap
  terlihat oleh pemeriksaan terkunci, meski transaksi memiliki snapshot lama.
- Semua 25 tabel lama sintetis tetap utuh; kedua container/situs/server uji sendiri
  sudah dibersihkan. Log PHP bersih. Tidak menyentuh database pengguna/produksi.

Uji browser mencakup login/admin/nonce/review negatif dan inspector yang sudah
ada, bukan form approval positif baru. Uji persetujuan baru memakai service API
langsung setelah bootstrap WordPress nyata dengan marker keberadaan kelas WP-CLI;
runner resmi WP-CLI lengkap dan LocalWP pengguna belum diuji end-to-end. Parser
resmi CLI diuji terpisah offline. Ini bukan uji beban VPS atau bukti izin nyata.
COMMIT fault disuntikkan sebelum commit, bukan kegagalan TCP/lost-ack nyata.

Log/diff `docs/qa/dev7.14`; checkpoint `docs/PROGRESS.md` di dalam ZIP.
Pengayaan fakta nyata masih **0/200**; estimasi fondasi ~55% tetap perkiraan kasar.
Selanjutnya form persetujuan admin, worker ekstraksi yang dapat dilanjutkan dan
publisher lokal berizin dengan rollback. Ranking Google/rekomendasi AI tidak dijamin.
