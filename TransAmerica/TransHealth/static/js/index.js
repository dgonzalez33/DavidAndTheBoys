
var app = angular.module('healthForm', []);
app.controller('questionair', function($scope) {
	$scope.submit = function() {
	 var data = {salary: $scope.salary, age: $scope.age, height: $scope.height, weight: $scope.weight  };
        var config = {
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
            }
        }
        $http.post('/setInformation/', data, config)
        .success(function (data, status, headers, config) {
            $scope.result = data;
        })
        .error(function (data, status, header, config) {
            $scope.result = "Data: " + data +
                "<hr />status: " + status +
                "<hr />headers: " + header +
                "<hr />config: " + config;
        });

	console.log($scope.result);        
        }
        $scope.submit();
});
