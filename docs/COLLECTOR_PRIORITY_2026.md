# Collector 2026.2 — prioritas SMP/MTs dan inspeksi Excel besar

Permintaan operator: SMP dan MTs dahulu, kemudian SMA, SMK, MA dan sederajat.
Urutan ini diterapkan pada antrean SQLite, bukan mengubah NPSN, data WordPress,
atau daftar beku 200 Tasikmalaya. Kelompok pertama dan kedua masing-masing diurutkan
NPSN agar hasil dapat diulang. Tidak ada pencocokan sekolah berdasarkan nama.

## Implementasi

- school_form eksplisit menentukan priority0 untuk SMP/MTs dan padanan yang terdaftar;
  priority1 untuk SMA/SMK/MA dan padanan; priority2 untuk lainnya atau tidak diketahui.
  Alias lengkap ada di school_priority dan README. Tidak menebak jenjang dari nama.
- Run default mengecualikan priority2. Operator dapat memilih --include-other secara
  eksplisit; grup lain tetap sesudah kedua kelompok prioritas. SLB tanpa jenjang
  tidak diasumsikan sebagai SMPLB/SMALB. Tidak menyimpulkan negeri dari alias MTsN/MAN.
- SQLite schema2 menambah jobs.priority dan partial index jobs_ready_priority hanya
  pada queued/retry_wait dengan attempts<3. EXPLAIN membuktikan indeks dipakai tanpa
  temporary sort pada query default. Ini menghindari pengurutan semua job selesai
  pada setiap run. Bukan benchmark nasional555k atau Windows4GB.
- Database baru langsung schema2. Database schema1 perlu command upgrade eksplisit,
  backup eksklusif .before-priority-v2.sqlite, worker berhenti dan lease direcover
  memakai source lama dahulu. Backup tidak ditimpa. ALTER/index/prioritas/version/
  audit berada dalam satu transaksi; fault injection membuktikan rollback schema.
  Semua fakta, draf dan status lama dipertahankan. Rollback source2026.1 perlu backup
  database schema1 ketika semua proses berhenti; tidak ada migrasi WordPress.

## File yang baru diunggah

Download tool menolak AHDA_Gabungan_Sekolah_Peserta_Didik_2026.xlsx karena melebihi
batas transfer32MiB. File belum berhasil dipindahkan ke workspace. Nama kolom,
jumlah sekolah, SHA256, hitungan siswa, dan distribusi jenjang file ini BELUM
DIKETAHUI. Tidak menganggap hasil workbook pilot sebagai hasil file nasional.
Tidak mengulang transfer dengan rute lain atau mengunggah dataset ke GitHub.

Command inspect-xlsx dapat dijalankan pada file asli di Windows. Pembaca ZIP/XML
memeriksa baris pertama sebagai calon header, membaca shared strings secara
streaming hanya untuk indeks header, bukan memuat seluruh tabel string. Defusedxml
menolak entity. Batas metadata1MiB,100sheet,256kolom/2000karakter header,
scan worksheet16MiB/sharedstrings64MiB,10000member tanpa nama ganda. Tidak memakai
jumlah baris yang dideklarasikan sebagai jumlah sekolah. Ini inspeksi header saja,
bukan importer penuh tanpa batas; cap memori importer openpyxl tetap berlaku.

Konfirmasi bahwa baris pertama benar-benar header sebelum membagikan hasil, karena
file tanpa header dapat menaruh data pribadi pada baris tersebut. Untuk uji cloud,
salin data SMP/MTs beserta header ke file bagian <32MiB, tanpa data pribadi siswa,
sambil mempertahankan workbook asli. Mapping school_form wajib disediakan agar
penjadwalan jenjang bekerja; jika tidak, job masuk priority2 dan tidak diproses default.

## Bukti pengujian

38 tes unik lulus:22tes sebelumnya,10tes prioritas/migrasi/inspeksi baru,6tes PHP
preview facade. Mencakup NPSN SMP/MTs lebih besar tetap didahulukan, missing/unknown/
SD/TK ditahan, alias eksplisit, index query plan, backup/schema/cache idempotensi,
lease aktif, rollback fault, header inline/shared rich strings, serta XXE ditolak.
Run awal menemukan58 karena TestCase lama ikut terimpor dan terdiscovery dua kali;
import fixture diperbaiki. Final38 adalah jumlah unik, tidak mengklaim58tesunik.

SQLite sintetis1000 mixed SMP/SMA lulus tanpa duplikasi. Log benchmark menunjukkan
sekitar40MB peak RSS Linux. Runtime header baru tidak dipakai dalam benchmark itu;
streaming header diuji terpisah. Tidak ada pengujian Windows atau file nasional.

Workbook pilot yang SEBELUMNYA tersedia:177priority0 dan23priority1; seluruh177
diproses sebelum23,200draf identitas tersimpan di SQLite sementara. Workbook asli
utuh, database sementara dibersihkan, tidak ada klaim jumlah siswa/publikasi.
Plugin Directory/Discovery dan helper WordPress tidak berubah. Tidak ada network
fetch atau database WordPress pengguna/produksi yang diakses atau ditulis.

Bukti docs/qa/collector-priority-2026. Instruksi Windows collector/README.md.
Berikutnya: header file aktual, potongan SMP/MTs <32MiB, mapping yang benar, staged
10 NPSN dan preview operator LocalWP. Pencarian internet, izin sumber dan publisher
deskripsi tetap milestone terpisah; jangan klaim artikel nasional sudah terisi.
