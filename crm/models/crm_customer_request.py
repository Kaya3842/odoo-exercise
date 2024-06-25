# -*- coding: utf-8 -*-

from odoo import api, fields, models

class CustomerRequest(models.Model):
    _name = "crm.customer.request"
    _description = "Customer Request"
    
    # Fields
    product_id = fields.Many2one("product.template", string="Product", required=1)
    opportunity_id = fields.Many2one("crm.lead", string="Opportunity", required=1)
    date = fields.Date(string="Date", required = 1, default=fields.Date.today())
    description = fields.Text()
    qty = fields.Float(string="Quantity", default=1)