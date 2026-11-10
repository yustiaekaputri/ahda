# AHDA Discovery Engine 0.1.0-dev.7.7 — panduan LocalWP

Pembaruan ini menambah worker **pratinjau offline** yang dapat dilanjutkan dari
checkpoint, pemeriksaan hash dokumen, serta penahanan klaim antarsumber yang
bertentangan. Isi demo sintetis. Belum menambah fakta/artikel pada profil sekolah.
Crawler, persetujuan positif, dan publisher tetap belum aktif.

## Unduh dari GitHub

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/local-worker-dev7.7/artifacts
2. Klik `AHDA_Discovery_Engine_Local_Worker_0.1.0-dev.7.7.zip`.
3. Pada halaman file, klik **Download raw file** (ikon unduh). Jangan pilih Code > Download ZIP karena itu mengunduh seluruh repositori.
4. Simpan ZIP di komputer. Jangan ekstrak untuk metode upload WordPress berikut.

SHA-256 ZIP: `399ed70b880e1b7d490646cda2f8e8dc1d807f4e3af325e6275f4513bd0d421b`.

## Memasang di situs lokal

Tidak perlu mengulang semua demo versi sebelumnya. Pemasangan ini opsional untuk
menguji fitur baru. Gunakan **ahda.local**, jangan ahda.sch.id/WinSCP produksi.

1. Di aplikasi Local, pilih **ahda** > **Start site**.
2. Buat backup/salinan situs lokal terlebih dahulu menggunakan cara backup Anda.
3. Klik **WP Admin**, masuk sebagai admin.
4. Buka **Plugins > Add New Plugin > Upload Plugin > Choose File**.
5. Pilih ZIP7.7 di atas > **Install Now**.
6. Jika WordPress mendeteksi plugin lama, pilih **Replace current with uploaded**.
7. Pastikan hanya AHDA Discovery Engine yang diganti; AHDA School Directory0.8.9 tetap.
8. Aktifkan companion jika sebelumnya nonaktif; jangan mengaktifkan flag write/network/publisher atau mengubah wp-config.php.

Folder root ZIP adalah `ahda-discovery-engine/`. Tidak ada migrasi skema/tabel atau
perubahan role/opsi baru. Fitur penolakan/tunda tulis tetap OFF sesuai versi lama.

## Coba satu batch opsional

Di Local > ahda > **Open Site Shell**, jalankan:

```bat
wp --user="admin" ade pilot work --demo --batch-size=10 --dry-run
```

Hasil normal: mode `READ_ONLY_LOCAL_BATCH_PREVIEW`, cursor10, processed_this_call10,
database_writes0, network_requests0, filesystem_writes0, publication_enabled false.
Semua contoh **bukan fakta sekolah**. Jika DOM tersedia dan identitas200 tetap cocok,
10sekolah awal menghasilkan1preview,1konflik,1dokumen salahNPSN,7needs_source.
Urutan worker ini berdasarkan NPSN, berbeda dari urutan school_id pada preview lama.
Jika identitas tidak cocok, identity_blocked adalah penahanan aman; jangan dipaksa.

## Coba melanjutkan checkpoint

Simpan laporan di luar folder public. Contoh Windows CMD:

```bat
mkdir "C:\Users\user\Documents\AHDA-preview"
wp --user="admin" ade pilot work --demo --batch-size=10 --dry-run > "C:\Users\user\Documents\AHDA-preview\batch-01.json"
wp --user="admin" ade pilot work --demo --checkpoint-file="C:\Users\user\Documents\AHDA-preview\batch-01.json" --batch-size=10 --dry-run > "C:\Users\user\Documents\AHDA-preview\batch-02.json"
```

Periksa output pertama sebelum menjalankan yang kedua; kedua normalnya cursor20.
Jangan memakai nama output yang sama dengan file checkpoint input: shell akan
mengosongkannya sebelum dibaca. Simpan setiap laporan karena results hanya batch
saat itu; checkpoint berisi ringkasan/hash, bukan seluruh teks kandidat lama.
CLI sendiri tidak menyimpan file; tanda `>` adalah penyimpanan oleh shell Anda.
Jangan simpan dokumen privat/report fakta nyata di GitHub atau folder web publik.

Tidak perlu menjalankan20batch demo hanya untuk membuktikan fitur. Uji otomatis
sudah memeriksa resume sampai200. complete=true berarti200**diperiksa**, bukan200
profil lengkap. Checkpoint bukan bukti approval/commit dan tidak bisa dipakai
untuk mengesahkan penyimpanan/publikasi. Jangan jalankan stage/store/publish dari
demo. Lihat `docs/LOCAL_ARCHIVE_WORKER.md` dalam ZIP untuk format dan batas lengkap.

## Bukti dan batas pengujian

- 21suite/1230pemeriksaan lulus masing-masing PHP8.2 dan8.4 dengan DOM.
- 1166pemeriksaan tanpaDOM; ekstraksi HTML tidak dijalankan dalam konfigurasi itu.
- 74filePHP lint;84hash baseline serta6file tes asli tetap sama.
- Official WP-CLI2.12 parser/dispatcher diuji memakai facade WP/fakeDB, termasuk pembacaan file dan resume.
- Benchmark sintetis cloud:arsip3,3MB/batch10HTML,0,423detik,peakPHPsekitar14MB. Ini bukan sertifikasi beban VPS.
- Worker baru **belum diuji pada WordPress/LocalWP Anda**. Bukti39pemeriksaan WordPress nyata dari7.6 tetap berstatus versi sebelumnya.

Bukti lengkap/log/diff tersedia di folder `docs/qa/dev7.7` dalam ZIP.
Tidak ada permintaan sumber sekolah atau perubahan database nyata sesi7.7.
Akses katalog resmi masih terbatas kebijakan jaringan cloud. Belum ada200artikel
faktual lengkap, dan tidak ada janji peringkat Google/rekomendasiAI.

Rollback: ganti folder plugin dengan ZIP7.6 dari branch `delivery/wp-validation-dev7.6`.
Tidak perlu menghapus tabel atau mengimpor ulang sekolah. Simpan arsip/report Anda.
Langkah pengembangan berikutnya adalah menghubungkan arsip sumber sah ke evidence
pending dengan persetujuan terpisah, lalu worker transaksi dan publisher lokal.
