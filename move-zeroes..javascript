/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

 var moveZeroes = function(nums) {
    var l=0;
    var r=1
  var length =nums.length
  console.log(length);
    for(var i=0;i<length;i++){
      
         if(nums[r]!=undefined){
        
       if(nums[l]==0&&nums[r]!=0){
           var temp=nums[l];
            nums[l]=nums[r];
            nums[r]=temp
            l++ 
            r++
            console.log("swap");
       }
       else if(nums[l]==0&&nums[r]==0){
        r++;
  
       }
       else if(nums[l]!=0&&nums[r]!=0||nums[l]!=0&&nums[r]==0){
           r++;
           l++
       }
         }
  
    }
  
    console.log(nums)
            
  };