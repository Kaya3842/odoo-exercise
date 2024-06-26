# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class CustomerRequest(models.Model):
    _name = "crm.customer.request"
    _description = "Customer Request"
    
    # Fields
    product_id = fields.Many2one("product.template", string="Product", required=1)
    opportunity_id = fields.Many2one("crm.lead", string="Opportunity", required=1)
    date = fields.Date(string="Date", required = 1, default=fields.Date.today())
    description = fields.Text()
    qty = fields.Float(string="Quantity", default=1)

    # Methods
    @api.model
    def create(self, vals):
        opportunity = self.env['crm.lead'].browse(vals.get('opportunity_id'))
        if opportunity.stage_id and opportunity.stage_id.name != 'New':
            raise ValidationError("Only create, update, delete on 'new' state of Opportunity")
        return super(CustomerRequest, self).create(vals)

    def write(self, vals):
        for request in self:
            if request.opportunity_id.stage_id and request.opportunity_id.stage_id.name != 'New':
                raise ValidationError("Only create, update, delete on 'new' state of Opportunity")
        return super(CustomerRequest, self).write(vals)

    def unlink(self):
        for request in self:
            if request.opportunity_id.stage_id and request.opportunity_id.stage_id.name != 'New':
                raise ValidationError("Only create, update, delete on 'new' state of Opportunity")
        return super(CustomerRequest, self).unlink()