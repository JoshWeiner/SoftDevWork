/*
WeinersNotLosers - Daniel Gelfand and Joshua Weiner
SoftDev1 pd6
K#28 -- Sequential Progression
2018-12-19 W
*/
var fibonacci = function(n) {
  if(n == 0){
    return 0;
  }

  if(n < 3){
    return 1;
  }
  //Recursion
  return fibonacci(n-1) + fibonacci(n-2);
};

//EuclIdean Algorithm
var gcd = function (a,b){

  if(a == 0){
    return b;
  }

  if(b == 0){
    return a;
  }
  var remainder = (Math.max(a,b)%Math.min(a,b));

  return gcd(Math.min(a,b),remainder);
};


var names = ["Bob", "Josh", "Kaitlin", "Jeff", "Brooks", "Pam"];

var randomStudent = function(nameList){
  //Random index within the length of the provIded list
  return nameList[Math.floor(Math.random() * (nameList.length))];
};


// // FUNCTION CALLS //
// console.log("Fibonacci test cases, should print 0, 1, 1, 2, 3");
// console.log(fibonacci(0));
// console.log(fibonacci(1));
// console.log(fibonacci(2));
// console.log(fibonacci(3));
// console.log(fibonacci(4));
//
// console.log("GCD Test cases, expecting 2 then 1:");
// console.log(gcd(6, 2));
// console.log(gcd(7, 3));
//
// console.log("Random Student Tests, expecting random output!");
// console.log(randomStudent(names));
// console.log(randomStudent(names));
// console.log(randomStudent(names));

var do_fib = function () {
  var fn = document.getElementById("fib_num").value;
  console.log("Fibonacci: " + fibonacci(fn));
};


var do_gcd = function() {
  var gcdOne = document.getElementById("gcd1").value;
  var gcdTwo = document.getElementById("gcd2").value;
  console.log("GCD: " + gcd(gcdOne, gcdTwo));
}

var get_student = function () {
  console.log("Random student: " + randomStudent(names));
}

var fib = document.getElementById("fib");
fib.addEventListener('click', do_fib);

var get_gcd = document.getElementById("gcd");
get_gcd.addEventListener('click', do_gcd);

var randstud = document.getElementById("randstud");
randstud.addEventListener('click', get_student);
