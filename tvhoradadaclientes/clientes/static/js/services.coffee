angular.module("tvh.services", [])

.factory "clientes", [
    "Restangular"
    (Restangular) ->
        return Restangular.all("clientes")
]


.filter("moneda", ->
    (item) ->
        oot.formatNumber(oot.toFloat(item)) + "€"
)

.filter("numero", ->
    (item) ->
        oot.formatNumber oot.toFloat(item)
)
