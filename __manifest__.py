# -*- coding: utf-8 -*-
{
    'name': "sf_partner_information",

    'summary': """
       """,

    'description': """
        
    """,

    'author': "FK",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website_crm','crm'],

    # always loaded
    'data': [
      
        'views/res_partner.xml',
        'static/src/xml/website_crm.xml',
      
    ],
 
}
