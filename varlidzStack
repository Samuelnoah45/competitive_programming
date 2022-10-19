/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function (pushed, popped) {
  var stack = [];
  var pop = 0;
  var push = 1;

  stack.push(pushed[0]);
  for (let i = 0; i < pushed.length * 2; i++) {
    if (stack[stack.length - 1] == popped[pop]) {
      stack.pop();
      pop++;
    } else {
      if (pushed[push]) {
        stack.push(pushed[push]);
        push++;
      }
    }
  }
  console.log(stack);
  return stack.length == 0 ? true : false;
};

var pushed = [1, 2, 3, 4, 5];
var popped = [4, 3, 5, 1, 2];

console.log(validateStackSequences(pushed, popped));
