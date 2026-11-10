# Audit AHDA dan Collector 2026 — 2026-11-10

## Source yang benar-benar tersedia

Workspace berisi baseline School Directory 0.8.9, Discovery R4a awal dan source
pengembangan dev7.18, tools validasi/seleksi NPSN, serta workbook pilot 200 sekolah.
Tidak ditemukan source Collector mandiri atau Excel gabungan nasional sekolah dan
peserta didik 2026. Ini batas audit checkout yang tersedia, bukan pernyataan bahwa
operator tidak memiliki source lain. Source lain perlu dikirim untuk audit lanjutan.

Setiap file ZIP Directory terbaru operator dibandingkan dengan baseline: identik.
Folder ZIP memakai nama v0.1.0, tetapi versi plugin 0.8.9. Baseline dan semua source
Discovery tetap utuh. Branch `development/collector-2026` berawal dari main kontrak
8123d8a, terpisah dari delivery plugin7.18. Tambahan `collector/` bukan pengganti
plugin dan tidak mengubah daftar beku 200 Tasikmalaya atau baseline 555.460 profil.

## Database dan dependensi WordPress

Directory memakai wpdb dan prefix runtime. `ahda_schools` memiliki unique NPSN;
tabel profil berelasi melalui school_id. Importer lama membaca CSV 12 kolom dan
mode APPLY dapat mengganti nama serta menginvalidasi indeks pencarian. Collector
TIDAK memanggil importer itu, AHDA_Profile::save, atau wp_insert_post.

AHDA_Profile::meta membaca meta berstatus verified. Terdapat 38 META_KEYS, termasuk
profile_description, profile_programs, profile_curriculum, profile_hours,
profile_source_url dan badge profile_school_verified yang harus tetap dilindungi.
Stats memiliki unique(school_id,academic_year). Fasilitas, prestasi, kegiatan,
penerimaan, dan biaya juga memakai tabel relasi; bukan semua dapat ditulis sebagai
meta bebas. Reader dan template school-profile.php adalah kontrak tampilan aktual.

Tujuh tabel Discovery/schema1 dipertahankan. Publisher dev7.17/18 hanya mendukung
pilot beku dan tiga field; belum profile_description/nasional. Collector tidak
memperluas allowlist atau mematikan gate tersebut. Helper baru hanya preview SELECT
pada LocalWP ahda.local, admin manage_options, Directory0.8.9. Join hanya NPSN unik.
Nama berbeda/hidden diblokir; deskripsi lama terisi ditandai PRESERVE_EXISTING.
Belum ada apply/approval/undo WordPress untuk deskripsi dari Collector.

## Kontrak SQLite dan keamanan impor

- Database lokal terpisah dengan application_id AHDA dan user_version1. Init menolak
  file existing; connect menolak database asing/tidak ada. Tidak ada migrasi WordPress.
- schools memakai PRIMARY KEY NPSN; observations unik(import,row); import diidentifikasi
  SHA256 file, sheet, mapping, tahun, dan URL; jobs unik NPSN; draf unik(NPSN,input_hash).
- Semua value SQL memakai parameter, header tidak menjadi identifier SQL. Data
  hanya identitas sekolah dan agregat siswa yang dipetakan eksplisit; kolom pribadi
  siswa tidak disalin. Formula dikarantina, XML memakai defusedxml wajib.
- XLSX read_only/data_onlyFalse/keep_linksFalse. Cap shared strings32MiB, satu member
  512MiB, total expandedZIP1GiB. Openpyxl tetap memuat shared strings: tidak dijanjikan
  constant memory untuk semua Excel nasional. File besar dapat perlu dipecah.
- SHA file dihitung streaming sebelum/sesudah impor. Perubahan source menahan impor.
  Checkpoint per baris berkomit; resume membaca ulang sampai cursor. Default satu
  pemanggilan10.000 baris. Tidak menyimpan semua rows di list; transaksi per row dapat
  memengaruhi throughput disk pada Windows dan belum diuji untuk555k.
- NPSN delapan karakter digit/alphanumerik legacy, nol awal string dipertahankan.
  Float/scientific notation tidak direkonstruksi, tidak ada join nama. Identitas
  berbeda pada NPSN sama dikarantina untuk keputusan operator, bukan last-write-wins.
- Count siswa harus integer0..1juta. Nilai invalid, L+P tidak sama total, atau count
  bertentangan pada tahun/NPSN sama ditandai dan tidak dipaksakan menjadi klaim.
  Duplikat identik menyimpan provenance, bukan menggandakan sekolah atau jumlah siswa.

## Queue, generator, dan sumber

Satu worker direkomendasikan. BEGIN IMMEDIATE, lease60detik/token, maksimal3attempt;
final reread fakta, CAS token+expiry, draft, checkpoint dan audit atomik. Recover
lease kedaluwarsa dan retry failed eksplisit. Pause antar job; error pertama
menghentikan run untuk pemeriksaan/backoff. Cache draf immutable berdasarkan fakta;
ekspor menolak draft stale. Konflik tidak otomatis diperbaiki dengan data yang baru.

Template hanya memakai fakta berkas operator, tanpa mengarang prestasi/fasilitas/
keunggulan. URL sumber jika diberikan, serta SHA/sheet/baris/tahun selalu tersedia.
File tanpa URL bukan sumber pemerintah terverifikasi. Internet source-add hanya
mencatat calon URL dengan status pending_identity_and_access_review. Pencarian,
autofetch, robots dan cache HTTP masih belum diintegrasikan pada Collector Python.

Ollama hanya lewat command eksplisit LOCAL_OLLAMA_EDIT: endpoint tetap loopback,
redirect ditolak, qwen2.5:0.5b, context1024/output256/thread2/temp0, timeout30detik,
response32KiB, keepalive0. Tidak auto-pull model atau memakai API AI berbayar.
Saran plaintext disimpan terpisah sebagai unverified_model_suggestion; tidak mengganti
fakta/template. Model masih dapat berhalusinasi. Transport diuji palsu, model asli
belum diuji. Kecepatan/RAM Windows4GB dan akselerasi AMD tidak dijanjikan.

## Bukti dan batas acceptance

PASS: 28 tes Collector/PHP facade, SQLite sintetis10/100/1000, workbook pilot200
existing menghasilkan10draft identitas tanpa angka siswa, regresi Discovery28suite/
1680checks PHP8.2DOM, hash84baseline dan112file runtime/tests/fixture Discovery utuh.
Source PHP helper lint8.2/8.4; facade dijalankan memakai PHP yang dicatat di QA.
Linux1000rows peak RSS sekitar38MiB, bukan benchmark Windows/LocalWP/555k.

Tes XML awal salah mengharapkan exception langsung; openpyxl membungkus
EntitiesForbidden di ValueError. Test diperbaiki untuk memeriksa __cause__ yang
tepat dan memastikan tidak ada sekolah dibuat; guard runtime tidak dilonggarkan.
Log awal dan final dipertahankan. Instal pip user pertama gagal filesystem read-only;
kemudian dependensi dipasang di venv workspace, tanpa memakai paket yang gagal.

NOT TESTED: Excel gabungan nasional2026 belum diberikan, RAM/throughput Windows555k,
model Ollama asli,10NPSN LocalWP/frontend/approval/apply-undo Collector, sumber internet
aktual. Tidak ada akses database pengguna atau produksi. Tidak mengklaim enam tahap
selesai, artikel lengkap, atau produksi siap. Raw rights/privacy/retention/quota pada
Discovery tetap gate sebelum bulk capture nyata.

Berikutnya: audit Excel aktual/definisi count,10preview LocalWP operator, sumber sah,
lalu publisher description terpisah dengan capability/nonce, approval, backup,
beforehash, transaksi, audit dan undo. Satu sekolah dahulu sebelum batch10/100/1000.
