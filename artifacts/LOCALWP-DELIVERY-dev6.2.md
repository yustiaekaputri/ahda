# dev.6.2 — pemeriksaan URL lokal

Download ZIP dev.6.2 di direktori ini. SHA-256: e865873d38a14d475ce451cd75e0675c9d44b9fb6e5c5b42cb1329875ffdda81.

Hasil yang sudah diterima dari LocalWP dev.6.1: schema INSTALLED7/7, pilot200/200
lolos, preview10 berjalan. needs_source berarti belum ada link Discovery, bukan
bukti tidak ada website. Tidak perlu menjalankan ulang pemeriksaan yang lulus.

1. Pastikan backup LocalWP tersedia. Masuk WP Admin situs ahda.local.
2. Plugins > Add New > Upload Plugin. Pilih ZIP dev.6.2 > Install Now.
3. Pilih Replace current with uploaded untuk AHDA Discovery Engine saja.
4. Pastikan versi0.1.0-dev.6.2 di Installed Plugins; pertahankan Directory v0.8.9.
5. Buka Open site shell di aplikasi Local, pilih situs AHDA, jalankan:

```sh
wp --user="admin" ade pilot source-preview --batch-size=10 --dry-run
```

Kirim hasilnya. Perintah hanya membaca field URL verified lokal, tidak fetch,
mendaftarkan sumber atau mengubah database. Petunjuk URL tetap pending/manual_only.
Jika ada error, berhenti dan kirim kode error. Jangan enqueue/crawl/publish dulu.
Skema tetap1, tidak perlu schema install atau reimport. Jangan unggah ke produksi.
Build ini belum diuji native source-preview-nya pada database Anda;13 suite
offline lulus pada PHP8.2/8.4,512 checks per runtime. Rincian dan checkpoint
kelanjutan tersedia dalam docs di dalam ZIP. Rollback dev.6.1 tidak perlu migrasi.
