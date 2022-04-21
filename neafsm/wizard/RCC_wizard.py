from odoo import models, fields, _
from datetime import datetime

class RescheduleData(models.TransientModel):
    _name = "reschedule.data"
    _description = 'Need to fill this wizard to reschedule the task'

    r_desc = fields.Char(string="Description", required=True)




    def action_reschedule(self):
        """Update from wizard button"""
        self.ensure_one()
        rescheduled_stage_id = self.env.ref("neafsm.nea_fsm_stage_3").id
        values_dict = {'reschedule_note': self.r_desc, 'stage_id': rescheduled_stage_id}
        self.env['project.task'].browse(self.env.context.get('active_ids')).write(values_dict)


class CancelData(models.TransientModel):
    _name = "cancel.data"
    _description = 'Need to fill this wizard to cancel the task'

    c_desc = fields.Char(string="Description", required=True)

    def action_cancel(self):
        """Update from wizard button"""
        self.ensure_one()
        current_task_obj = self.env['project.task'].browse(self.env.context.get('active_ids'))

        # find id of canceled stage
        canceled_stage_id = self.env.ref("neafsm.nea_fsm_stage_5").id
        values_dict = {'cancellation_note': self.c_desc, 'stage_id': canceled_stage_id}
        # change update task (to cancelled)
        current_task_obj.write(values_dict)


class CompleteData(models.TransientModel):
    _name = "complete.data"
    _description = 'Need to fill this wizard to before the task'

    c_desc = fields.Char(string="Description", required=True)
    meter_sn = fields.Char(string='Meter Serial Number', required=True)
    meter_type = fields.Selection([('1pwc', '1 Phase WC Meter'), ('3p3wct', '3 Phase 3 Wire CT Meter'), \
                                   ('3p4wwc', '3 Phase 4 Wire WC Meter'), ('3p4wct', '3 Phase 4 Wire CT Meter')],
                                  required=True, default='1pwc')
    meter_reading = fields.Float(string='Meter Reading', required=True)
    installed_by = fields.Char(string='Installed By')
    customer_signature=fields.Binary(string="Customer's Signature")
    image=fields.Binary(string="Image")


    def action_complete(self):
        """Update from wizard button"""
        self.ensure_one()
        current_task_obj = self.env['project.task'].browse(self.env.context.get('active_ids'))

        meter_details = {'meter_sn': self.meter_sn,
                         'meter_type': self.meter_type,
                         'meter_reading': self.meter_reading,
                         'installed_date':datetime.now(),
                         'installed_by': self.env.user.name,
                         'sm_image':self.image,}
        completed_stage_id = self.env.ref("neafsm.nea_fsm_stage_4").id
        values_dict = {'completion_note': self.c_desc, 'stage_id': completed_stage_id,'customer_signature':self.customer_signature}

        current_task_obj.write(values_dict)
        current_task_obj.partner_id.write(meter_details)
