// Generated by CoffeeScript 1.7.0
(function() {
  angular.module("tvh.services", []).factory("clientes", [
    "Restangular", function(Restangular) {
      return Restangular.all("clientes");
    }
  ]).filter("moneda", function() {
    return function(item) {
      return oot.formatNumber(oot.toFloat(item)) + "€";
    };
  }).filter("numero", function() {
    return function(item) {
      return oot.formatNumber(oot.toFloat(item));
    };
  });

}).call(this);

//# sourceMappingURL=services.map
