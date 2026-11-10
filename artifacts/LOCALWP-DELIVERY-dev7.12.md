# AHDA Discovery Engine 0.1.0-dev.7.12 — pemeriksaan ikatan raw

Fitur baru membaca ulang satu bukti tersimpan dan mencocokkannya dengan raw:
NPSN, nilai kandidat, kutipan, hash dokumen/payload, waktu, URL dan relasi sumber.
Hasil cocok tetap **bukan persetujuan/izin/verifikasi identitas sumber**. Layanan
ini baca-saja; tidak mengubah profil, status review atau database.

## Unduh

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/raw-check-dev7.12/artifacts
2. Klik `AHDA_Discovery_Engine_Raw_Check_0.1.0-dev.7.12.zip`.
3. Klik **Download raw file**/ikon unduh, bukan Code > Download ZIP.
4. Simpan ZIP; untuk upload WordPress tidak perlu diekstrak.

SHA-256: `28e2299988fb12fd21f72dd39f3de9e4ec78c9b2adeb70726a2fc4f7c6f5e05a`.

## Memasang (opsional, hanya ahda.local)

Tidak perlu mengulang demo lama atau membuat data hanya untuk mencoba fitur.
Anda boleh menyimpan paket ini dahulu selama pengembangan berlanjut.

1. Di Local pilih **ahda > Start site**, backup folder plugin/situs lokal dahulu.
2. **WP Admin**, login admin.
3. **Plugins > Add New Plugin > Upload Plugin > Choose File**.
4. Pilih ZIP7.12 > **Install Now > Replace current with uploaded** jika diminta.
5. Ganti AHDA Discovery Engine saja; Directory0.8.9 tetap.
6. Aktifkan companion jika diperlukan. Jangan mengaktifkan write/crawler/publisher atau mengubah wp-config.php.

Tidak ada migration/tabel/role/options baru atau import/delete profil. Jangan
unggah ke ahda.sch.id melalui WinSCP. Rollback memakai backup lokal tanpa menghapus
tabel. Tautan branch lama pada dokumentasi historis ZIP mungkin sudah dibersihkan;
daftar aktif GitHub hanya paket terbaru dan satu panduan.

## Memakai verifier bila sudah ada record sah

Pada SiteShell lokal, command baru bernama **archive_verify** (underscore):

```bat
wp --user="admin" ade pilot archive_verify --npsn=NPSN_PILIHAN --candidate-id=ID_KANDIDAT --evidence-id=ID_BUKTI --dry-run
```

Ganti placeholder dengan ID/NPSN actual yang tersimpan dan berelasi di sekolah
sama. Demo sebelumnya tidak disimpan, sehingga tidak perlu menjalankan contoh
ini sekarang bila belum ada record. Jangan memaksa demo menjadi non-fixture.

Hasil normal: mode READ_ONLY_ARCHIVE_BINDING_CHECK, binding_matches true,
ready_for_approval false, identity_attested false, permission_attested false,
publication_enabled false dan write/network0. Raw/kutipan tidak disalin ke output.
Current_value_conflict dan stale tetap menjadi penahanan. Jika bukti berubah,
raw/hash/value tidak cocok atau sumber blocked, command menolak dengan kode error.

Hasil adalah snapshot, bukan token approve atau jaminan kondisi tetap sama.
Persetujuan/publisher masa depan wajib memeriksa ulang dalam transaksi. Admin page
tidak otomatis mem-parse raw, sehingga tetap ringan; notice raw belum diperiksa
ulang pada halaman itu tetap benar. Detail docs/RAW_BINDING_CHECK.md dalam ZIP.

## Bukti tes

- 25suite/1545checks lulus masing-masing PHP8.2 dan8.4 dengan DOM.
- 1477tanpaDOM; ekstraksi HTML tidak dijalankan dalam konfigurasi tersebut.
- 85filePHP lint,84hash baseline dan6regresi asli tetap utuh.
- 96pemeriksaan layanan actualWordPress/wpdb +47browser/admin checks pada MySQL8.4 sintetis; seluruh25tabel lama sintetis tetap utuh.
- Pengubahan kutipan, hash, source blocked, actor/IDOR dan snapshot drift diuji.
- UjiWordPress pertama gagal login timeout30s; bukti FAIL disimpan. Dua situs baru berikutnya lulus96+47 dengan logPHP bersih. Penyebab timeout pertama belum terbukti.
- Semua3container/situs/server uji sendiri dihapus. Tidak ada database pengguna, wp-config atau operasi produksi disentuh.

ActualWordPress harness memakai service API langsung dan CLI class-presence
marker untuk modul write lama; officialWPCLI runner lengkap dan LocalWP Anda
belum diuji end-to-end. Ini juga bukan uji beban VPS atau sumber faktual nyata.
Log/diff ada docs/qa/dev7.12; checkout/tes/progres dalam docs/PROGRESS.md.

Penyimpanan dan publikasi tetap defaultOFF. Fondasi MVP masih perkiraan~55%;
pengayaan fakta nyata0/200. Tahap selanjutnya source/identity/permission attestation
serta review positif yang memakai pemeriksaan raw segar, lalu worker/publisher
lokal berizin dengan rollback. Tidak menjanjikan ranking Google/rekomendasiAI.
