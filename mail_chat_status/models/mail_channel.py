# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from email.utils import formataddr

import re
import uuid

from odoo import _, api, fields, models, modules, tools
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools import ormcache
from odoo.tools.safe_eval import safe_eval


class BusPresenceType(models.Model):
    _name = 'bus.presence.type'

    present = fields.Boolean()
    description = fields.Char()

    """
    Insert data records
        present = TRUE
        NAME:
        'Avaliable'
        'In the Zone'
        'In conference'

        Present = False
        NAME:
         'LUNCH'
         'BREAK'
    """




class BusPresence(models.Model):
    _inherit = 'bus.presence'

    """
    bus presence is used by chat_manager js
    in mail module to establish the status of
    the user in channels that are of type "dm".
    this will then be rendered as status.

    We want to extend these statuses.
    with a descriptor.

    We will also add the possibility to change status description
    manually.
    """
    status_description = fields.Many2one(
        'bus.presence.type'
        compute='_compute_status_description'
        inverse='_inverse_status_description'

    @depends('status')
    def _compute_status_description(self):
        if self.status == 'online':
            # this will take care of automatic unsetting
            self.status_description = self.env.ref(
                'XMLID of available state')


    def _inverse_status_description(self):
        if self.status_description.

