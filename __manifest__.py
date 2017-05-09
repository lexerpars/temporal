# -*- coding: utf-8 -*-
{
    'name': "temporal",

    'summary': """
        Modulo especifico para realizar pruebas de concepto sobre programacion en Odoo""",

    'description': """
        POC, Proof Of Concept, es un modulo que contiene pruebas de concepto sobre la api que
        tiene odoo, asi como de diversas tecnicas de programacion.
    """,

    'author': "rperez",

    'application': True,

    'installable': True,

    'website': "http://www.guatewares.com",

    'category': 'Testing',

    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/invoice_format_print.xml',
    ],

    'demo': [

    ]
}
