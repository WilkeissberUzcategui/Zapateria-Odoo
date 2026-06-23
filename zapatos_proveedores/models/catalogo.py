from odoo import models, fields


class Proveedor(models.Model):
    _name = 'zapatos.proveedor'
    _description = 'Proveedor'

    name = fields.Char(
        string='Nombre',
        required=True
    )

    telefono = fields.Char(
        string='Telefono'
    )

    email = fields.Char(
        string='Correo Electronico'
    )

    direccion = fields.Text(
        string='Direccion'
    )


class Categoria(models.Model):
    _name = 'zapatos.categoria'
    _description = 'Categoria'

    name = fields.Char(
        string='Nombre',
        required=True
    )

    descripcion = fields.Text(
        string='Descripcion'
    )