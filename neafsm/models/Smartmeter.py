from odoo import models, fields

class SmartMeter(models.Model):
    _name='smartmeter.details'
    _description = 'Device details and status information'

    name = fields.Char(string='Meter Serial Number', required=True)
    meter_type = fields.Selection([('1pwc','1 Phase WC Meter'),('3p3wct','3 Phase 3 Wire CT Meter'),\
                                   ('3p4wwc','3 Phase 4 Wire WC Meter'),('3p4wct','3 Phase 4 Wire CT Meter')],required=True, default='1pwc')
    meter_reading=fields.Float(string='Meter Reading')
    approved_load=fields.Char(string='Approved Load ')
    rel_partner_id = fields.Char('res.partner', string='Owner')