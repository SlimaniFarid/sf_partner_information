# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'


    family_situation = fields.Selection(string='Family situation',selection=[('single', 'Single'),('married', 'Married'),('divorced', 'Divorced')])
    Place_of_birth   = fields.Char('Place of birth')  
    Profession       = fields.Selection(string='Profession',selection=[('entrepreneur','Entrepreneur'),('student','Student'),('employee','Employee'),('sector','Sector'),('retired','Retired'),])
    passport_number  = fields.Char('Passport number')
    delivered_by     = fields.Char('Delivered by') 
    Passport_delivery_date   = fields.Char('Passport delivery date')
    Passport_expiration_date = fields.Char('Passport expiration date')
    Spouses_name     = fields.Char("Spouse's name")
    Fathers_name     = fields.Char("Father's name")
    document_type    = fields.Char("Document type")
    foreigner_identity_number = fields.Char('Foreigner Identity Number (NIE)')
    reasons    = fields.Selection(string='For economic interests',selection=[('For_economic_interests','For economic interests'),
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
    
    


