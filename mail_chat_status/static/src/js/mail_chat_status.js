odoo.define('mail_chat_status.chat_manager', function (require) {
    "use strict";
    var chat_manager = require('mail.chat_manager');

chat_manager.include({
     function make_channel (data, options) {
            debugger;
            channel = this._super(data, options);
            if (channel_type == "dm") {
                channel.direct_partner = data.direct_partner[0]
                channel.status_description = channel.direct_partner.status_description
            }
            return channel
        }
    })

});

