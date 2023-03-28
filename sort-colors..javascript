/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
  var red=[]
  var blue=[]
  var white=[]
  for(var i=0;i<nums.length;i++){
   if(nums[i]==0)
     red.push(nums[i])
     else if (nums[i]==1)
     white.push(nums[i])
     else
     blue.push(nums[i])
  }
   for(var i=0;i<red.length;i++)
    nums[i]=0;
    for(var i=0+red.length;i<white.length+red.length;i++)
    nums[i]=1;
    for(var i=0+white.length+red.length;i<blue.length+white.length+red.length;i++)
    nums[i]=2;

    
};