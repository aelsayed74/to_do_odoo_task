from odoo import fields, models, api
from odoo.exceptions import ValidationError

class To_do(models.Model):
    _name = "to.do"
    _inherit=['mail.thread','mail.activity.mixin']
    _description = "Task"
    name=fields.Char(required=True)
    description =fields.Text(tracking=True)
    due_date = fields.Datetime(required=True, tracking=True)
    status = fields.Selection([
        ("new","New"),
        ("in_progress","In progress"),
        ("completed","Completed"),
        ("close","Close"),], default="new", tracking=True)
    assign_to = fields.Many2one("res.users", string="Assign To")
    line_ids = fields.One2many("estimated.time","task_id")
    expected_time = fields.Float(string="Expected Time")
    time_taken = fields.Float(string="Time Taken", compute="_compute_time_taken",store=True)
    remaining_time = fields.Float(string="Remaining Time", compute="_compute_remaining_time")
    active = fields.Boolean(default=True)
    is_late = fields.Boolean(compute="_compute_is_late")

    
    @api.depends('due_date')
    def _compute_is_late(self):
        for rec in self:
            if rec.due_date and rec.due_date < fields.Datetime.now():
                rec.is_late = True
            else:
                rec.is_late = False

    @api.depends('line_ids.time_taken')
    def _compute_time_taken(self):
        for rec in self:
            rec.time_taken = sum(rec.line_ids.mapped('time_taken'))
            
    @api.constrains('time_taken','expected_time')
    def check_taken_time(self):
        for rec in self :
            if rec.time_taken > rec.expected_time:
                raise ValidationError("Taken time shouldn't be bigger than expected time")
            
    @api.depends('expected_time', 'time_taken')
    def _compute_remaining_time(self):
        for rec in self:
            rec.remaining_time = rec.expected_time - rec.time_taken

    def new_action(self):
        for rec in self:
            rec.status="new"
    
    def in_progress_action(self):
        for rec in self:
            rec.status="in_progress"
    
    def completed_action(self):
        for rec in self:
            rec.status="completed"
    
    def close_action(self):
        for rec in self:
            rec.status="close"