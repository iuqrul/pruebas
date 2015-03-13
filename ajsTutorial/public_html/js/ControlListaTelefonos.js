var tutorialApp = angular.module('tutorialApp', []);

tutorialApp.controller('ControlListaTelefonos', function($scope) {
    $scope.telefonos = [
        {'nombre': 'Nexus S', 'descripcion': 'Rápido es más rápido con Nexus S.', 'edad': 1},
        {'nombre': 'Motorola XOOM™ con Wi-Fi', 'descripcion': 'La siguiente generación de tabletas.', 'edad': 3},
        {'nombre': 'MOTOROLA XOOM™', 'descripcion': 'La siguiente generación de tabletas.', 'edad': 2}
    ];
    
    $scope.mundo = "Mundo";
    //$scope.orderProp="edad";
});