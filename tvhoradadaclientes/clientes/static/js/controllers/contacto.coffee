angular.module "contacto", []

.controller "contactoController", [
    "$scope"
    "flash"
    "Restangular"
    ($scope, flash, Restangular) ->
        contacto = Restangular.all("contacto")

        $scope.submit = () ->
            contacto.post($scope.contacto)
                .then (result) ->
                    flash.success = result.message
                    $scope.contacto = {}


]
