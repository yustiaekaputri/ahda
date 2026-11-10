# AHDA Discovery Engine 0.1.0-dev.7.13 — deklarasi sumber operator

Paket pengembangan lokal ini menambahkan pencatatan deklarasi identitas sumber
serta izin penggunaan satu klaim faktual singkat, lengkap dengan referensi,
masa berlaku maksimal 90 hari, dan penarikan deklarasi. Penulisan default OFF.
Deklarasi manusia bukan verifikasi independen, persetujuan kandidat, atau publikasi.
Referensi dicatat sebagai metadata; sistem tidak mengakses atau mengesahkan isinya.

## Unduh dari GitHub

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/source-attest-dev7.13/artifacts
2. Klik `AHDA_Discovery_Engine_Source_Attestation_0.1.0-dev.7.13.zip`.
3. Klik **Download raw file** / ikon unduh. Jangan pilih **Code > Download ZIP**.
4. Simpan ZIP; tidak perlu diekstrak untuk upload melalui WordPress.

SHA-256 ZIP: `c3f8de359d5ae7fb69b7e5dbefed19fd9c955da018cc52cec1162336ae2abaf7`.

## Memasang opsional, hanya ahda.local

Tidak perlu mengulang demo atau membuat data baru untuk mencoba rilis ini.
Anda dapat menyimpan paket dahulu selama pengembangan berlanjut.

1. Di Local pilih **ahda > Start site**. Backup situs dan folder plugin lokal dahulu.
2. Buka **WP Admin**, login sebagai admin.
3. Pilih **Plugins > Add New Plugin > Upload Plugin > Choose File**.
4. Pilih ZIP dev.7.13 > **Install Now > Replace current with uploaded**, bila diminta.
5. Ganti AHDA Discovery Engine saja; AHDA School Directory 0.8.9 tetap.
6. Aktifkan companion bila diperlukan. Biarkan semua fitur penulisan/crawler/publisher OFF.

Jangan mengubah wp-config.php atau mengunggah ke ahda.sch.id lewat WinSCP.
Tidak ada migrasi skema, tabel baru, reimport, penghapusan profil, atau perubahan
badge. Rollback memakai backup plugin lokal tanpa menghapus tabel/data/event.
Daftar aktif GitHub menyisakan ZIP terbaru dan panduan ini. Branch delivery lama
dibersihkan; tautan historis dalam dokumen ZIP mungkin tidak aktif. Riwayat Git
masih disimpan; pembersihan daftar aktif tidak menghapus ukuran riwayat lama.

## Perilaku baru dan batasnya

Lima command baru memakai underscore: `attest_stage`, `attest_record`,
`attest_status`, `attest_revoke_stage`, `attest_revoke`. Detail kontrak request
13 field, scope dan parameter ada dalam ZIP: `docs/SOURCE_ATTESTATION.md`.
Command write sengaja tetap diblokir sampai ada persetujuan operator yang
spesifik serta pengaktifan terkontrol. Tidak perlu menjalankannya sekarang.

Deklarasi mengikat satu kandidat/bukti/raw dan kondisi sumber. Perubahan sumber,
raw, kedaluwarsa atau pencabutan menahan validitas. Preview lama ditolak jika
versi kandidat berubah sebelum penyimpanan, termasuk saat transaksi memiliki
snapshot MySQL lama. Retry identik tidak menggandakan event. Penarikan tetap
bisa dicatat saat sumber terblokir; event asli tidak dihapus.

Izin satu klaim dengan atribusi tidak meliputi seluruh artikel, gambar/logo,
raw atau izin crawler. Status baca-saja adalah snapshot; approval selanjutnya
wajib memeriksa ulang deklarasi, pencabutan, raw dan target dalam transaksi.
Tidak ada perubahan status persetujuan kandidat, promosi sumber menjadi resmi,
atau penerbitan profil otomatis. Penarikan per deklarasi bukan larangan global
suatu domain dan tidak otomatis menarik artikel yang telah terbit.

## Bukti tes

- 26 suite / 1.588 pemeriksaan lulus masing-masing pada PHP 8.2 dan 8.4 dengan DOM.
- 1.520 tanpa DOM; ekstraksi HTML tidak dijalankan pada konfigurasi itu.
- 88 file PHP lint; 84 hash baseline dan 6 file regresi asli tetap utuh.
- 118 pemeriksaan layanan WordPress/wpdb + 47 pemeriksaan browser/admin lulus
  pada MySQL 8.4 sintetis; seluruh 25 tabel lama sintetis tetap utuh.
- Uji dua sesi database membuktikan preview ditolak saat kandidat berubah
  meski transaksi telah membaca snapshot lama. Kegagalan INSERT/COMMIT, rollback,
  retry, withdrawal, capability dan default OFF diuji.
- Kedua container/situs/server uji milik sesi sudah dibersihkan; log PHP bersih.
- Tidak mengakses atau mengubah database pengguna, wp-config, atau produksi.

Harness memakai service API langsung dan marker keberadaan kelas WP-CLI untuk
modul write lama. Runner resmi WP-CLI lengkap, LocalWP pengguna dan beban VPS
belum diuji end-to-end. Ini bukan bukti izin nyata atau sumber sekolah asli.
Log/diff: `docs/qa/dev7.13`; checkpoint: `docs/PROGRESS.md` di dalam ZIP.

Pengayaan fakta nyata masih 0/200 sekolah. Estimasi fondasi ~55% tetap kualitatif,
bukan persentase isi profil. Tahap berikutnya approval positif dengan validasi
terkunci, worker berkelanjutan dan publisher lokal berizin dengan rollback.
Ranking Google dan rekomendasi AI tidak dapat dijamin.
