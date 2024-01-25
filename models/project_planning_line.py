from odoo import models, fields, api
from datetime import date


class ProjectPlanningLine(models.Model):
    _name = "project.planning.line"
    _description = 'Planning Hours'

    project_id = fields.Many2one("project.project", "Project")
    employee_id = fields.Many2one("hr.employee", "Employee")
    hours_invested = fields.Float("  H. Invested  ", compute="_compute_hours_invested", store=True)
    hours_assigned = fields.Float(" H.Assigned ")
    hours_assigned_string = fields.Char(" H.Assigned ")
    hour_pending = fields.Float(" H.Pending ", compute="_compute_hour_pending", store=True)
    hours_pending_string = fields.Char(" H.Pending ")

    @api.depends('project_id')
    def _compute_hours_invested(self):
        self.hours_invested = sum(list(rec.unit_amount for rec in self.project_id.timesheet_ids))

    @api.onchange('employee_id')
    def _onchange_relation(self):
        self.hours_assigned = self.employee_id.hours_assigned
        self.hours_assigned_string = f"{self.hours_assigned}/{self.hours_invested}"

    @api.depends('hours_assigned')
    def _compute_hour_pending(self):
        self.hour_pending = self.hours_invested - self.hours_assigned
        if self.hours_assigned > self.hours_invested:
            self.hours_pending_string=0.0
        else:
            self.hours_pending_string = f"{self.hour_pending}/{self.hours_invested}"
