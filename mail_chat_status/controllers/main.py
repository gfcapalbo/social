# -*- coding: utf-8 -*-

from odoo.http import request
from odoo.addons.bus.controllers.main import BusController


class BusController(BusController):

    def _poll(self, dbname, channels, last, options):
        if request.uid:
            partner = request.env.user.partner_id
            if 'bus_presence_partner_ids' in options:
                options['bus_presence_partner_ids'].append(partner.id)
            else:
                options['bus_presence_partner_ids'] = [partner.id]

        return super(BusController, self)._poll(
            dbname, channels, last, options,
        )
