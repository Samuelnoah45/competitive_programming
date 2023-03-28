/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    var l=0;
    var  r=numbers.length-1
    var arr=new Array();
    while(l<r){ 
         var sum= numbers[l]+numbers[r];
         console.log(numbers[l],numbers[r])
        if(sum==target){
          arr.push(l+1)
          arr.push(r+1)
          return arr
        }
        else if(sum>target){
            r--
        }
         else if(sum<target){
            l++
        } }
    
};