from odoo import models, fields, api
from datetime import date


class ProjectProject(models.Model):
    _inherit = "project.project"
    _description = 'Planning Hours'

    hours_total = fields.Float("Hours Project")
    hours_total_planned = fields.Float(string='Scheduled Hours',compute="_compute_hours_total_planned")
    planning_line_ids = fields.One2many(comodel_name='project.planning.line', inverse_name="project_id",
                                        string="Planning Hours")

    @api.depends("hours_total_planned")
    def _compute_hours_total_planned(self):
        self.hours_total_planned = self.hours_total - (sum(list(rec.hours_invested for rec in self.planning_line_ids)))


