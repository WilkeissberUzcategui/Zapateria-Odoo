{
    'name': 'Biblioteca Lectores',
    'version': '18.0.1.0.0',
    'summary': 'Gestión básica de lectores de biblioteca',
    'description': 'Módulo hijo con lectores relacionados a las sedes de biblioteca.',
    'author': 'Docente',
    'category': 'Education',
    'license': 'LGPL-3',
    'depends': ['base', 'biblioteca_base'],
    'data': [
        'security/ir.model.access.csv',
        'views/biblioteca_lector_views.xml',
        'data/biblioteca_lectores_data.xml',
    ],
    'installable': True,
    'application': True,
}
