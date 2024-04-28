# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Produk(models.Model):
    #nama id model, nama id ini akan otomatis digenerate menjadi table di database
    _name = 'oavatar.produk' 

    #ini adalah keterangan modelnya
    _description = 'Ini adalah master produk'

    #ini untuk memaksa odoo, jangan pakai field name, tapi field no_transaksi
    # _rec_name = "no_transaksi"

    #nama di odoo = name 
    no_transaksi = fields.Char(string="Kode Produk")

    name = fields.Char('Nama Produk', required=True)

    harga = fields.Float()

    # untuk status, biasanya namanya state 
    state = fields.Selection(string='Status', selection=[
        ('good', 'Good'),
        ('bad', 'Bad'),
    ])

    notes = fields.Text(readonly=True)



    @api.model
    def create(self, vals):
        # Agregar codigo de validacion aca
        
        produk = super(Produk, self).create(vals)

        name = produk.name
        msg = 'Data {} telah berhasil disimpan'.format(name)

        # tampilkan pesan
        # enggak bisa taro di sini.
        # return self.open_popup_form()

        return produk



    # Method to open the popup form
    def open_popup_form(self):
        return {
            'name': 'Berhasil',
            'type': 'ir.actions.act_window',
            'res_model': 'oavatar.pesan',  # Ganti dengan nama model Anda
            'view_mode': 'form',    # mode form, bukan tree
            'target': 'new',    # akan muncul di popup
        }




    def unlink(self):
    # Agregar codigo de validacion aca
        # self = adalah current record (bisa banyak)
        """
            Jika produk dihapus 
            maka set transaction id= 4, notes nya menjadi 'Usser X baru saja menghapus produk Y'

        """ 
        penjualan_id = [4, 5]
        penjualan_ids = self.env['oavatar.penjualan'].browse(penjualan_id)

        print("################################################")
        print("penjualan: ", penjualan_ids) # (4, 5)

        username = self.env.user.name
        nama_produk = self.name
        notes = 'Usser {} baru saja menghapus produk {}'.format(username, nama_produk)
        
        
        penjualan_ids.notes2 = 'Usser {} baru saja menghapus produk {}'.format(username, nama_produk)

        # for p in penjualan_ids:
        #     p.notes = notes
        #     print(" update {} set notes = {}".format(p.id, notes) )


        # print("penjualan: ", penjualan) # (4, 5)

        return super(Produk, self).unlink()


