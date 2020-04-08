odoo.define('mail_chat_status.chat_manager', function (require) {
    "use strict";
    var chat_manager = require('mail.chat_manager');

    chat_manager.include({
        make_channel: function (data, options) {
            debugger;
            channel = this._super.apply((data,options);
            if (channel_type == "dm") {
                channel.direct_partner = data.direct_partner[0]
                channel.status_description = channel.direct_partner.status_description
            }
            return channel
        }
    })

});

