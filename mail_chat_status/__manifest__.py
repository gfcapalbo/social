# -*- coding: utf-8 -*-
# Copyright 2020 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "mail_chat_status",
    "version": "12.0.1.0.0",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Mail",
    "summary": "Adds statuses to chat users",
    "depends": [
        'mail',
    ],
    "data": [
   #     'views/assets.xml',
    ],
    "qweb": [
        'static/src/xml/chat_extension.xml',
    ],
    "installable": True,
}
