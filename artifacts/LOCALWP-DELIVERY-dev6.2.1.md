# dev.6.2.1 — hotfix nama perintah

Underscore source_preview sudah berhasil pada LocalWP dev.6.2 Anda:
```sh
wp --user="admin" ade pilot source_preview --batch-size=10 --dry-run
```
Tidak perlu memasang ulang untuk melanjutkan. Hotfix opsional ini menambahkan
alias source-preview, run-one-batch, integrity-check, retry-failed; nama underscore
lama dipertahankan. Tidak ada perubahan query/database/schema/flags/crawler.

Jika memilih memasang: backup LocalWP, WP Admin lokal > Plugins > Add New > Upload
Plugin > pilih ZIP dev.6.2.1 > Install > Replace current untuk Discovery saja.
Directory tetap. `wp help ade pilot` dapat melihat alias; native LocalWP alias
belum diuji.13 suite offline/520 checks per PHP8.2 dan PHP8.4 lulus.
SHA-256 ZIP: 38862d3ffdb0ec64c2bdec62ebc4fd87104ac3d00b226ced969b991615d4aff3.

Hasil source preview hanya10 sekolah pertama: belum ada URL verified pada field
yang diperiksa. Bukan bukti seluruh200 tidak punya website. Jangan membuat job
kosong untuk mengatasi sumber yang belum tersedia.

Operator sudah menyetujui riset katalog terbatas; cloud proxy menolak CONNECT
untuk dua domain. Tambahkan hanya domain berikut pada pengaturan akses jaringan
lingkungan cloud, pertahankan semua izin yang sudah ada:
- referensi.data.kemendikdasmen.go.id
- referensi.data.kemdikbud.go.id
Tidak perlu mengubah VPS/WordPress atau memberi password. Jangan membuka akses
internet tanpa batas.2 request dari batas20 sudah dipakai;18 tersisa. Tidak ada
crawl berhasil, perubahan profil atau publikasi. Produksi tetap tidak disentuh.
