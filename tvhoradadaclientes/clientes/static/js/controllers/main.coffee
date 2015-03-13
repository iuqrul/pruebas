angular.module "main", []

.controller "mainController", [
    "$scope"
    "clientes"
    "flash"
    ($scope, clientes, flash) ->

        clientes.getList()
            .then (data) ->
                $scope.cliente = data[0]

        $scope.enviar = () ->
            clientes.post($scope.cliente)
                .then (data) ->
                    flash.success = "Su solicitud de cambio de información ha sido enviada."

                .catch () ->
                    console.log "error"
                    flash.error = "Ha ocurrido un error enviando los datos, pruebe más tarde."



]
