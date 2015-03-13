"use strict"

# El archivo de configuración de la aplicación
# Aquí se configuran las rutas y servicios.

angular.module "tvh", [
    'ui.router'
    'ui.bootstrap'
    'ngAnimate'
    'restangular'
    'angular-flash.service'
    'angular-flash.flash-alert-directive'

    'main'
    'facturas'
    'consumo'
    'contacto'

    'tvh.services'
]

.config [

    '$httpProvider'
    '$stateProvider'
    '$urlRouterProvider'
    'RestangularProvider'
    'flashProvider'
    ($httpProvider, $stateProvider, $urlRouterProvider, RestangularProvider, flashProvider) ->
        flashProvider.errorClassnames.push('alert-danger')

        RestangularProvider.setBaseUrl "/api/v1"
        $httpProvider.defaults.xsrfCookieName = "csrftoken"
        $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken"

        $stateProvider
            .state "home",
                url: "/"
                templateUrl: "/static/views/datos.html"
                controller: "mainController"

            .state "facturas",
                url: "/facturas"
                templateUrl: "/static/views/facturas.html"
                controller: "facturasController"

            .state "consumo",
                url: "/consumo"
                templateUrl: "/static/views/consumo.html"
                controller: "consumoController"

            .state "contacto",
                url: "/contacto"
                templateUrl: "/static/views/contacto.html"
                controller: "contactoController"

        $urlRouterProvider.otherwise "/"
]
