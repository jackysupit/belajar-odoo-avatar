# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

"""
    Ini digunakan untuk mencatat, siswa siapa saja yang mau membeli seragam 
    cara kerjanya 

    1 transksi 
    banyak siswa yang akan membeli seragam 

    contoh:
    no: TRANS-001
    tgl: 01-01-2024
    total: 50.000

    detail:
        no      | nama          | Qty       | Harga         | subtotal
        1       | Andi          | 2         | 10.000        | 20.000
        2       | Budi          | 3         | 10.000        | 30.000
"""
class Penawaran(models.Model):
    _name = 'osekolah.penawaran' 
    _description = 'ini model untuk melakukan penawaran oleh siswa'


    name = fields.Char(string='No Transaksi')
    tgl = fields.Date()
    total = fields.Float(compute="compute_total", store=True)

    @api.depends('detail_ids')
    def compute_total(self):
        for record in self:
            total = 0
            for detail in record.detail_ids:
                total = total + detail.subtotal

            record.total = total
    


    detail_ids = fields.One2many('osekolah.penawaran.detail', 'penawaran_id', string='Detail')


class PenawaranDetail(models.Model):
    _name = 'osekolah.penawaran.detail' 
    _description = 'ini model detail untuk melakukan penawaran oleh siswa'

    penawaran_id = fields.Many2one(string='', comodel_name='osekolah.penawaran', ondelete='restrict')


    siswa_id = fields.Many2one(comodel_name='osekolah.siswa', ondelete='restrict')
    # siswa_id = fields.Many2one(comodel_name='osekolah.siswa', ondelete='cascade')

    #ini harusnya otomatis ambil dari siswa
    harga_detail = fields.Float(string='', related="siswa_id.harga", store=True)

    qty = fields.Integer(string='')
    subtotal = fields.Float(string='', compute="compute_subtotal", store=True)

    @api.depends('qty', 'harga_detail')
    def compute_subtotal(self):
        for record in self:
            record.subtotal = record.qty * record.harga_detail




