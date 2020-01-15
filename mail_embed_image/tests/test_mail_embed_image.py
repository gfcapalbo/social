# -*- coding: utf-8 -*-
# Copyright 2019 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from base64 import b64encode
from lxml import html
from requests import get
from odoo.addons.mail.tests.common import TestMail


class TestMailEmbedImage(TestMail):

    def setUp(self):
        super(TestMailEmbedImage, self).setUp()
        # DATA
        base_url = self.env['ir.config_parameter'].get_param(
            'web.base.url')
        image_url = base_url + \
            '/mail_embed_image/static/description/icon.png'
        image = get(image_url).content
        body = html.tostring(html.fromstring("""
            <div>
            this is an email
            <img src="base64: %s"></img>
            <img src="%s"></img>
            <img src="%s"></img>
            </div>""" % (
            b64encode(image),
            image_url,
            '/web/image/res.partner/1/image',
            )))
        email_from = 'test@example.com'
        email_to = 'test@example.com'
        subject = 'test mail'
        self.email = self.env['ir.mail_server'].build_email(
            email_from, email_to, subject,
            body, subtype='html', subtype_alternative='plain')
        # END DATA

    def test_mail_embed_image(self):
        """We pass a mail with <img src="..." /> tags to build_email,
        and then look into the result, check there were attachments
        created and you find xpaths like //img[src] have a cid"""
        images_in_mail = 0
        for part in self.email.walk():
            if part.get_content_type() == 'text/html':
                # we do not search in text, just in case that texts exists in
                # the text elsewhere (not probable, but this is better)
                images_in_mail += len(
                    html.fromstring(
                        part.get_payload(decode=True)
                    ).xpath("//img[starts-with(@src, 'cid:')]")
                )
        # verify 1 replaced image
        self.assertEqual(images_in_mail, 1)
        # verify 1 attachment present
        self.assertEqual([
            x.get_content_type() for x in self.email.walk(
            ) if x.get_content_type().startswith('image/')], ['image/png'])
