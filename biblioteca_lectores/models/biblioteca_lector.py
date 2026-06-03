import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BibliotecaLector(models.Model):
    _name = 'biblioteca.lector'
    _description = 'Lector de Biblioteca'
    _rec_name = 'name'

    name = fields.Char(string='Nombre del Lector', required=True)
    cedula = fields.Char(string='Cédula', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo Electrónico')
    limite_prestamos = fields.Integer(string='Límite de Préstamos', required=True, default=3)

    sede_id = fields.Many2one(
        'biblioteca.sede',
        string='Sede Asignada',
        required=True
    )

    @api.constrains('cedula')
    def _validar_cedula(self):
        for record in self:
            if record.cedula and not re.fullmatch(r'\d{10}', record.cedula):
                raise ValidationError('La cédula debe contener exactamente 10 dígitos numéricos.')

    @api.constrains('email')
    def _validar_email(self):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        for record in self:
            if record.email and not re.match(patron, record.email):
                raise ValidationError('Ingrese un correo electrónico válido.')

    @api.constrains('limite_prestamos')
    def _validar_limite_prestamos(self):
        for record in self:
            if record.limite_prestamos <= 0:
                raise ValidationError('El límite de préstamos debe ser mayor a cero.')
