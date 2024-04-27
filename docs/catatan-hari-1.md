# Catatan Hari 1 #
*--------------------------------------------------------*

## membuat module baru
    - masuk ke menu apps -> update app list -> activate 

## membuat model baru
    - nama file sebaiknya sama dengan model
    - latihan: buat field name, harga, warna, keterangan 
    - set _name dan _description
    - masukkan __init__.py
    - set security/ir.model.access.csv

## mengenal macam2 field
    - char
    - integer
    - selection
    - many2one
    - one2many
    - many2many

## buat menu dari UI
    - biar tahu ada banyak cara di odoo

## buat menu dan view baru
    - perubahan XML, tidak perlu restart. tapi karena membuat data baru: perlu upgrade module 
    - sekalian belajar field widget: state, radio, tags

## one2many fields & views
    - latihan: membuat table transaksi penjualan
    - mode default
    - mode advanced: tree di dalam field

## many2one fields & views
    - mode default
    - mode advanced: allow create / update

## dynamic view
    - mengenal attributes
    - mengenal decoration di dalam tree

## computed fields
    - latihan: buat field subtotal
    - field yang otomatis
    - sifatnya readonly

## related fields
    - latihan: buat field harga related ke produk.harga
    - field yang otomatis
    - sifatnya readonly

## py store=True
    - defaultnya field related dan computed tidak akan disimpan di db
    - memaksa field ini disimpan di db, jadi bisa dipakai untuk filter & group

## xml force_save
    - defaultnya: field readonly tidak akan disipan di db
    - memaksa field ini disimpan di db

## auto sequence
    - tambahkan kode_barang di model produk
    - buat master sequence di xml
    - deklarasi field, kasih default value
    - waktu data di create, set kode_barangnya

## multi column group view
    - group sama seperti bootstrap css grid, bedanya hanya 2 kolom
    - ada opsi: col