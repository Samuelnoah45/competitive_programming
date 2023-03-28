/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
      var l=0;
      var r=1;
      var result=0
    for(var i=0;i<nums.length;i++){
        if(nums[l]!=nums[r]){
            nums[l+1]=nums[r]
            l++;
            r++;
            result++;
        }
      else if(nums[l]==nums[r]){
            r++;
            console.log(l,r)

        }

    }
    return result
};