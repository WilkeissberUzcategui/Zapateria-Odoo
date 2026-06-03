import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BibliotecaLector(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Prestamos de Libros'
    #_rec_name = 'name'
    
    lector_id = fields.Many2one('biblioteca.lector',
                               string = "Lector",
                               required=True,
                               ondelete="restrict")
    
    cedula_rel = fields.Char(related='lector_id.cedula',
                             string = "Cedula",
                             required=True)
    
    limite_prestamos_rel = fields.Integer(related='lector_id.limite_prestamos',
                                          string = "Limites de Prestamos",
                                          required=True)
    
    sede_rel = fields.Integer(related='lector_id.sede_id',
                                          string = "Sede Asignada",
                                          required=True)
    
    libro_id = fields.Many2one('biblioteca.libro',
                               string = "Libro",
                               required=True,
                               ondelete="restrict")
    
    categoria_rel = fields.Many2one(related='libro_id.categoria_id')
    
    sede_rel = fields.Many2one(related='lector_id.sede_id',
                               string="Sede Asignada",
                               store=True)
    
    dia_prestados_rel = fields.Integer(related='libro_id.dias_prestamo',
                                    string = "Días Permitidos",
                                    required=True)
    
    multa_diaria_rel = fields.Float(related='libro_id.multa_diaria',
                                    string = "Multa Diaria",
                                    required=True)
    
    dias_usados = fields.Integer(string="Días Usados",
                                 required=True,
                                 default=1)
    
    dias_atrasados = fields.Integer(string="Días Atrasados",
                                    compute='_compute_atrasos',
                                    store=True)

    multa_total = fields.Float(string="Multa Total",
                               required=True,
                               default=0)
    
    @api.depends('dias_usados','dia_prestados_rel')
    def _compute_atrasos(self):
        for rec in self:
            rec.dias_atrasados = rec.dias_usados - rec.dia_prestados_rel

    @api.depends('dias_atrasados','multa_diaria_rel')
    def _compute_multa_total(self):
        for rec in self:
            rec.multa_total = rec.dias_atrasados * rec.multa_diaria_rel
