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

    notes = fields.Text()
    notes2 = fields.Text()
    
    
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

        produk_id = 1
        produk = self.env['oavatar.produk'].browse(produk_id)
        produk.notes = 'do something'

        """
            beberapa cara meng-edit data di odoo 
                1. record.field = value 

                values = {
                    'field1': value,
                    'field2': value
                }
                2. record.write(values)

        """

        return super(Penjualan, self).create(vals)


    # pas di klik save, untuk edit 
    def write(self, vals):
        # Agregar codigo de validacion aca
        
        """
            setiap kali data di edit, maka ganti notes menjadi:
            'Data terakhir di ubah oleh : {} pada tanggal {}'
        """

        username = self.env.user.name
        # tanggal_sekarang = fields.Date.today()
        
        tanggal_sekarang = datetime.now()
        notes = 'Data terakhir di ubah oleh : {} pada tanggal {}'.format(username, tanggal_sekarang)
        vals['notes'] = notes

        #jika berhasil akan return True
        #jika error, maka odoo akan otomatis menampilkan errornya kenapa, kita enggak usah capek-capek ngurusin elsenya
        hasil = super(Penjualan, self).write(vals)

        # ini adalah cara lain dalam meng-edit isi data
        # jangan meng-edit record ini, di dalam func write() milik model yang sama, jadi endless loop
        # self.notes = notes #yang dilakukan, ini sebenarnya odoo akan menjalakan func write({'notes':notes})

        return True


    # Method to open the popup form
    def open_popup_form(self):

        # self = current record
        msg = 'Menampilkan popup milik data: {} '.format(self.name)


        # mode create new 
        return {
            'name': 'Berhasil',
            'type': 'ir.actions.act_window',
            'res_model': 'oavatar.pesan',  # Ganti dengan nama model Anda
            'view_mode': 'form',    # mode form, bukan tree
            'target': 'new',    # akan muncul di popup
            'context': {
                'default_name': msg
            }
        }


        # # mode popup readonly
        # return {
        #     'name': 'Berhasil',
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'oavatar.pesan',  # Ganti dengan nama model Anda
        #     'view_mode': 'form',    # mode form, bukan tree
        #     'target': 'new',    # akan muncul di popup
        #     'res_id': 1, # id milik record yang akan ditampilkan
        #     'create': False,
        #     'edit': False,
        # }


        # # mode popup boleh edit
        # return {
        #     'name': 'Berhasil',
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'oavatar.pesan',  # Ganti dengan nama model Anda
        #     'view_mode': 'form',    # mode form, bukan tree
        #     'target': 'new',    # akan muncul di popup
        #     'res_id': 1, # id milik record yang akan ditampilkan
        #     'create': False,
        #     'edit': True,
        # }


