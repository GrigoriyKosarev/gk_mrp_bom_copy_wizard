{
    'name': 'BOM copy',
    'version': '15.0.0.0.1',
    'summary': """
        BOM.
    """,
    'category': 'Customizations',
    'author': 'grigoriykosarev@gmail.com',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['mrp'],
    'external_dependencies': {'python': [], },
    'data': [
        'security/ir.model.access.csv',
        'wizard/mrp_bom_line_views.xml',
        'wizard/copy_bom_wizard_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'support': 'grigoriykosarev@gmail.com',
}
