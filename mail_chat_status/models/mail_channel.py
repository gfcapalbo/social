# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


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

    not_present = [('away', 'Away'), ('lunch', 'Lunch')]
    present = [
        ('available', 'Available'),
        ('concentrated', 'Concentrated'),
        ('meeting', 'Meeting/client'), ]
    present_not_present = not_present + present

    presence = fields.Boolean(compute='compute_presence')
    status_description = fields.Selection(
        present_not_present, default='available', required=True)

    @api.depends('status_description')
    def compute_presence(self):
        for this in self:
            if this.status_description in zip(*self.present)[0]:
                this.presence = True
                continue
            this.presence = False
