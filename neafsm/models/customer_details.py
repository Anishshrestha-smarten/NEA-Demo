from odoo import models, fields

class Partner(models.Model):

    _inherit = "res.partner"

    consumer_id = fields.Char(string="Consumer ID")
    consumer_sc_no = fields.Char(string="Consumer SC No")
    customer_category = fields.Selection([('domestic60a','Domestic Consumer(60A)')],required=True, default='domestic60a',string='Consumer Category')
    nearest_landmark = fields.Char(string="Nearest Landmark")
    department_name = fields.Selection([('budhanilkantha','Budhanilkantha'),('naxal','Naxal'),('maharjgunj','Maharajgunj'),('ratnapark','Ratnapark'),('tokha','Tokha')],string="Department Name")


    meter_sn = fields.Char(string='Meter Serial Number')
    meter_type = fields.Selection([('1pwc','1 Phase WC Meter'),('3p3wct','3 Phase 3 Wire CT Meter'),\
                                   ('3p4wwc','3 Phase 4 Wire WC Meter'),('3p4wct','3 Phase 4 Wire CT Meter')],required=True, default='1pwc')
    meter_reading=fields.Float(string='Meter Reading')
    approved_load=fields.Char(string='Approved Load ')
    installed_by=fields.Char(string='Installed By')
    installed_date=fields.Datetime(string="Installation date", readonly=True)
    sm_image=fields.Binary(string='Meter Details')