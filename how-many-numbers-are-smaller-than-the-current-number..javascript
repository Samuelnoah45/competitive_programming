/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
     var count =new Array(nums.length).fill(0)
    
    for(var i=0; i<nums.length;i++){
       for(var j=0;j<nums.length;j++){
           if(nums[i]>nums[j])
            count[i]++
       }

    }
   return count
};