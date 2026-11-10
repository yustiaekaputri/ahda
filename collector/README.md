# AHDA Collector offline — pratinjau pengembangan 2026.2

Collector ini menambahkan pengolahan Excel dan draf ke proyek AHDA yang ada.
Plugin Directory 0.8.9 dan Discovery 7.18 tidak diubah. Collector tidak membuat
WordPress Posts, mengimpor ulang sekolah, atau menulis database WordPress.
Tidak diperlukan OpenAI API maupun API AI berbayar lainnya.

**Tersedia:** impor XLSX ke SQLite, pencocokan NPSN, laporan konflik dan angka siswa,
provenance, antrean yang dapat dilanjutkan, cache draf template, saran Ollama opsional,
ekspor draf, serta preview baca-saja di LocalWP.

**Belum tersedia:** pencarian dan pengambilan internet otomatis, persetujuan dan
penerbitan `profile_description`, artikel lengkap, serta uji nyata 10 profil LocalWP.
Excel gabungan nasional 2026 belum tersedia untuk diuji. Memasang ZIP Discovery
saja tidak menjalankan Collector atau mengubah halaman sekolah.

## Prioritas jenjang — versi 2026.2

Antrean sekarang memproses **SMP/MTs dahulu**, kemudian **SMA/SMK/MA**.
Dalam setiap kelompok, urutan NPSN tetap deterministik. Klasifikasi memakai
`school_form` yang dipetakan dari kolom bentuk pendidikan, bukan nama sekolah.
Contoh mapping siswa kini menyertakan `school_form: Bentuk Pendidikan`; sesuaikan
header itu dengan Excel aktual. Tanpa kolom tersebut, jenjang dianggap belum diketahui.

Padanan yang didukung secara eksplisit: SMPLB/SMPK/SMPTK/Paket B pada kelompok
pertama; SMALB/SMAK/SMTK/MAK/Paket C/Utama Widya Pasraman pada kelompok kedua.
MTsN/MTsS dan MAN/MAS dikenali sebagai label bentuk, bukan penetapan status negeri.
SLB yang tidak menyebut jenjang, bentuk asing, SD/TK, serta nilai kosong tidak
masuk run default. `run --include-other` hanya untuk keputusan operator yang sengaja
ingin memproses kelompok lain setelah dua kelompok prioritas.

Database baru memakai schema SQLite2. Jika sudah membuat database dengan Collector
2026.1, hentikan semua worker dan selesaikan/recover lease memakai source lama dahulu.
Simpan backup source, lalu jalankan dengan source baru:

```bat
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite upgrade
```

Upgrade membuat `ahda2026.sqlite.before-priority-v2.sqlite`, mempertahankan sekolah,
fakta, draf dan status, lalu menambah prioritas dan indeks antrean. Lease aktif dan
backup dengan nama sama ditolak. Tidak ada migrasi diam-diam saat connect.
Jika upgrade gagal, simpan backup untuk pemeriksaan, jangan menghapusnya agar bisa
memaksa retry. Rollback ke source2026.1 memerlukan backup database schema1 ketika
semua proses berhenti; source lama tidak boleh dipakai pada schema2.

## Instalasi Windows

Unduh branch `development/collector-2026` dari GitHub melalui **Code > Download ZIP**.
Ekstrak, misalnya ke `C:\AHDA\ahda`. Ini source Collector, bukan ZIP plugin yang
diunggah melalui WordPress. Jangan menaruhnya di `wp-content/plugins`.

Pasang Python 3.11 atau 3.12 versi 64-bit dari python.org. Buka Command Prompt:

```bat
cd /d C:\AHDA\ahda\collector
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite init
```

Sesuaikan folder dengan hasil ekstraksi Anda. Dependensi perlu diunduh sekali;
impor dan generator template berjalan offline. SQLite harus berada di disk lokal,
bukan OneDrive atau network share. Simpan di folder privat dengan izin Windows
yang sesuai. `init` menolak file yang sudah ada; jangan menghapus database untuk
melanjutkan pekerjaan. Backup SQLite ketika worker berhenti.

## Menyiapkan Excel dan mapping

Unggahan `AHDA_Gabungan_Sekolah_Peserta_Didik_2026.xlsx` melebihi batas transfer
alat cloud 32 MiB; belum dibaca atau dihitung. File aslinya dapat diperiksa di Windows
menggunakan source ini. Salin file ke path contoh atau sesuaikan parameter:

```bat
.venv\Scripts\python.exe -X utf8 ahda_collector.py --db unused inspect-xlsx --file "C:\AHDA\AHDA_Gabungan_Sekolah_Peserta_Didik_2026.xlsx" > header-2026.json
```

Perintah tidak membuat database. Ia membaca baris pertama setiap worksheet sebagai
calon header; bukan baris data, dan tidak menyimpulkan jumlah sekolah dari dimensi.
Periksa `header-2026.json` sebelum membagikannya: jika baris pertama ternyata data
pribadi, jangan kirim. Shared strings dipindai streaming hanya untuk indeks header,
dengan batas scan 64 MiB, header worksheet 16 MiB, dan maksimal 100 sheet. Jika batas
tercapai, pisahkan workbook; jangan menurunkan pengamanan XML.

Untuk pengujian cloud pada data aktual, simpan salinan terfilter **SMP/MTs dahulu**
dengan header utuh dan ukuran tiap file di bawah 32 MiB. Jangan unggah data pribadi
siswa. File sumber asli tetap dipertahankan. Pemeriksaan header ringan ini tidak
mengubah batas memori importer penuh di bawah.

Isi file gabungan sekolah dan agregat peserta didik 2026 belum dapat ditransfer
ke workspace karena batas ukuran alat. Header harus diperiksa pada file aktual. Collector
memerlukan header pada baris pertama, sheet yang dipilih secara eksplisit, dan
mapping JSON. Tidak ada pencocokan sekolah berdasarkan nama.

Salin `examples\mapping-with-students.json`, lalu ganti nama header agar persis
sama dengan Excel. Hapus field yang tidak tersedia. `npsn` dan `name` wajib;
field opsional adalah `school_form`, `province`, `regency`, `students_total`,
`students_male`, dan `students_female`. Jangan memetakan nama, NISN, atau data
pribadi siswa. Formula dikarantina, bukan dihitung dari cached value.

Contoh berikut memakai path dan header yang harus Anda sesuaikan:

```bat
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite import-xlsx --file "C:\AHDA\sekolah-siswa-2026.xlsx" --sheet "Data" --mapping examples\mapping-with-students.json --year 2026 --max-rows 10000
```

Jika memiliki URL penerbit asli, tambahkan `--source-url "https://DOMAIN/PATH"`.
URL tersebut hanya menjadi referensi; Collector tidak mengambilnya atau menyatakan
situs itu resmi. Tanpa URL, SHA-256 file, sheet, nomor baris, dan tahun tetap dicatat.
Jangan mengarang URL. Tahun 2026 adalah metadata yang diberikan operator.

Jalankan perintah yang sama untuk resume sampai `status: complete`. File, mapping,
sheet, tahun, dan URL harus tetap sama. Perubahan membuat identitas impor baru.
Jangan mengedit Excel ketika impor berjalan. Resume XLSX membaca ulang baris
sebelum cursor, tetapi tidak menyimpan semua baris di RAM.

Openpyxl tetap memuat tabel shared strings ke memori. Collector membatasi tabel itu
32 MiB dan ukuran ZIP setelah dekompresi 1 GiB; ini bukan jaminan bahwa semua Excel
nasional muat pada RAM 4 GB. Bila ditolak, pecah file dengan header dan NPSN utuh.
Jangan menonaktifkan perlindungan XML. Tutup Excel, browser, dan Ollama saat impor.

## Memeriksa masalah dan membuat draf

```bat
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite report
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite issues --limit 25 --after 0
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite run --limit 10
```

Untuk halaman masalah berikutnya, gunakan cursor hasil sebagai `--after`.
`run` tidak mengakses internet. Impor terkait harus selesai dan identitas harus
bebas konflik. Draf selalu berstatus `pending_review`.

- `DUPLICATE_NPSN_OBSERVATION`: sumber tambahan untuk NPSN yang sama, bukan sekolah baru.
- `IDENTITY_CONFLICT`: nama/wilayah/bentuk bertentangan; draf NPSN tersebut ditahan.
- Angka negatif, bukan bilangan bulat, atau jumlah laki-laki dan perempuan yang tidak
  sesuai total ditandai dan tidak dipaksakan masuk ke artikel.
- Angka berbeda pada NPSN dan tahun yang sama ditahan, bukan dijumlahkan atau dipilih diam-diam.

```bat
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite control pause
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite control resume
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite control recover
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite control retry-failed
```

Pause berlaku antar job. Recover hanya mengambil lease yang kedaluwarsa setelah
60 detik. Batas percobaan tiga kali; retry untuk job failed dilakukan secara eksplisit.
Satu worker disarankan. Error menghentikan batch untuk pemeriksaan; perbaiki penyebab
sebelum menjalankan ulang. Jangan mengedit status SQL secara manual.

## Ekspor dan preview profil LocalWP

Ganti `ID_DARI_HASIL_RUN` dengan draft_id yang benar:

```bat
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite export-draft --draft-id ID_DARI_HASIL_RUN --output draft-sekolah.json
```

Ekspor menolak file output yang sudah ada dan draf yang sumbernya sudah berubah.
Ini belum paket impor WordPress yang disetujui.

Di Local, pilih **ahda > Start site > Open site shell**, lalu jalankan:

```bat
wp --user="admin" eval-file "C:\AHDA\ahda\collector\wordpress-preview.php" "C:\AHDA\ahda\collector\draft-sekolah.json"
```

Helper hanya melakukan SELECT setelah memeriksa admin, host `ahda.local`, dan
Directory 0.8.9. WordPress memakai bootstrap LocalWP seperti perintah WP-CLI biasa;
helper tidak membaca credential atau `wp-config.php` secara langsung.

Hasil harus menunjukkan `apply_supported: false` dan `database_writes: 0`.
NPSN yang hilang atau duplikat ditolak. Nama berbeda atau profil tersembunyi ditahan.
Deskripsi yang sudah terisi mendapat `PRESERVE_EXISTING_DESCRIPTION`.
`before_sha256` hanya hasil preview, bukan izin menerapkan perubahan.
Belum ada command apply atau approve untuk draf deskripsi Collector ini.
Jangan menjalankannya di produksi `ahda.sch.id`.

## Ollama opsional

Template bekerja tanpa Ollama. Untuk mencoba penyunting lokal, pasang Ollama Windows
melalui installer resminya. Periksa ruang disk dan memori terlebih dahulu:

```bat
ollama pull qwen2.5:0.5b
.venv\Scripts\python.exe ahda_collector.py --db ahda2026.sqlite ollama-edit --draft-id ID_DARI_HASIL_RUN --confirm LOCAL_OLLAMA_EDIT
```

`pull` mengunduh model dan memerlukan internet; Collector tidak mengunduhnya otomatis.
Server harus berjalan pada `127.0.0.1:11434`. Adapter membatasi context 1024, output
256 token, dua thread, timeout 30 detik, dan `keep_alive: 0`. Tidak bergantung pada
akselerasi GPU AMD. Kinerja pada Windows 4 GB belum dibuktikan; coba satu draf dengan
LocalWP, browser, dan impor berhenti dahulu. Timeout tidak mengganti draf.

Saran disimpan terpisah sebagai `unverified_model_suggestion`. Model bisa mengarang
fakta, sehingga saran wajib dibandingkan dengan sumber. Template dan fakta tidak
ditimpa. Tidak ada OpenAI API/token berbayar. Model asli belum diuji di cloud;
pengujian adapter menggunakan transport palsu dan dinyatakan demikian di laporan.

## Sumber internet, pengujian, dan rollback

`source-add --npsn NPSN --url https://... --kind school_website` hanya mencatat calon
sumber. Label `government` juga belum berarti terverifikasi. Pengambilan robots/HTML,
pencarian otomatis, dan cache HTTP belum diintegrasikan. Izin per host, robots,
SSRF, dan pembatasan akses tetap wajib untuk adapter berikutnya. Izin satu website
bukan izin mengambil semua situs sekolah. Pilot Discovery 200 tidak diubah.

Jangan mengunggah database atau Excel privat ke GitHub. Retensi, enkripsi penyimpanan,
izin sumber, dan penerbitan perlu ditetapkan sebelum penggunaan produksi.

```bat
.venv\Scripts\python.exe -m unittest discover -s tests -v
.venv\Scripts\python.exe tests\benchmark.py --rows 10
```

Enam tes facade PHP memerlukan `php` di PATH atau `PHP_BIN`; jika tidak tersedia,
tes tersebut ditandai skipped. Uji SQLite sintetis 10/100/1.000 bukan uji profil
LocalWP. Pengukuran Linux untuk 1.000 baris sekitar 38 MiB peak RSS; jangan
mengekstrapolasikannya menjadi jaminan Windows atau 555.000 sekolah.

Bukti awal: `docs/qa/collector-2026`; bukti prioritas terbaru: `docs/qa/collector-priority-2026` pada branch. Audit: `docs/COLLECTOR_AUDIT_2026.md`.
Checkpoint: `docs/PROGRESS.md`. Rollback dengan menghentikan Collector lalu memakai
source dan backup SQLite sebelumnya. Tidak ada perubahan profil WordPress untuk
di-undo oleh Collector ini. Ranking Google atau rekomendasi AI tidak dijanjikan.
