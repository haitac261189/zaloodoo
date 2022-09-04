import requests
import json

from odoo import fields, models
from odoo.exceptions import ValidationError


class ZaloFormMessage(models.TransientModel):
    _name = 'zalo.form.message'

    recipient_ids = fields.Many2many('res.partner', string='Recipients')
    message_type = fields.Selection(string='Message Type',
                                    selection=[('text', 'Text Message'), ('image', 'Image Message'),
                                               ('file', 'File Message')], default="text")
    content = fields.Text('Content')
    file = fields.Many2many('ir.attachment', string="File")
    file_name = fields.Char()

    def get_token(self):
        try:
            if self.env['ir.config_parameter'].sudo().get_param('zalo_message.is_setting'):
                token = self.env['ir.config_parameter'].sudo().get_param('zalo_message.access_token')
                return token
        except Exception as e:
            raise ValidationError(e)

    def get_attachment_id(self):
        if self.file:
            file_path = self.file.local_url
            access_token = self.get_token()
            url = 'https://openapi.zalo.me/v2.0/oa/upload/file?access_token=' + str(access_token)
            headers = {
                'Content-Type': 'application/json',
                'Content-Disposition': 'form-data',
            }
            data = {"file": "localhost:8069" + file_path}

            data = json.dumps(data, indent=4)
            data = data.replace(" ' ", ' " ')
            response = requests.post(url, data=data, headers=headers)
            print(response.content)
            return response.text
        else:
            raise ValidationError('You have not selected file.')

    def action_send(self):
        access_token = self.get_token()
        url = 'https://openapi.zalo.me/v2.0/oa/message?access_token=' + str(access_token)
        headers = {
            'Content-Type': 'application/json'
        }
        message = self.content
        user_id = self.recipient_ids.zalo_id
        if self.message_type == 'text':
            data = {
                "recipient": {
                    "user_id": user_id
                },
                "message": {
                    "text": message
                }
            }
        else:
            attachment_id = self.get_attachment_id()
            data = {
                "recipient": {
                    "user_id": user_id
                },
                "message": {
                    "attachment": {
                        "payload": {
                            "token": 'attachment_id.token'
                        },
                        "type": "file"
                    }
                }
            }
        data_json = json.dumps(data, indent=4)
        data_json.replace(" ' ", ' " ')
        requests.post(url, data=data_json, headers=headers)
        so_message = self.env['sale.order'].browse(self._context['active_id'])
        po_message = self.env['purchase.order'].browse(self._context['active_id'])
        if self._context['active_model'] == 'sale.order':
            source_document = so_message.name
            self.env['zalo.message.history'].sudo().create({
                'recipient': self.recipient_ids.name,
                'message_type': dict(self._fields['message_type'].selection).get(self.message_type),
                'content': self.content,
                'source_document': source_document
            })
            so_message_count = self.env['zalo.message.history'].sudo().search(
                [('source_document', '=', source_document)])
            so_message.message_count = len(so_message_count)
        else:
            source_document = po_message.name
            self.env['zalo.message.history'].sudo().create({
                'recipient': self.recipient_ids.name,
                'message_type': dict(self._fields['message_type'].selection).get(self.message_type),
                'content': self.content,
                'source_document': source_document
            })
            po_message_count = self.env['zalo.message.history'].sudo().search(
                [('source_document', '=', source_document)])
            po_message.message_count = len(po_message_count)
