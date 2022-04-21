# -*- coding: utf-8 -*-
{
    'name': "NEA Inventory Smartmeter",

    'summary': """
        Inventory management customization for Smartmeter installation""",

    'description': """
        Inventory management for smartmeter installation 
    """,

    'author': "Smarten Technologies",
    'website': "https://www.smarten.com.np",

    'category': 'Services',
    'version': '0.1',
    'license': 'LGPL-3',
    'sequence':'-10',
    'depends': ['base', 'stock','product'],

    'data': [
        'views/meter_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,

    'installable': True,
}
