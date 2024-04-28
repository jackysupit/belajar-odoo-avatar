# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime, timedelta

"""
header 

detail 

"""



class PenjualanProduk(models.Model):
    _name = 'oavatar.penjualan.produk' 
    _description = 'Ini adalah produk-produk yang dijual'

    # trans_id = field.header 

    #restric = jika sudah ada data ini, maka data penjualan tidak akan bisa dihapus
    penjualan_id = fields.Many2one(comodel_name='oavatar.penjualan', ondelete='restrict')
    
    #cascade, waktu data penjualan dihapus, maka record ini juga akan dihapus
    # penjualan_id = fields.Many2one(comodel_name='oavatar.penjualan', ondelete='cascade')

    produk_id = fields.Many2one(comodel_name='oavatar.produk', ondelete='restrict')

    state = fields.Selection(string='Status', selection=[
        ('good', 'Good'),
        ('bad', 'Bad'),
    ], related="produk_id.state")


    qty = fields.Integer()
    
    """
        harga_transaksi = otomatis ikut harga produk
    """
    harga_transaksi = fields.Float(related="produk_id.harga", store=True)

    """
        subtotal = otomatis harga x qty 
    """
    subtotal = fields.Float(compute="compute_subtotal", store=True)

    """
         self = context milik class ini, isinya selalu adalah array[record]
         walaupun hanya 1, tetep bentuknya array 
         tapi kelebihan di odoo, kalau ada data model array, isinya hanya 1, otomatis bisa kita perlakukan seperti object 

         contoh:
            rec = record produk mangga 
                print(rec.name) # mangga 

            rec = multi record produk mangga dan apel 
                for satu in rec:
                    print(satu.name) # mangga, apel 
    """

    @api.depends('qty', 'harga_transaksi')
    def compute_subtotal(self):
        print("nama model = ", self._name)
        print("nama description = ", self._description)

        for record in self:
            record.subtotal = record.qty * record.harga_transaksi


    """
        field related dan compute 
        - otomatis readonly 
        - tidak tersimpan di database 
            - tidak bisa digunakan untuk filter, search, group by 

        store=True

    """




    # Method to open the popup form
    def open_popup_form(self):
        return {
            'name': 'Berhasil',
            'type': 'ir.actions.act_window',
            'res_model': 'oavatar.pesan',  # Ganti dengan nama model Anda
            'view_mode': 'form',    # mode form, bukan tree
            'target': 'new',    # akan muncul di popup
        }

