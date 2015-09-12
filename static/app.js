var app= angular.module('vid',[]);

app.controller("getvideos",['$scope',function($scope){
    console.log("called");
    $scope.name="hello";
  $http.get('52.89.20.199:2358/').then(function(response) {
    // this callback will be called asynchronously
    // when the response is available
       console.log("success");
       console.log(response);
  }, function(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status
       console.log("error")
       console.log(response)
  });
    
}]);



app.controller("getvid",function($scope,$http){
   $scope.name="hello"; 
   $http.get('/').then(function(response) {
    // this callback will be called asynchronously
    // when the response is available
       console.log("success");
       console.log(response);
  }, function(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status
       console.log("error")
       console.log(response)
  });     
});