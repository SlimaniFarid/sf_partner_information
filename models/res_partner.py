# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    reports_name      = fields.Text('reports name')    
    family_situation = fields.Selection(string='Family situation',selection=[('single', 'Single'),
                                                                             ('married', 'Married'),
                                                                             ('divorced', 'Divorced'),
                                                                             ('widow','Widow / Widower'),
                                                                             ('separated','Separated'),
                                                                             ])
  
    country_of_birth_id = fields.Many2one('res.country',string='Country of birth')
    Place_of_birth   = fields.Char('Place of birth')
    Profession       = fields.Selection(string='Profession',selection=[('entrepreneur','Entrepreneur'),('student','Student'),('employee','Employee'),('sector','Sector'),('retired','Retired'),])
    passport_number  = fields.Char('Passport number')
    delivered_by     = fields.Char('Delivered by') 
    Passport_delivery_date   = fields.Date('Passport delivery date')
    Passport_expiration_date = fields.Date('Passport expiration date')
    Spouses_name     = fields.Char("Spouse's name")
    Fathers_name     = fields.Char("Father's name")
    document_type    = fields.Char("Document type")
    foreigner_identity_number = fields.Char('Foreigner Identity Number (NIE)')
    reasons    = fields.Selection(string='Reasons',selection=[('For_economic_interests','For economic interests'),
                                                                             ('for_professional_interests','For professional interests'),
                                                                             ('for_social_interests','For social interests'),
                                                                                    
                                                                                    ] )
    specify = fields.Selection(string='Specify',selection=[('company_creation','Company creation'),
                                                                             ('studies','studies'),
                                                                             ('buy_hous','Buy hous'),
                                                                             ('open_bank_account','Open bank account'),
                                                                             ('other','Other'),
                                                                                    ])                                                                               
    place_of_presentation =  fields.Selection(string='Place of presentation',selection=[('immigration_Office','Immigration Office'),
                                                                             ('police_station','Police station'),
                                                                             ('consular_office','Consular office'),
                                                                    
                                                                                    ])   
    ######################                                                                                
    building_no           =  fields.Char('Building N°')   
    floor_no              =  fields.Char('Floor N°')   
    mothers_name          =  fields.Char("Mother's name")   
    lastname2            =  fields.Char('Last name (2)') 
    request_nie           =  fields.Date('Request NIE')    

    def do_print_report(self,id):
       report_obj = self.env['ir.actions.report']
       # report = report_obj._get_report_from_name('account.account_invoices')
       # return {
       #      'doc_ids': [1],
       #      'doc_model': 'account.move',
       #      'docs': self,
       #  }
       # return self.env.ref('').report_action(id)

