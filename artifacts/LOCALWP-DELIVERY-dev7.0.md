# dev.7.0 — M2 preview sintetis, bukan pengayaan profil nyata

Paket ini melanjutkan pengembangan offline selama akses katalog cloud terblokir.
M2 awal: validator dokumen evidence dan pratinjau kandidat3 meta fields, tanpa
penyimpanan/approval/publish. Tidak ada hasil crawl atau fakta sekolah baru.
SHA-256 ZIP: ff07026965badf7da1d1c2e57d4f93678ee014f1c581585de60eab173b70c187.

Jika ingin menguji modul baru, setelah backup dan persetujuan pemasangan lokal:
1. Buka Local > AHDA > WP Admin, pastikan situs ahda.local.
2. Plugins > Add New > Upload Plugin > pilih ZIP dev.7.0 > Install Now.
3. Replace current with uploaded untuk AHDA Discovery Engine saja. Directory tetap.
4. Pastikan versi0.1.0-dev.7.0. Buka Open site shell AHDA dan jalankan:

```sh
wp --user="admin" ade pilot extract --demo --dry-run
```

Hasil yang diharapkan: FIXTURE_ONLY_READ_ONLY, fixture_only=true,3 preview
candidate/evidence, semua persisted=false, approved_value=null, publication false,
zero network/write. Demo memakai NPSN20268071 untuk binding sekolah lokal saja;
program/kurikulum/jam adalah CONTOH SINTETIS dan tanggal lama. Jangan menyalin
nilai demo ke profil. Kirim output untuk bukti uji native. Nama command `extract`
satu kata; alias hyphen/underscore reader lama tetap dipertahankan.

14 suite offline lulus PHP8.2/8.4,580 checks masing-masing;43 PHP files lint.
Native M2 di LocalWP belum diuji. Dokumen nyata baru dapat dipreview setelah
sumber berizin tersedia; parser HTML/CSV, persistence, review dan publisher
belum selesai. Baca docs/M2_PREVIEW.md dalam ZIP. Tidak untuk produksi.
Rollback ke dev6.2.1 tidak perlu perubahan database atau penghapusan baris.

Source research: izin operator sudah ada, tetapi dua domain katalog belum masuk
allowlist cloud: referensi.data.kemendikdasmen.go.id dan referensi.data.kemdikbud.go.id.
Tidak ada request ulang;18 dari20 anggaran tersisa. Memasang plugin ini tidak
mengubah akses jaringan cloud; pengguna source_preview dev6.2 tidak perlu upgrade
hanya untuk melanjutkan riset. Semua persetujuan DB/jaringan/publikasi tetap berlaku.
