# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Resident(models.Model):
    _name = 'resident.resident'
    _description = 'resident.resident'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    tenant_name = fields.Char('First Name', required=True)
    tenant_middle_name = fields.Char('Middle Name')
    tenant_last_name = fields.Char('Last Name', required=True)
    tenant_move_in_date = fields.Datetime('Move In', required=True)
    tenant_move_out_date = fields.Datetime('Move Out')
    tenancy_start_date = fields.Datetime('Tenancy Start Date', required=True)
    tenancy_end_date = fields.Datetime('Tenancy End Date')
    Tenancy_duration = fields.Selection([
        ('less', 'Less than 6 Month'),
        ('6month', '6 Month'),
        ('12month', '1 Year'),
        ('18month', '1.5 Year'),
        ('24month', '2 Year'),
        ('more', 'More'),
    ])
    pets = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string="Pets")
    letting_agent = fields.Char()
    parking = fields.Char()
    private_phone = fields.Char()
    private_email = fields.Char()