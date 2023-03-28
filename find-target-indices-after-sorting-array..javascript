/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    var sort=nums.sort((a,b)=> a-b);
    var  result=new Array();
    for(var i=0;i<nums.length;i++){
     if(nums[i]==target)
       result.push(i)
       
    }
  return result
};