# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    zalo_id = fields.Char('Zalo Id')
