from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BibliotecaSede(models.Model):
    _name = 'biblioteca.sede'
    _description = 'Sede de Biblioteca'
    _rec_name = 'name'

    name = fields.Char(string='Nombre de la Sede', required=True)
    ciudad = fields.Char(string='Ciudad', required=True)
    direccion = fields.Char(string='Dirección')
    codigo = fields.Char(string='Código de Sede', required=True)

    _sql_constraints = [
        ('codigo_sede_unico', 'unique(codigo)', 'El código de sede ya existe.')
    ]


class BibliotecaCategoria(models.Model):
    _name = 'biblioteca.categoria'
    _description = 'Categoría de Libro'
    _rec_name = 'name'

    name = fields.Char(string='Categoría', required=True)
    descripcion = fields.Text(string='Descripción')


class BibliotecaLibro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro de Biblioteca'
    _rec_name = 'titulo'

    codigo = fields.Char(string='Código del Libro', required=True)
    titulo = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor', required=True)
    categoria_id = fields.Many2one('biblioteca.categoria', string='Categoría', required=True)
    dias_prestamo = fields.Integer(string='Días Permitidos', required=True, default=7)
    multa_diaria = fields.Float(string='Multa Diaria', required=True, default=0.50)
    disponible = fields.Boolean(string='Disponible', default=True)

    _sql_constraints = [
        ('codigo_libro_unico', 'unique(codigo)', 'El código del libro ya existe.')
    ]

    @api.constrains('dias_prestamo', 'multa_diaria')
    def _validar_condiciones_prestamo(self):
        for record in self:
            if record.dias_prestamo <= 0:
                raise ValidationError('Los días permitidos deben ser mayores a cero.')
            if record.multa_diaria < 0:
                raise ValidationError('La multa diaria no puede ser negativa.')
