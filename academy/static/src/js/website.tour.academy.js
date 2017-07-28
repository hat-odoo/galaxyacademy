odoo.define('academy.tour', function (require) {
'use strict';

var tour = require('web_tour.tour');
var base = require("web_editor.base");

tour.register('teacher_view', {
    test: true,
    url: '/',
    wait_for: base.ready()
},
    [
        {
            content: "Go to the `Lester` page",
            trigger: 'a:contains("Teachers")',
        },
        {
            content: "got to lester page",
            trigger: 'a:contains("Lester Vaughn")',
            // trigger: 'select:eq(0)',
            // run: 'text 1',
        },
        {
            content: "Got to Course Button",
            // extra_trigger: 'select:eq(0):has(option:contains(1):propSelected)',
            trigger: 'a:contains("Courses")',
            // run: 'text 2',
        },
        {
            content: "Select Some of Courses",
            // extra_trigger: 'select:eq(1):has(option:contains(2):propSelected)',
            trigger: 'a:contains("Course_Management_Training")',
        }
    ]
);

});
