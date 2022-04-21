from email.policy import default
from odoo import models, fields

class SmartMeter(models.Model):
    _inherit='product.template'

    is_meter = fields.Boolean(string='Is Meter', default=False)
    meter_sn = fields.Integer(string='Meter Serial Number', index=True)


    