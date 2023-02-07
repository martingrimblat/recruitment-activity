{
    'name': 'Real State Management',
    "version": "15.0.1.0.0",
    'depends': ['base'],
    "license": "LGPL-3",
    'data': [
        'data/estate.property.type.csv',
        'data/estate_property_tag_data.xml',
        'demo/estate_property_demo.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}