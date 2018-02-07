'use strict';

// Register `people` component, along with its associated controller and template
angular.
  module('people').
  component('people', {
    templateUrl: 'people/people.template.html',
    controller: ['Person',
      function PeopleController(Person) {
        this.people = Person.query();
        this.orderProp = 'age';
      }
    ]
  });
