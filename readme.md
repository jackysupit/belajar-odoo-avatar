## <span style="color:green;"># Panduan Programming Odoo #</span>
###### waktu baca: 5 menit

### <span style="color:yellowgreen;"># Cara Kerja Odoo</span>

1. Setiap perubahan di python, harus direstart
2. Perubahan di XML, biasanya cukup hard reset views
3. Penambahan record di XML, biasanya butuh upgrade module
    - Jika hanya mengupdate merubah design, cukup Hard Reset
    - Jika membuat view baru, perlu Upgrade Module
4. Backup / restore database ada di /web/database/manager

### <span style="color:yellowgreen;"># Convention</span>
1. Naming convention untuk variable menggunakan snake_case: contohnya_seperti_ini
2. Naming convention untuk class, gunakan CamelCase
3. Naming convention untuk file, gunakan under_score.ext
4. Nama model biasanya menggunakan Double Quote <br/>
    contoh: _name = "nama_module.nama_table"
5. Inherit table biasanya menggunakan Single Quote <br/>
    contoh: _inherit = 'nama_module.nama_table'
6. Rekomendasi gunakan spaces 4

### <span style="color:yellowgreen;"># Tips</span>
1. Gunakan git untuk bekerja, titik.
    - repo ini ada di: https://github.com/jackysupit/belajar-odoo-avatar.git
2. Gunakan ChatGPT dulu sebelum googling
3. Rekomendasi gunakan vscode dengan odoo extension, dan masukkan folder odoo ke workspace
    - Odoo.odoo
    - trinhanhngoc.vscode-odoo
    - jigar-patel.OdooSnippets

### <span style="color:yellowgreen;"># Cheat Sheet</span>
1. Untuk relasi many2one biasanya menggunakan nama_field + _id, contoh: customer_id, vendor_id, product_id, dsb
2. Untuk relasi one2many dan many2many, biasanya menggunakan nama_field  + _ids, contoh: customer_ids, vendor_ids, product_ids, dsb


### <span style="color:yellowgreen;"># Tentang Training Odoo</span>
1. Memperhatikan lebih baik daripada nyoba-nyoba
2. Kelas akan berjalan dengan sangat cepat, karena kita enggak punya waktu banyak. Jika mencatat membuatmu ketinggalan, tidak bisa memperhatikan dengan baik, lebih baik tidak usah mencatat. Perhatikan saja. Nanti cukup clone repo, coba-coba sambil nyontek contoh yang sudah dibuat. Kalau bingung silahkan konsultasi via WA ***(bikin group WA, biar 1x jawab, semua memperhatikan)***

### <span style="color:yellowgreen;"># Wisdom</span>
1. programming itu menyenangkan, jika menggunakan odoo. :))
