# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api
from odoo import http
from odoo.http import request
from odoo.addons.website_crm.controllers.main import WebsiteForm
import logging
_logger = logging.getLogger(__name__)
import io
import re
from PyPDF2 import  PdfFileReader, PdfFileWriter
import base64
import werkzeug
from werkzeug import urls
import ast

class WebsiteForm(WebsiteForm):

    def _get_country(self):
        country_code = request.session.geoip and request.session.geoip.get('country_code') or False
        if country_code:
            return request.env['res.country'].sudo().search([('code', '=', country_code)], limit=1)
        return request.env['res.country']

    def _get_phone_fields_to_validate(self):
        return ['phone', 'mobile']


    @http.route('/contactus', type='http', auth="user", website=True)
    def contactus(self, **kwargs):
        return request.render("website_crm.contactus_form")
      
    def get_country(self):
        return request.env['res.country'].sudo().search([])  

    def get_state(self):
        return request.env['res.country.state'].sudo().search([]) 


    @http.route('/my_form_nie', type='http', auth="user", website=True)
    def my_form_nie(self, **kwargs):

        values = {'countries':self.get_country(),
                  'states'  : self.get_state(),
                }


        return request.render("sf_partner_information.nie_form",values)
      


    # Check and insert values from the form on the model <model> + validation phone fields
    @http.route('/form_nie', type='http', auth="user", methods=['POST'], website=True, csrf=False)
    def form_nie(self, **kwargs):
        val = {     
                'lastname'                      : kwargs.get('lastname'),
                'lastname2'                     : kwargs.get('lastname2'),
                'firstname'                     : kwargs.get('firstname'),
                'reports_name'                  :"['sf_partner_information.report_formulaire']",
                'family_situation'              : kwargs.get('family_situation'),
                'country_of_birth_id'           : kwargs.get('country_of_birth_id'),
                'Place_of_birth'                : kwargs.get('Place_of_birth'),
                'Profession'                    : kwargs.get('Profession'),
                'passport_number'               : kwargs.get('passport_number'),
                'delivered_by'                  : kwargs.get('delivered_by'),
                'Passport_delivery_date'        : kwargs.get('Passport_delivery_date'),
                'Passport_expiration_date'      : kwargs.get('Passport_expiration_date'),
                'Spouses_name'                  : kwargs.get('Spouses_name'),
                'Fathers_name'                  : kwargs.get('Fathers_name'),
                'document_type'                 : kwargs.get('document_type'),
                'reasons'                       : kwargs.get('reasons'),
                'specify'                       : kwargs.get('specify'),                                                 
                'place_of_presentation'         : kwargs.get('place_of_presentation'),                                                                
                'building_no'                   : kwargs.get('building_no'),
                'floor_no'                      : kwargs.get('floor_no'),
                'mothers_name'                  : kwargs.get('mothers_name'),
                'request_nie'                   : fields.Date.today(),
                }
       
        user = request.env['res.users'].search([('id','=',request.session.uid)])    
        child = False
        user.partner_id.write({'reports_name' : "['sf_partner_information.report_formulaire']",})

        for c in user.partner_id.child_ids:
            if c.type=="private":
                child = c 
        if not child :
            user.partner_id.child_ids = [(0,0,val)] 
        else :
            child.write(val)       
    





        return request.render("sf_partner_information.nie_form_thanks")
        


    @http.route('/print_report_1', auth="user",type='http' )
    def print_report(self,**kwargs):
        pdf_writer = PdfFileWriter()
        partner = request.env.user.partner_id
        _logger.warning('\n ok ok partner.reports_name=>%s',partner.reports_name)

        report_name = ast.literal_eval(partner.reports_name)[0]

        report = request.env['ir.actions.report'].search([('report_name','=',report_name)])
        pdf_content =  report.render_qweb_pdf(partner.id)[0]        
        pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf_content)),('Content-Disposition', 'attachment; filename='+partner.name+'.pdf'),]
        return request.make_response(pdf_content, headers=pdfhttpheaders)       


    def insert_record(self, request, model, values, custom, meta=None):
        if model.model == 'crm.lead':
            if 'company_id' not in values:
                values['company_id'] = request.website.company_id.id
            lang = request.context.get('lang', False)
            lang_id = request.env["res.lang"].sudo().search([('code', '=', lang)], limit=1).id
            values['lang_id'] = lang_id
        result = super(WebsiteForm, self).insert_record(request, model, values, custom, meta=meta)
        visitor_sudo = request.env['website.visitor']._get_visitor_from_request()
        if visitor_sudo and result:
            lead_sudo = request.env['crm.lead'].browse(result).sudo()
            if lead_sudo.exists():
                vals = {'lead_ids': [(4, result)]}
                if not visitor_sudo.lead_ids and not visitor_sudo.partner_id:
                    vals['name'] = request.env['crm.lead'].browse(result).sudo().contact_name
                visitor_sudo.write(vals)


        return result
