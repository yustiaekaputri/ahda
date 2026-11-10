# AHDA Discovery Engine 0.1.0-dev.7.11 — hasil integrasi WordPress

Perkiraan fondasi kode MVP saat ini **sekitar55%**, berdasarkan milestone dan
bukan hasil ukur otomatis. Pengayaan fakta nyata melalui mesin: **0/200profil**.
Daftar kriteria menuju selesai ada pada docs/MVP_ACCEPTANCE.md dalam ZIP.

7.11 menambah bukti integrasi aktualWordPress, tanpa perubahan logika runtime
selain nomor versi. Seluruh write/crawler/publisher tetap nonaktif pada situs Anda.
Tidak perlu mengulang demo inspect/batch sebelumnya atau menjalankan mutasi baru.

## Unduh

1. Buka https://github.com/yustiaekaputri/ahda/tree/delivery/wp-bridge-dev7.11/artifacts
2. Klik `AHDA_Discovery_Engine_WP_Bridge_0.1.0-dev.7.11.zip`.
3. Klik **Download raw file**/ikon unduh, bukan Code > Download ZIP.
4. Simpan ZIP; upload lewat WordPress tidak perlu diekstrak.

SHA-256: `d5ccceec287b9c4ad94dca3ef0f489b3727ada2b0fe1a5f85681ee8539001ae8`.

## Memasang (opsional, hanya ahda.local)

Karena ini pembuktian integrasi dan runtime sama dengan7.10, paket boleh disimpan
dahulu sambil melanjutkan pengembangan. Tidak perlu segera memperbarui situs Anda.

1. Di Local pilih **ahda > Start site** dan buat backup situs/folder plugin lokal.
2. **WP Admin**, login admin.
3. **Plugins > Add New Plugin > Upload Plugin > Choose File**.
4. Pilih ZIP7.11 > **Install Now** > **Replace current with uploaded** jika diminta.
5. Ganti companion AHDA Discovery Engine saja; Directory0.8.9 tetap.
6. Aktifkan companion jika diperlukan. Jangan mengaktifkan flag write/network/publisher atau mengubah wp-config.php.

Tidak ada migrasi/schema/role/opsi baru, import atau penghapusan profil. Jangan
unggah ke ahda.sch.id/produksi dengan WinSCP. Rollback menggunakan backup lokal
sebelum update, tanpa menghapus tabel. Tautan branch lama dalam dokumentasi
historis ZIP mungkin sudah dibersihkan; daftar aktif GitHub hanya paket terbaru
beserta panduan ini. Riwayat Git dan cadangan pengembangan tetap ada.

## Bukti baru

- **83 pemeriksaan layanan** dengan WordPress7.1.4, Directory0.8.9, realwpdb/capability dan MySQL8.4.13 sementara.
- **47 pemeriksaan browser/admin** menggunakan login/session/nonce/admin-post dan halaman WordPress nyata.
- Semua **25tabel legacy sintetis** tetap sama hash-nya; raw archive tidak berubah ketika kandidat dibuat.
- Diuji16posisi kegagalan insert: actualWP queryfilter membuat realMySQL menolak satu INSERT, lalu seluruh row operasi di-rollback.
- Two-source evidence, rawhash pointer, exact replay, pending revision/version dan reviewed freeze diuji; skor/approval/publish tidak dipromosikan.
- Final log PHP bersih. Uji awal punya3peringatan updateCore yang ditahan oleh network guard; harness khusus diperbaiki dan tes diulang.
- Dua database/site/server uji sendiri sudah dihapus. Tidak ada wp-config pengguna dibaca/diubah atau sumber sekolah nyata diambil.

Layanan dipanggil langsung sesudah WordPress dimuat. Harness memakai marker
keberadaan classWP_CLI untuk guard; **bukan tes end-to-end official WP-CLI runner**.
Parser/dispatcher official2.12 tetap diuji secara offline. Custom testbootstrap/
homealias/loopback dibedakan dari LocalWP Anda; tidak mengklaim semua plugin/theme
pihak ketiga atau beban VPS sudah teruji.

Offline24suite1504checks tiap PHP8.2/8.4 dengan DOM,1436tanpaDOM (HTML NOT RUN),
82filePHP lint,84hash baseline dan6regresi asli utuh. Log/diff/screenshots dalam
`docs/qa/dev7.11`; scope lengkap `docs/WORDPRESS_ARCHIVE_BRIDGE.md`.

## Pekerjaan yang masih perlu diselesaikan

Sumber nyata berizin dan pembuktian identitas/permission, verifikasi raw penuh
pada review, approval positif/edit, worker durable dengan lease/checkpoint commit,
publisher lokal serta rollback dan frontend/resource acceptance masih perlu
pekerjaan. Retensi/privacy raw juga belum siap untuk data nyata. Tidak ada200profil
faktual lengkap atau jaminan ranking Google/rekomendasiAI. Produksi tetap excluded.
