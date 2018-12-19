/*
WeinersNotLosers - Daniel Gelfand and Joshua Weiner
SoftDev1 pd6
K#28 -- Sequential Progression
2018-12-19 W
*/
var fibonacci = function(n){
  if(n == 0){
    return 0;
  }

  if(n < 3){
    return 1;
  }
  //Recursion
  return fibonacci(n-1) + fibonacci(n-2);
};

//Euclidean Algorithm
var gcd = function(a,b){

  if(a == 0){
    return b;
  }

  if(b == 0){
    return a;
  }
  var remainder = (Math.max(a,b)%Math.min(a,b));

  return gcd(Math.min(a,b),remainder);
}


var names = ["Bob", "Josh", "Kaitlin", "Jeff", "Brooks", "Pam"];

var randomStudent = function(nameList){
  //Random index within the length of the provided list
  return nameList[Math.floor(Math.random() * (nameList.length))];
}


// FUNCTION CALLS //
console.log("Fibonacci test cases, should print 0, 1, 1, 2, 3");
console.log(fibonacci(0));
console.log(fibonacci(1));
console.log(fibonacci(2));
console.log(fibonacci(3));
console.log(fibonacci(4));

console.log("GCD Test cases, expecting 2 then 1:");
console.log(gcd(6, 2));
console.log(gcd(7, 3));

console.log("Random Student Tests, expecting random output!");
console.log(randomStudent(names));
console.log(randomStudent(names));
console.log(randomStudent(names));
