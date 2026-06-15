from odoo import models, fields, api
 
 
class ZapatosZapato(models.Model):
    _inherit = 'zapatos.zapato'
 
    codigo = fields.Char(string='Código')
    marca = fields.Char(string='Marca')
    color = fields.Char(string='Color')
    material = fields.Char(string='Material')
    descripcion = fields.Text(string='Descripción')
    stock_minimo = fields.Integer(string='Stock Minimo', default=5)
 
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('available', 'Disponible'),
        ('out_stock', 'Agotado'),
        ('discontinued', 'Descontinuado'),
    ], string='Estado', default='draft')
 
    valor_inventario = fields.Float(
        string='Valor_inventario',
        compute='_compute_valor_inventario',
        store=True
    )
 
    @api.depends('precio', 'stock')
    def _compute_valor_inventario(self):
        for record in self:
            record.valor_inventario = record.precio * record.stock
 
    def action_disponible(self):
        for record in self:
            record.state = 'available'
 
    def action_agotado(self):
        for record in self:
            record.state = 'out_stock'
 
    def action_descontinuar(self):
        for record in self:
            record.state = 'discontinued'
 
    def action_borrador(self):
        for record in self:
            record.state = 'draft'
 
