# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    message_count = fields.Integer('Message')

    def action_send_zalo_message(self):
        message = 'Hello ' + self.partner_id.name + '. Your order ' + self.name + ' amounting in $' + str(
            self.amount_total) + ' has been confirmed. Thank you for your trust!'

        ctx = {
            'default_recipient_ids': [(6, 0, self.partner_id.ids)],
            'default_source_origin': self.name,
            'default_content': message,
            'default_model': 'purchase.order'
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'zalo.form.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }

    def action_open_message_history(self):
        order_name = self.name
        action = self.env.ref('zalo_message.zalo_message_history_action').read()[0]
        action['domain'] = [('source_document', '=', order_name)]
        return action
