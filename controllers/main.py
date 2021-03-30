# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.addons.website_crm.controllers.main import WebsiteForm
import logging
_logger = logging.getLogger(__name__)

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
      
  

    # Check and insert values from the form on the model <model> + validation phone fields
    @http.route('/website_form/<string:model_name>', type='http', auth="user", methods=['POST'], website=True)
    def website_form(self, model_name, **kwargs):
        user = request.env['res.users'].search([('id','=',request.session.uid)])    
        _logger.warning('\n ok ok user =>%s',user)
        user.partner_id.write({
                               'Place_of_birth':kwargs.get('Place_of_birth'),
                               'Passport_delivery_date':kwargs.get('Passport_delivery_date'),
                               'Passport_delivery_date':kwargs.get('Passport_delivery_date'),
                               'specify':kwargs.get('specify'),
        })

   

        return super(WebsiteForm, self).website_form(model_name, **kwargs)

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
