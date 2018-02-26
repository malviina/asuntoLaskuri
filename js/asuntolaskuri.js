
var app = angular.module('asuntoLaskuri', [])
.controller('AsuntoLaskuriController', function($scope, $http) {
    var asuntoLaskuri = this;
/*   $scope.data = [
        {"paikka": 'Helsinki', "vuokra": [22, 5]},
        {"paikka": 'Vantaa', "vuokra": [12,5]}];*/
    
    $http.get("./data.json").then(function(response) {
        $scope.data = response.data;
    })
    $scope.vuokralla = "";
    $scope.omistus = "";
    
    $scope.paikkakuntaKysytty = false;
    $scope.neliotKysytty = false;
    $scope.vuokraKysytty = false;

    $scope.laskettu = false;
    $scope.vuokra = "";
    $scope.neliot = "";
    $scope.suurempiVaiPienempi = "";
    
    
// LASKURI KYSYMYKSET //
    
    $scope.paikkakuntaSelected = function() {
        if ($scope.paikkakuntaKysytty) {
            $scope.laskeVuokra();
        } else {
            $scope.kysyNeliot();
        }
    }
    
    $scope.vuokraSelected = function() {
        $scope.vuokraKysytty = true;
        $scope.laskeVuokra();
    }
    
    
    $scope.kysyNeliot = function() {
        $scope.paikkakuntaKysytty = true;
        //$scope.neliotKysytty = false;
        //$scope.vuokraKysytty = false;
    }
    
    $scope.kysyVuokra = function() {
        if ($scope.laskettu) {
            $scope.laskeVuokra();
        }
        $scope.paikkakuntaKysytty = true;
        $scope.neliotKysytty = true;
        if (!$scope.vuokralla) {
            $scope.laskeVuokra();
        }
        //$scope.vuokraKysytty = false;
    }
    
    
    $scope.laskeVuokra = function() {
        var kerroin = $scope.selectPaikkakunta.kerroin;
        var elmnt = document.getElementById("laskettuVuokra");
        $scope.laskettuVuokra =Math.pow($scope.neliot, 2) * kerroin[0] + $scope.neliot * kerroin[1] + kerroin[2];
        if ($scope.paikkakuntaKysytty && $scope.neliotKysytty) {
            $scope.laskettu = true;
            if ($scope.laskettuVuokra < $scope.vuokra) {
                $scope.suurempiVaiPienempi = "suurempi";
                $scope.onnittelut = "Harmin paikka!"
            } else {
                $scope.suurempiVaiPienempi = "pienempi";
                $scope.onnittelut = "Onneksi olkoon!"
            }
        };
        
    }
    

    
// LASKURI VASTAUKSET //

});

app.directive('isEnter', function () {
return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.isEnter);
                });

                event.preventDefault();
            }
        });
    };
});


