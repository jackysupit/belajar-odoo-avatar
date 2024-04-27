# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime, timedelta

"""
header 

detail 

"""



class Penjualan(models.Model):
    _name = 'oavatar.penjualan' 
    _description = 'Ini adalah transkasi penjualan'

    """
        convention odoo 
        biasanya jika membuat auto sequence 
        bikin field = default value = New 
        readonly 
        store ke database 
    """
    name = fields.Char('No Transaksi', default = "New", readonly=True, store=True)

    notes = fields.Text(default="ini adalah value default untuk field: notes")
    
    #misal tgl default adalah hari ini
    #misal tanggal kirim adalah hari ini + 3 hari 
    def default_tgl(self):
        tgl = fields.Date.today()
        return tgl

    # def default_tgl_kirim(self):
    #     tgl = fields.Date.today()
    #     tgl_kirim = tgl + timedelta(days=3)
    #     return tgl_kirim

    tgl = fields.Date(default=fields.Date.today())
    tgl_kirim = fields.Date(default=datetime.today() + timedelta(days=3))

    # tgl = fields.Date(default='default_tgl')
    # tgl_kirim = fields.Text(default='default_tgl_kirim')

    """
        ondelete = restrict = jika sudah ada data penjualan milik Customer PT Andi Jaya
        maka, data master customer PT Andi Jaya tidak bisa dihapus 

        cascade = jika PT Andi Jaya dihapus, maka data transaksi otomatis dihapus juga 
    """
    # customer =  fields.Many2on(comodel_name='res.partner', ondelete='cascade')
    customer_id =  fields.Many2one(comodel_name='res.partner', ondelete='restrict')

    total = fields.Float(compute="compute_total", store=True)
    #default value 
    
    
    @api.depends('produk_ids')
    def compute_total(self):
        for record in self:
            total = 0
            for produk in record.produk_ids:
                # total = total + produk.subtotal
                total += produk.subtotal

            record.total = total

    produk_ids = fields.One2many(comodel_name='oavatar.penjualan.produk', inverse_name='penjualan_id' )


    # pas di klik save untuk create new 
    #vals = adalah semua value yang akan disimpan ke dalam datbase 
    """
        bentuknya object 

        contoh: 

        {
            'name': 'Apel',
            'harga': 5000,
        }
    """
    @api.model
    def create(self, vals):
        # Agregar codigo de validacion aca
        
        #versi php: if (isset($vals["nae"])) {}
        #versi python:  if 'name' in vals:

        """
            jika vals['name'] == '' atau vals['name'] == 'New'
                maka ganti vals['name'] = dengan auto sequence 
        """
        if vals.get('name') != '' or vals.get('name') == 'New':

            # Ambil tanggal hari ini dalam format yyyymmdd
            tanggal_hari_ini = datetime.today().strftime('%Y%m%d')
            name  = self.env['ir.sequence'].next_by_code('penjualan_seq') 

            # vals['name'] = name + tanggal_hari_ini
            vals['name'] = "{}-{}".format(name, tanggal_hari_ini)

        return super(Penjualan, self).create(vals)


    # pas di klik save, untuk edit 
    def write(self, vals):
        # Agregar codigo de validacion aca
        
        return super(Penjualan, self).write(vals)



class PenjualanProduk(models.Model):
    _name = 'oavatar.penjualan.produk' 
    _description = 'Ini adalah produk-produk yang dijual'

    # trans_id = field.header 
    penjualan_id = fields.Many2one(comodel_name='oavatar.penjualan', ondelete='restrict')

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

    """

