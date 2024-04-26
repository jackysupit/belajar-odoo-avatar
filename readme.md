*------------------------------------------------------------* 
## Panduan Programming Odoo
*------------------------------------------------------------* 

1. Setiap perubahan di python, harus direstart
2. Perubahan di XML, biasanya cukup hard reset views
3. Penambahan record di XML, biasanya butuh upgrade module
4. Backup / restore database ada di /web/database/manager
5. Naming convention untuk variable menggunakan snake_case underscode: contohnya_seperti_ini
6. Naming conevntion untuk class, gunakan CamelCase
7. Naming convention untuk file, gunakan underscore.ext
8. Gunakan ChatGPT dulu sebelum googling
9. Rekomendasi gunakan vscode dengan odoo extention, dan masukkan folder odoo ke workspace
10. Untuk relasi many2one biasanya menggunakan nama_field + _id, contoh: customer_id, vendor_id, product_id, dsb
11. Untuk relasi one2many dan many2many, biasanya menggunakan nama_field  + _ids, contoh: customer_ids, vendor_ids, product_ids, dsb
12. rekomendasi gunakan spaces 4
13. programming itu menyenangkan, hanya jika menggunakan odoo. :))
