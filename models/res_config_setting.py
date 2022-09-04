# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigZaloSmsSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_setting = fields.Boolean(string='Zalo API', store=True)
    access_token = fields.Char('OA Access Token')

    @api.model
    def get_values(self):
        res = super().get_values()
        res.update(
            is_setting=self.env['ir.config_parameter'].sudo().get_param('zalo_message.is_setting'),
            access_token=self.env['ir.config_parameter'].sudo().get_param('zalo_message.access_token')
        )
        return res

    def set_values(self):
        super().set_values()
        param = self.env['ir.config_parameter'].sudo()

        field_is_setting = True and self.is_setting or False
        field_access_token = self.access_token and self.access_token or False

        if not field_is_setting:
            field_is_setting = None

        param.set_param('zalo_message.is_setting', field_is_setting)
        param.set_param('zalo_message.access_token', field_access_token)
