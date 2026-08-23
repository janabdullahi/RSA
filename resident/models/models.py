# -*- coding: utf-8 -*-

from odoo import models, fields, api


class resident(models.Model):
    _name = 'resident.resident'
    _description = 'resident.resident'

    tenant_name = fields.Char('Name', required=True)
    tenant_middle_name = fields.Char('Middle Name')
    tenant_last_name = fields.Char('Last Name', required=True)
    tenant_move_in_date = fields.Datetime('Move in', required=True)
    tenant_move_out_date = fields.Datetime('Move out')
    tenancy_start_date = fields.Datetime('Tenancy start Date', required=True)
    tenancy_end_date = fields.Datetime('Tenancy end Date')
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