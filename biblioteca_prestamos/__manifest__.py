{
    'name': 'Biblioteca Prestamo',
    'version': '18.0.1.0.0',
    'summary': 'Gestión básica para prestamos de la biblioteca',
    'description': 'Módulo hijo con lectores relacionados a las sedes de biblioteca.',
    'author': 'Wil',
    'category': 'Education',
    'license': 'LGPL-3',
    'depends': ['base', 'biblioteca_base','biblioteca_lectores'],
    'data': [
        'security/ir.model.access.csv',
        'views/biblioteca_prestamo_views.xml',
    ],
    'installable': True,
    'application': True,
}
