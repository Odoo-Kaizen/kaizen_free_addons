# -*- coding: utf-8 -*-
{
    'name': "Stock Report PDF",

    'summary': """
       print stock report, stock report pdf, print stock report pdf, product report pdf, product stock pdf, product stock with overall total purchased and total sold quantities""",

    'description': """
       print stock report, stock report pdf, print stock report pdf, product report pdf, product stock , product stock with overall total purchased and total sold quantities""",


    'author': "Kaizen Principles",
    'website': 'http://www.kaizenae.com',


    'category': 'Stock',
    'version': '17.0.1.0',
    'license': 'OPL-1',
    'depends': ['base', 'stock', 'stock_account', 'sale', 'purchase', 'product'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,

}
