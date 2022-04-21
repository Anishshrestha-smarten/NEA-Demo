from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import timedelta, datetime

class ProjectTask(models.Model):
    _inherit = "project.task"

    cancellation_note = fields.Text(string="Cancellation Note:")
    reschedule_note = fields.Text(string="Reschedule Note:")
    completion_note = fields.Text(string="Completion Note:")

    stage_name = fields.Char(default='New')
    project_name = fields.Char(related="project_id.name")
    is_fsm_nea = fields.Boolean(related="project_id.is_fsm_nea")

    customer_signature = fields.Binary(string="Customer's Signature")


    @api.constrains('planned_date_begin')
    @api.onchange('planned_date_begin')
    def _schedule_begin(self):
        if self.stage_id.name == "New":
            if self.planned_date_begin:
                if not self.planned_date_end:
                    self.planned_date_end=self.planned_date_begin+timedelta(hours=24)
                self.stage_id = self.env.ref("neafsm.nea_fsm_stage_1").id
                if self.user_ids:
                    self.stage_id=self.env.ref("neafsm.nea_fsm_stage_2").id

    @api.onchange('user_ids')
    @api.constrains('user_ids')
    def _onchange_uid(self):
        if self.stage_id.name == "Scheduled" and self.user_ids:
            self.stage_id = self.env['project.task.type'].browse(self.stage_id.id+1).id


    @api.constrains('stage_id')
    def _kanban_state(self):
        self.stage_name = self.stage_id.name
        if self.stage_name == 'New':
            self.kanban_state='normal'
        elif self.stage_name =='Cancelled':
            self.kanban_state='blocked'
        else:
            self.kanban_state='done'


