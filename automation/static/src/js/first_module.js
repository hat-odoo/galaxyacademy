odoo.define('automation', function (require) {
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');
// var Model = require('web.Model');
// var session = require('web.session');
// var PlannerCommon = require('web.planner.common');
// var framework = require('web.framework');
// var webclient = require('web.web_client');
// var PlannerDialog = PlannerCommon.PlannerDialog;

// var QWeb = core.qweb;
// var _t = core._t;

var Frontview = Widget.extend({
	template: 'first_module',
    init: function(){
        console.log(":::::INIT");
        this._super();
    },
    events: {
        'click button.save_button': function () {
            console.log("Save Button Clicked");

            //this.trigger('user_chose', true);
        },
        'click button.cancel_button': function () {
            //this.trigger('user_chose', false);
            console.log("Cancel Button Clicked");
        }
    },

    start: function(){
    	console.log("started");
  //   	this.$el.append("<div>Hello dear Odoo user!</div>");
		this.$el.append("<div>Are you sure you want to perform this action?</div>" +
			"<button class='save_button'>Save</button>" +
			"<button class='cancel_button'>Cancel</button>");
    }
});

core.action_registry.add('automation.main', Frontview);

});
