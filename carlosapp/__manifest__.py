{
    'name':'Motorcycle Registry',
    'summary':""" Manage Registration of s """,
    'description':""" Motorcycle Registry
    ====================
    This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.
       """,
    'license':'OPL-1',
    'author':'cmgv-odoo',
    'website':'www.odoo.com',
    'category':'Kawiil/Admin',
    'depends':['stock', 'website'],
    'data':[
        'security/carlosapp_groups.xml',
        'security/ir.model.access.csv',
        'security/carlosapp_security.xml',
        'data/registry_data.xml',
        'views/carlosapp_menuitems.xml',
        'views/carlosapp_views.xml',
        'views/product_view_inherit.xml',
        'views/carlosapp_web_templates.xml',
    ],
    'demo':[
        'demo/registry_demo.xml',
    ],
    'application': True,
}