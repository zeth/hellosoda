'use strict';

angular.
    module('core.directory').
    factory('Person', ['$resource',
                       function($resource) {
                           return $resource('/api/person/:personId', {}, {
                               query: {
                                   method: 'GET',
                                   params: {personId: 'people'},
                                   isArray: true
                               }
                           });
                       }
                      ]);
