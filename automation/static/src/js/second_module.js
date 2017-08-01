odoo.define('automation_second', function (require) {
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');
var Model = require('web.Model');
// var session = require('web.session');
// var PlannerCommon = require('web.planner.common');
// var framework = require('web.framework');
// var webclient = require('web.web_client');
// var PlannerDialog = PlannerCommon.PlannerDialog;

// var QWeb = core.qweb;
// var _t = core._t;

var PreView = Widget.extend({
	template: 'PreView',
    init: function(){
        console.log("Initialising Second module");
        this._super();
    },
    events: {
        'click button.create_button': function () {
            
            // var my_widget = new PostView();
            var out = this.$el;
            // console.log(out);
            // console.log(my_widget);
            // my_widget.appendTo(".second");
            // new PostView().appendTo(".second");
            // console.log(this);
            new PostView().replace(this.$el);
            console.log("Create Button Clicked");
            // 

            // new PostView().replace($)
        }
        // 'click button.create_button': 'PostView';
    },

    start: function(){
    	console.log("started");
    	// this.$el.append("<div>Hello dear Odoo user!</div>");
		this.$el.append("<div>Create New!!!</div>" +
			"<button class='create_button'>Create</button>");
        // console.log(this.$el)
        // this._super();
    }
});

var PostView = Widget.extend({
    template: 'PostView',
    init: function(){
        console.log("Initialising Second module form");
        // this._super();
    },
   

    start: function(){
        console.log("started second form");
        // this.$el.append("<div>Hello dear Odoo user!</div>");
        console.log("View Displayed");
        // this.$el.append("<div>Create New!!!</div>" +
        //     "<button class='create_button'>Create</button>");
        // this._super();
    }

});

core.action_registry.add('automation_second.main', PreView);
// core.action_registry.add('automation_second.main', PView);
// return {
//     PreView: PreView,
//     PostView: PostView,
// };

});
