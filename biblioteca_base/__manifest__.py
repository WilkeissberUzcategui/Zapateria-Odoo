{
    'name': 'Biblioteca Base',
    'version': '18.0.1.0.0',
    'summary': 'Configuración base para sistema de biblioteca',
    'description': 'Módulo padre con sedes, categorías y libros para el ejercicio práctico.',
    'author': 'Docente',
    'category': 'Education',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/biblioteca_base_views.xml',
        'data/biblioteca_base_data.xml',
    ],
    'installable': True,
    'application': True,
}
