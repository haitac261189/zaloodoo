# -*- coding: utf-8 -*-
{
    'name': "zalo_message",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_management',
        'purchase',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/res_partner_views.xml',
        'views/res_config_setting_views.xml',
        'views/zalo_message_history.xml',
        'wizard/zalo_form_message_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/message_form.xml'
    ],
}
