# dev.7.3 — Parser dokumen sekolah lokal

## Perubahan

Parser CSV terstruktur dan tabel HTML terbatas tersedia. Tujuannya menghasilkan
kandidat dengan evidence dari dokumen tersimpan, bukan membuat fakta baru. Bidang
saat ini tetap program/kurikulum/jam layanan. Lebih banyak bidang dan worker,
review admin serta publisher belum selesai. Tidak ada profil nyata diperkaya,
fetch jaringan, perubahan database, persetujuan atau penerbitan oleh parser.
Pengaturan sumber katalog cloud tetap diblokir; sisa izin riset18/20 tidak dipakai.

## Pemasangan LocalWP

Tidak perlu mengulang demo artikel7.2 yang sudah berhasil. Untuk menguji parser
baru, ganti Discovery dengan paket ini setelah backup lokal:

1. Local > AHDA > Start Site > WP Admin, login admin.
2. Plugins > Add New Plugin > Upload Plugin > Choose File.
3. Pilih AHDA_Discovery_Engine_M2_Parsers_0.1.0-dev.7.3.zip > Install Now.
4. Pilih Replace current with uploaded untuk AHDA Discovery Engine saja.
5. Pastikan Discovery aktif dan versi0.1.0-dev.7.3. Jangan mengganti Directory,
   uninstall Discovery, menghapus tabel, reimport atau membangun ulang indeks.
6. Local > AHDA > Open site shell. Jalankan kedua perintah berikut satu per satu:

```sh
wp --user="admin" ade pilot parse --format=csv --demo --dry-run
wp --user="admin" ade pilot parse --format=html --demo --dry-run
```

Hasil diharapkan: mode LOCAL_DOCUMENT_PARSE_PREVIEW, format sesuai perintah,
raw_document_sha256, structured_document, preview dengan3candidates,
preview.fixture_only true, network_requests0/database_writes0/publication_enabled
false. Kutipan mengacu pada teks hasil normalisasi, bukan byte HTML mentah.
Simpan file sumber asli beserta laporan/hash ketika nanti memakai dokumen nyata.
Demo2020/example.org tetap sintetis; blocker fixture/stale/identity/review adalah
pengaman yang diharapkan. Jangan mengubah flag demo atau menyalinnya ke profil.

Jika HTML mengembalikan M2_HTML_DOM_EXTENSION_REQUIRED, kirim pesan tersebut.
Itu berarti PHP DOM belum tersedia; CSV dan fitur lama tetap dapat dipakai.
Jangan mengunduh modul DLL acak atau mengubah database untuk memperbaikinya.

## Format dokumen dan batasan

Baca docs/M2_DOCUMENT_PARSER.md dalam ZIP untuk format/parameter lengkap. CSV
memerlukan header tepat npsn,target_key,value dan satu NPSN sekolah per dokumen.
HTML memerlukan satu tabel label/nilai yang jelas, dengan NPSN dan klaim dalam
tabel yang sama. Bukan semua layout website/katalog bisa dibaca adapter ini.
NPSN bertentangan, struktur ambigu, nilai konflik, formula CSV, deklarasi DTD/XXE,
markup berbahaya dan anggaran ukuran/kedalaman yang terlampaui diblokir.
CSS/JS/layout kompleks tidak dihitung; hasil tetap perlu pemeriksaan manusia.
Raw hash saat ini hanya di preview/report, belum kontrak arsip database.
URL/waktu/reference dari operator tidak membuktikan otoritas atau izin sumber.

## Bukti tes

18suite/945checks lulus masing-masing PHP8.2/8.4 dengan DOM sungguhan. Tanpa DOM:
892checks lulus masing-masing, HTML extraction NOT RUN dan guard diuji.60file PHP
lint tiap versi.88checks native MySQL8.4.13/PHP8.2 lulus termasuk parser->pending
writer->replay; WordPress/wpdb/preflight masih stub, bukan full LocalWP PASS.
Kedua container/storage uji sementara sudah dihapus.84baseline hashes dan6suite
regresi asli tidak berubah. Log, diff, security review dan checkpoint dalam
docs/qa/dev7.3 dan docs/PROGRESS.md. Versi7.3 LocalWP parser masih menunggu hasil
operator; jangan menganggap pengujian cloud membuktikan seluruh WordPress.

Jangan jalankan store atau unggah ke ahda.sch.id. Izin disposable MySQL tidak
mengizinkan penulisan LocalWP. Canonical/schema School/SEO frontend lama tidak
diubah; tidak menjanjikan ranking Google atau rekomendasi AI. Rollback file
Discovery ke7.2 tanpa migrasi, pertahankan semua data.

SHA-256 ZIP: 21d7791e0afc03d83637092ef4327ef9830205320217d87bf51153953504f9f9
