from odoo import fields, models

class Estimated_time(models.Model):
    _name = "estimated.time"
    _description = "Spend Time"
    _inherit=["mail.thread","mail.activity.mixin"]
    task_id = fields.Many2one("to.do", string="Task Name")
    date = fields.Date()
    time_taken = fields.Float(string="Time Taken")
    description = fields.Text()
    activity_type = fields.Selection([
        ("develop","Develop"),
        ("check","Check"),
        ("meeting","Meeting"),
    ], default = "develop")
    active = fields.Boolean(default=True)

    
    