/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
        let l = 0;
        while (l < nums.length) {
            if (nums[l] >= target) {
                break;
            }
            l++;
        }

         return l;
    
    
};