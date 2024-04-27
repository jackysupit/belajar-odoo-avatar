# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Siswa(models.Model):
    _name = 'osekolah.siswa' 
    _description = 'Ini adalah master siswa'

    name = fields.Char()
    jumlah_pelajaran = fields.Integer(string="Jumlah Pelajaran Yang Diambil")
    tinggi = fields.Integer()
    hoby = fields.Selection(string='Kesukannya apa?', selection=[
        ('makan', 'Makan'),
        ('nonton', 'Nonton'),
        ('mancing', 'Mancing'),
        ])

    keterangan = fields.Text(readonly=True, default='Ini defaultnya', store=True)

    harga = fields.Float("Harga Yang Disepakati Antara Siswa dan Sekolah")