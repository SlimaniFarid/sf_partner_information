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
    'depends': ['base','website_crm','crm','website_blog',
                'partner_contact_personal_information_page',
                'partner_contact_birthdate',
                'partner_contact_gender',
                ],

    # always loaded
    'data': [
      
        'views/res_partner.xml',
        'static/src/xml/nie_form_template.xml',
        'static/src/xml/website_blog.xml',
        'static/src/xml/website_form.xml',
        'static/src/xml/portal_my_doc.xml',

        'report/paperformat.xml',
        'report/template_form.xml',
        'report/partner_form.xml',
       
      
      
    ],
 
}
