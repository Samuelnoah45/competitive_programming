/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
  var prefix = [0];
  var ans = -1;
  for (var i = 0; i < nums.length; i++) {
    prefix.push(prefix[prefix.length - 1] + nums[i]);
  }
  for (var i = 0; i < nums.length; i++) {
    if (prefix[i] == prefix[prefix.length - 1] - prefix[i + 1]) {
      ans = i;
      break;
    }
  }
  console.log(prefix);
  return ans;
};