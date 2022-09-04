# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MessageHistory(models.Model):
    _name = 'zalo.message.history'

    recipient = fields.Char('Recipient')
    message_type = fields.Char('Message Type')
    content = fields.Text('Message Content')
    file = fields.Binary('File')
    source_document = fields.Char('Source Document')
