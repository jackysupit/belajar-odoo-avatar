# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Produk(models.Model):
    #nama id model, nama id ini akan otomatis digenerate menjadi table di database
    _name = 'oavatar.produk' 

    #ini adalah keterangan modelnya
    _description = 'Ini adalah master produk'

    #ini untuk memaksa odoo, jangan pakai field name, tapi field no_transaksi
    _rec_name = "no_transaksi"

    #nama di odoo = name 
    no_transaksi = fields.Char()

    name = fields.Char('Nama Produk', required=True)

    harga = fields.Float()

    # untuk status, biasanya namanya state 
    state = fields.Selection(string='Status', selection=[
        ('good', 'Good'),
        ('bad', 'Bad'),
    ])

    notes = fields.Text(readonly=True)


