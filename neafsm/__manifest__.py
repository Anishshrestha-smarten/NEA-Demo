# -*- coding: utf-8 -*-
{
    'name': "NEA FSM Smartmeter",

    'summary': """
        Field service management customization for Smartmeter installation""",

    'description': """
        To ease man Field service management for smartmeter installation 
    """,

    'author': "Smarten Technologies",
    'website': "https://www.smarten.com.np",

    'category': 'Services',
    'version': '0.1',
    'license': 'LGPL-3',
    'sequence':'-10',
    'depends': ['base', 'industry_fsm','contacts'],

    'data': [
        'security/ir.model.access.csv',
        'data/nea_smartmeter_fsm.xml',
        'wizard/state_wizards.xml',
        'views/views.xml',
        'views/project_task_extend.xml',
        'views/customer_details.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,

    'installable': True,
}
