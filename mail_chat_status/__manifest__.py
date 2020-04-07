# -*- coding: utf-8 -*-
# Copyright 2020 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "mail_chat_status",
    "version": "10.0.1.0.0",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Mail",
    "summary": "Adds statuses to chat users",
    "depends": [
        'mail',
    ],
    "data": [
    ],
    "qweb": [
        'views/chat_extension.xml',
    ],
    "test": [
    ],
    "images": [
    ],
    "pre_init_hook": False,
    "post_init_hook": False,
    "uninstall_hook": False,
    "auto_install": False,
    "installable": True,
    "application": False,
    "external_dependencies": {
        'python': [],
    },
}
