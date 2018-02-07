'use strict';

angular.
  module('directoryApp').
  config(['$locationProvider' ,'$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');

      $routeProvider.
        when('/people', {
          template: '<people></people>'
        }).
        when('/people/:personId', {
          template: '<person></person>'
        }).
        otherwise('/people');
    }
  ]);
