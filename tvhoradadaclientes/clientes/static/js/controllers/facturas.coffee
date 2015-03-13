angular.module "facturas", []

.controller "facturasController", [
    "$scope"
    "Restangular"
    "$modal"
    "$location"
    ($scope, Restangular, $modal, $location) ->
        facturas = Restangular.all("facturas")

        facturas.getList()
            .then (facturas) ->
                $scope.facturas = facturas
                $scope.years = _.reduce facturas, (result, item) ->
                    result.push item.Ejercicio if item.Ejercicio not in result
                    result
                , []
                $scope.year = $scope.years[$scope.years.length - 1]

        $scope.filtrado = (item) ->
            item.Ejercicio == $scope.year

        $scope.detalles = (item) ->
            modalInstance = $modal.open
                templateUrl: 'detalle_factura.html',
                controller: "facturaDetalleController"
                resolve:
                    factura: () -> facturas.one(parseInt(item.IdFacv))
                    item: () -> item

        $scope.Entero = (item) ->
            parseInt(item)

        $scope.descargar = (factura) ->
            document.location = "/descargar/factura/#{parseInt(factura.IdFacv)}"
]


.controller "facturaDetalleController", [
    "factura"
    "item"
    "$scope"
    "$modalInstance"
    (factura, item, $scope, $modalInstance) ->
        $scope.Entero = (item) -> parseInt(item)
        $scope.factura = item

        factura.getList("lineas")
            .then (data) ->
                $scope.lineasFactura = data

        $scope.close = () ->
            $modalInstance.close();
]
