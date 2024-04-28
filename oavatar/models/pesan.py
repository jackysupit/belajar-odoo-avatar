# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


"""
    models.Model adalah data yang akan dicommit ke dalam database, dan disimpan permanent 

    models.Transient adalah data yang akan disimpan di database, tapi akan otomatis di hapus oleh odoo, setiap periode tertentu. Sifatnya data sementara

"""


class Pesan(models.TransientModel):
    _name = 'oavatar.pesan' 
    _description = 'Ini adalah model khusus buat pesan'

    name = fields.Char(readonly=True, string="Pesan")