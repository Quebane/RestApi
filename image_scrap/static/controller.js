var imageScrapyApp = angular.module('ImageScrapy', []);

imageScrapyApp.controller('ImageScrapyController', function ($rootScope, $http) {
    $http.get('../').success(function(data) {
      $rootScope.images = data;
    });
});

imageScrapyApp.controller('ImageForm', function($scope,$rootScope, $http) {
    $scope.submit = function() {
        var in_data = { "url": $scope.url, "description": $scope.description };
        $http.defaults.headers.post.Authorization = "Token 0759702048e0a16f6c1ea0031247124dd58cfdc0";
        $http.defaults.headers.post.contentType = "application/json";
        $http.post('../', in_data)
            .success(function(out_data) {
                $rootScope.images.push(out_data);
            });
    }
});