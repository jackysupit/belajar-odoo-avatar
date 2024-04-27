# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

"""
header 

detail 

"""



class Penjualan(models.Model):
    _name = 'oavatar.penjualan' 
    _description = 'Ini adalah transkasi penjualan'

    name = fields.Char('No Penjualan')

    """
        ondelete = restrict = jika sudah ada data penjualan milik Customer PT Andi Jaya
        maka, data master customer PT Andi Jaya tidak bisa dihapus 

        cascade = jika PT Andi Jaya dihapus, maka data transaksi otomatis dihapus juga 
    """
    # customer =  fields.Many2one(comodel_name='res.partner', ondelete='cascade')
    customer =  fields.Many2one(comodel_name='res.partner', ondelete='restrict')
    tgl = fields.Date()

    total = fields.Float()

    produk_ids = fields.One2many(comodel_name='oavatar.penjualan.produk', inverse_name='penjualan_id' )



class PenjualanProduk(models.Model):
    _name = 'oavatar.penjualan.produk' 
    _description = 'Ini adalah produk-produk yang dijual'

    # trans_id = field.header 
    penjualan_id = fields.Many2one(comodel_name='oavatar.penjualan', ondelete='restrict')

    produk_id = fields.Many2one(comodel_name='oavatar.produk', ondelete='restrict')
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

    """

