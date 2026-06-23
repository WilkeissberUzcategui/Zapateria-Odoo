<<<<<<< HEAD
# zapateria 
# nombre , talla , precio, stock, 

from odoo import models, fields


class ZapatosZapato(models.Model):
    _name = 'zapatos.zapato'
    _description = 'Zapato'

    name = fields.Char(string='Nombre', required=True)
    talla = fields.Integer(string='Talla')
    precio = fields.Float(string='Precio')
    stock = fields.Integer(string='Stock')
    activo = fields.Boolean(string='Activo', default=True)
=======
# zapateria 
# nombre , talla , precio, stock, 

from odoo import models, fields, api


class ZapatosZapato(models.Model):
    _name = 'zapatos.zapato'
    _description = 'Zapato'

    name = fields.Char(string='Nombre', required=True)
    talla = fields.Integer(string='Talla')
    precio = fields.Float(string='Precio')
    stock = fields.Integer(string='Stock')
    activo = fields.Boolean(string='Activo', default=True)

    valor_inventario= fields.Float(compute='_compute_valor_inventario',string='valor total',store=True)

    @api.depends('stock','precio')
    def _compute_valor_inventario(self):
        for r in self:
            r.valor_inventario= r.precio * r.stock
>>>>>>> dc354161fbd08209893c1d018798333cc58b3849
