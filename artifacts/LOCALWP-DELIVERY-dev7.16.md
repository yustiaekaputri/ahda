# AHDA Discovery Engine 0.1.0-dev.7.16 — worker batch yang dapat dilanjutkan

Rilis ini mencakup form persetujuan admin dua tahap dari dev.7.15 dan worker lokal
untuk raw yang sudah tersimpan. Worker membentuk kandidat pending dan checkpoint
secara atomik. Tidak mengambil URL, menyetujui konten atau menerbitkan profil.
Semua fitur penulisan tetap OFF. Tidak perlu mengaktifkan atau mencoba writer
pada situs Anda sekarang.

## Unduh

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/archive-batch-dev7.16/artifacts
2. Klik `AHDA_Discovery_Engine_Archive_Batch_0.1.0-dev.7.16.zip`.
3. Klik **Download raw file** / ikon unduh, bukan **Code > Download ZIP**.
4. Simpan ZIP. Untuk upload WordPress tidak perlu diekstrak.

SHA-256: `27d15b625ba0d644f291e8ffd62ba0654a217c26771f1936d18346ccfcdbd40a`. Ukuran ZIP 1481370 byte.
Paket tetap hanya membawa QA terkini; bukti lama tersimpan di workspace dan
riwayat GitHub. Kode runtime, semua tes dan fixture tetap ada. Penghematan paket
besar dev.7.15 dipertahankan melalui cara pengemasan ini, bukan janji latensi VPS.

## Memasang opsional — hanya ahda.local

1. Local > **ahda > Start site**, backup situs dan folder plugin lokal dahulu.
2. **WP Admin**, login admin.
3. **Plugins > Add New Plugin > Upload Plugin > Choose File**.
4. Pilih ZIP dev.7.16 > **Install Now > Replace current with uploaded**, bila diminta.
5. Ganti AHDA Discovery Engine saja; AHDA School Directory 0.8.9 tetap.
6. Biarkan penulisan/crawler/publisher OFF. Jangan mengubah wp-config.php.

Jangan mengunggah ke ahda.sch.id melalui WinSCP. Upload merge bisa meninggalkan
QA versi lama, sehingga manfaat disk berbeda dari Upload Plugin > Replace.
Tidak ada migrasi, reimport, penghapusan profil, atau perubahan badge.
Rollback memakai backup lokal dev.7.15 tanpa menghapus tabel/jobs/receipt/audit.
Versi lama tidak memproses tipe batch baru; pasang kembali7.16 untuk melanjutkan.
Delivery aktif hanya ZIP terbaru dan panduan ini; riwayat Git tetap disimpan.

## Yang sudah dapat dilakukan

Dashboard: **AHDA Discovery > Kandidat**, pilih sekolah dan kandidat. Saat gate
positif sengaja diaktifkan dengan izin yang spesifik serta record sah tersedia,
reviewer memilih evidence raw + ID deklarasi, menekan pemeriksaan, lalu memberi
catatan/backup/konfirmasi pada halaman terpisah. Nilai lama dan usulan terlihat.
Persetujuan tetap bukan penerbitan atau verifikasi sumber independen.

Worker: input eksplisit1–200 NPSN pilot dan ID raw yang sudah tersimpan. Satu
pemanggilan maksimal3 sekolah; batas20detik/96MiB diperiksa antar sekolah, bukan
memutus parser di tengah. Lease90detik, maksimal3 percobaan per sekolah. Kandidat,
bukti, receipt dan checkpoint sekolah berhasil berkomit bersama. Crash/error tidak
boleh meninggalkan kandidat tanpa checkpoint yang sesuai atau menghapus prefix
sebelumnya. Raw yang tidak cocok/terblokir dilaporkan sebagai blocked; hasil itu
bukan fakta sekolah dan tidak menghentikan sekolah berikutnya untuk kode yang
secara eksplisit didukung. Error tidak dikenal berhenti untuk pemeriksaan/retry.

Nama command memakai underscore:

- `batch_stage --request-file=PATH --dry-run`: baca-saja, membekukan identitas dan scope; belum memeriksa raw/izin.
- `batch_enqueue`: defaultOFF, token preview + backup + konfirmasi ENQUEUE_ARCHIVE_BATCH.
- `batch_run`: defaultOFF, ID job + backup + konfirmasi RUN_ARCHIVE_BATCH.
- `batch_status --job-id=ID`: baca-saja, next_index dan hasil tiap sekolah; token lease/raw tidak dikeluarkan.
- `batch_control`: recover lease kedaluwarsa, retry failed/cancelled, atau cancel sisa dengan persetujuan khusus masing-masing.

Ini dokumentasi, bukan instruksi menjalankan write pada data nyata sekarang.
Kontrak JSON dan parameter lengkap ada di ZIP `docs/ARCHIVE_BATCH.md`.
Worker perlu ADE_LOCAL_ARCHIVE_BATCH_ENABLED dan modul candidate storage; paket
tidak mengaktifkan keduanya. Tidak ada cron, web worker, atau pengambilan nasional.

Completed artinya seluruh entri sudah dinilai, termasuk blocked, bukan seluruh
profil berhasil diperkaya. Manifest completed tidak di-reset. Untuk menilai ulang
blocked, gunakan raw sah yang baru atau subset tersisa yang eksplisit. Retry job
cancelled/failed mempertahankan prefix yang sudah berkomit. Kontrol menambahkan
audit jobs yang tidak ditimpa; penarikan izin tetap menahan publisher masa depan.
Jangan mengedit raw/checkpoint, menghapus job, atau mengubah approved secara manual.

## Bukti tes

- 27 suite / 1.634 pemeriksaan masing-masing PHP8.2 dan8.4 dengan DOM lulus.
- 1.566 tanpa DOM; ekstraksi HTML tidak dijalankan pada konfigurasi itu.
- 94 file PHP lint; 84 hash baseline dan6 regresi asli tetap utuh.
- 205 pemeriksaan layanan WordPress/MySQL sintetis dan89 pemeriksaan browser lulus.
- Empat sekolah sintetis membuktikan proses3+1, prefix parsial, rollback saat checkpoint gagal, lease token/attempt/expiry, recovery, retry terbatas, cancel/resume, audit kontrol atomik, pemilik job, corrupted checkpoint dan blocked yang jujur.
- COMMIT sungguh dijalankan lalu respons error disuntikkan: receipt/checkpoint sudah konsisten dan retry tidak menggandakan data. Ini simulasi lost-ack, bukan putus TCP/kill proses nyata.
- Seluruh25 tabel lama sintetis tetap utuh; kedua container/situs/server milik sesi dibersihkan; log PHP bersih.

Uji200 hanya bentuk manifest dengan fakeDB; batch SQL nyata diuji empat sekolah
sintetis, bukan200 profil faktual. Harness memakai WordPress/wpdb/nonce asli dengan
bootstrap salinan khusus dan marker kelas WP-CLI; full runner resmi CLI, LocalWP
pengguna, beban VPS dan hak sumber nyata belum diuji end-to-end. Tes browser tetap
mencakup nonce/session, editor/anonim, versi berubah, izin dicabut dan mobile.
Riwayat timeout login pada dev.7.15 tetap dicatat di bukti historis; tidak diklaim
sebagai perbaikan login situs pengguna. Tidak mengakses DB pengguna atau produksi.

Checkpoint `docs/PROGRESS.md`; log/diff `docs/qa/dev7.16` di dalam ZIP. Pengayaan
fakta nyata masih0/200. Selanjutnya publisher lokal dengan backup/rollback,
perluasan informasi berbukti, dan sumber yang sah. Artikel lengkap dan ranking
Google/rekomendasi AI belum terbukti dan tidak dijanjikan.
