angular.module "consumo", []

.controller "consumoController", [
    "$scope"
    "clientes"
    "$filter"
    ($scope, clientes, $filter) ->
        $scope.pageSize = 10
        todos = 'Todos mis números'
        $scope.telefono = todos

        clientes.one("current/consumos")
            .getList()
            .then (consumos) ->
                $scope.consumos = consumos
                $scope.setPage(1)
                $scope.telefonos = _.reduce consumos, (result, item) ->
                    result.push item.TelOrigen if item.TelOrigen not in result
                    result
                , [todos]


        $scope.setPage = (page) ->
            $scope.filter($scope.buscar, page)

        filtradoPorTelefono = (consumos, telefono) ->
            if telefono != todos
                consumos = _.filter(consumos, (item) -> item.TelOrigen == telefono)
            consumos

        filtradoPorBusqueda = (consumos, query) ->
            if query
                consumos = $filter('filter')(consumos, query)
            consumos

        $scope.filter = (query, page = 1) ->
            if $scope.consumos?
                consumos_filtrados = filtradoPorTelefono(filtradoPorBusqueda($scope.consumos, query), $scope.telefono)
                desde = (page - 1) * $scope.pageSize
                $scope.consumos_paginados = consumos_filtrados[desde .. ]

                $scope.totalItems = consumos_filtrados.length



        $scope.getTipo = (tipo) ->
            switch tipo
                when 'M' then 'Móvil'
                when 'N' then 'Nacional'
                when 'I' then 'Internacional'
                when 'R' then 'Otros'

        $scope.$watch 'buscar', (query) ->
            $scope.filter query


        $scope.$watch 'telefono', () ->
            $scope.filter $scope.buscar
]
