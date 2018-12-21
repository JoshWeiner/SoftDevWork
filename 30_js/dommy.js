/*
WeinersNotLosers - Daniel Gelfand and Joshua Weiner
SoftDev1 pd06
K #30: Sequential Progression III: Season of the Witch
2018-12-21
*/

/*
0. Define necessary functions
*/
//Sets heading to list item content when the mouse is over the list item
var setHeading = function(e) {
    var h = document.getElementById("h")
    h.innerHTML = e
};
//Changes heading back to default when mouse is no loger over the list item
var changeBack = function() {
  var h = document.getElementById("h");
  h.innerHTML = "Hello World!";
}
//Removes item from list
var remove = function(e) {
    //console.log(e);
    //console.log(e.target);
    var toRemove = e.target;
    toRemove.parentNode.removeChild(toRemove);
};

/*
1. Iterate through list items, give them functions with event listeners
*/
var L = document.getElementsByTagName("li");
for (var i=0; i<L.length; i++) {
    L[i].addEventListener('click', remove);
    L[i].addEventListener('mouseover',
      function (e) {
        setHeading(this.innerHTML);
      });
    L[i].addEventListener('mouseout', changeBack);
};

/*
2. Add new list items to the current list
*/
var addToList = function(e) {
    var list = document.getElementById("thelist");
    var listItem = document.createElement("li");
    listItem.innerHTML="WORD";
    listItem.addEventListener('click', remove);
    listItem.addEventListener('mouseover',
      function (e) {
        setHeading(this.innerHTML);
      });
    listItem.addEventListener('mouseout', changeBack);
    list.appendChild(listItem);
};

var button = document.getElementById("b");
button.addEventListener('click', addToList);

/*
3. Add fibonacci function and event listeners
*/
//Fibonacci sequence function
var fibonacci = function(n) {
    if (n == 0)
      return 0;
    else if (n < 3)
      return 1;
    else
      return fibonacci(n - 1) + fibonacci(n - 2);
}

//Add to the fibonacci ordered list sequence
var n = 0;
var addToFib = function(e) {
    var list = document.getElementById("fiblist");
    var listItem = document.createElement("li");
    listItem.innerHTML = fibonacci(n);
    list.appendChild(listItem);
    n++;
};

//Add event listener to fibonacci button
var fb = document.getElementById("fb");
fb.addEventListener("click", addToFib);
