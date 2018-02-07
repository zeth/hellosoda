'use strict';

// Register `person` component, along with its associated controller and template
angular.
    module('person').
    component('person', {
        templateUrl: 'person/person.template.html',
        controller: ['$routeParams', 'Person',
                     function PersonController($routeParams, Person) {
                         var self = this;
                         self.person = Person.get({personId: $routeParams.personId}, function(person) {
                             self.setImage(person.personal.avatar);
                         });

                         self.setImage = function setImage(imageUrl) {
                             self.mainImageUrl = imageUrl;
                         };
                     }
                    ]
    });

