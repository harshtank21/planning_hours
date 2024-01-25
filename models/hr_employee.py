from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    hours_assigned = fields.Float(" H.Assigned ")
