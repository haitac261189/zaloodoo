console.log('bbccdd')
odoo.define('sim_zalo_message/static/src/js/message_form.js', function (require) {
    'use strict';

    var ChatterTopbar = require('mail/static/src/components/chatter_topbar/chatter_topbar.js');

    const components = {
        FollowButton: require('mail/static/src/components/follow_button/follow_button.js'),
        FollowerListMenu: require('mail/static/src/components/follower_list_menu/follower_list_menu.js'),
    };
    // const PosIotProductScreen = ChatterTopbar =>
    //     class extends ChatterTopbar {
    //         _onClickSendZaloMessage() {
    //             console.log('click');
    //         }
    //     };
    //
    // ChatterTopbar.Component.extend(ChatterTopbar, PosIotProductScreen);
    //
    // return ChatterTopbar;

    // class ZaloChatterTopbar extends ChatterTopbar {
    //
    //     _onClickSendZaloMessage(ev) {
    //         console.log('click');
    //     }
    // };

    class ZaloChatterTopbar extends ChatterTopbar {

        /**
         * @override
         */
        constructor(parent, props) {
            super(parent, props);
            /* Here you can add useState, useRef... */
        }

        _onClickSendZaloMessage(ev) {
            console.log('kokokookokp');
        }
    };
    //
    // Object.assign(ZaloChatterTopbar);
    //
    // return ZaloChatterTopbar;
    // Object.assign(ZaloChatterTobbar);

    // Object.components.ChatterTopbar = ZaloChatterTobbar;

    // Object.assign(ZaloChatterTopbar, {
    //
    //     components,
    //     props: {
    //         chatterLocalId: String,
    //     },
    //     template: 'mail.ChatterTopbar',
    // });
    // console.log('lddddddd');
    // return ZaloChatterTopbar;
});

