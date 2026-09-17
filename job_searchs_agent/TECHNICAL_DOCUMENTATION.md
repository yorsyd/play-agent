=== JOB SEARCH AGENT===
---
Definisi:
Sebuah agen yang berfungsi untuk mencarikan lowongan pekerjaan diinternet dengan melihat kecocokan cv dan referensi pekerjaan yang diinginkan oleh user.
---
Alur Kerja:
1. User memasukkan prompt dan file cv 
2. Agen menerima kueri dan memastikan apakah referensi serta cv telah dikirimkan. Jika belum, maka agen akan meminta kepada user untuk mengirimkan hal tersebu 
3. Setelah dipastikan bahwa terlampri cv dan referensi kerja, agen menggunakan tool 'read_cv_file" untuk membaca cv dan mengekstrak informasi
4. Hasil dari membaca cv dan referensi kerja digunakan untuk mencari lowongan pekerjaan di internet yang sesuai dengan kueri yang dimasukkan menggunakan tool 'search_job_postings'
5. Kemudian agen memfilter lowongan sebanyak N menggunakan tool 'calculate_match_score', sehingga didapat lowongan pekerjaan yang benar-benar cocok (lowongan dengan skor => 70% berarti cocok)
6. Setelah beberapa lowongan pekerjaan yang sesuai berhasil ditemukan, agen membuat rangkuman dan menyimpannya dengan tool 'save_summary_recomendation_jobs'
7. Agen memberikan ringkasan pekerjaan yang ditemukan kepada user
---
Tools:
1. read_cv_file(file_path: str)
- Fungsi: membaca file dari dokumen CV (PDF/docs)
- Output: String lengkap CV
2. search_job_postings(job_preference: str, location_preference: str)
- Fungsi: Mencari pekerjaan yang sesuai dengan kueri (dokumen cv dan referensi kerja)
- Output: List Dict yang berisi detail lowongan (nama pekerjaan, gaji, lokasi, perusahaan, skill yang dibutuhkan, deskripsi, link)
3. save_summary_recomendation_jobs(filename: str, report_markdown: str)
- Fungsi: membuat ringkasan dan menyimpan daftar pekerjaan yang didapat
- Output: file dengan format yang diinginkan user, default-nya .md
4. calculate_match_score(cv_text: str, job_detail: str)
- Fungsi: Mengukur kecocokan cv dengan lowongan pekerjaan yang ditemukan
- Output: JSON berisi score, matching_skills, dan missing_skills
