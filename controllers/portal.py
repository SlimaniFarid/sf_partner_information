# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.exceptions import AccessError, MissingError, UserError
from odoo.http import request
from odoo.tools.translate import _
from odoo.addons.portal.controllers.portal import pager as portal_pager, CustomerPortal
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.osv.expression import OR
import logging
_logger = logging.getLogger(__name__)
import ast

class DocPortal(CustomerPortal):

    def _prepare_portal_layout_values(self):
        values = super(DocPortal, self)._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        reports_name = ast.literal_eval(partner.reports_name)
        report = request.env['ir.actions.report'].search([('report_name','in',reports_name)])
        values.update({"doc_count":len(report),
                       'title': _("Documents"),
                       'page_name': 'Documents'})
        return values   


    @http.route('/my/doc', type='http', auth="user", website=True)
    def contactus(self, **kwargs):
        partner = request.env.user.partner_id
        reports_name = ast.literal_eval(partner.reports_name)
        reports = request.env['ir.actions.report'].search([('report_name','in',reports_name)])
        values={}
        if len(reports)>0:
            values={"documents":[report.name for report in reports]}
        return request.render("sf_partner_information.portal_my_doc",values)