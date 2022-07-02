var a=[2,8,7,55,6,2,11,4]
 var swaps=0;
  for (var i = 0; i < a.length; i++) {
    // Last i elements are already in place
    for (var j = 0; j < a.length - i - 1; j++) {
      // Checking if the item at present iteration
      // is greater than the next iteration
      if (a[j] > a[j + 1]) {
        // If the condition is true then swap them
        var temp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = temp;
        swaps++;
      }
    }
  }
  var last = a.length - 1;
  console.log("Array is sorted in " + swaps + " swaps");
  console.log("First Element:" + a[0]);
  console.log("Last Element:" + a[a.length - 1]);
console.log(swaps);
