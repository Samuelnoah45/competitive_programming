/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function (s) {
  var stack = [];
  for (var i = 0; i < s.length; i++) {
    if (s[i] != ")") {
      stack.push(s[i]);
    } else if (s[i] == ")") {
      var sub = [];
      var popValue;
      do {
        popValue = stack.pop();
        sub.push(popValue);
      } while (popValue != "(");
      sub.pop();
      stack = stack.concat(sub);
    }
  }
  return stack.join("");
};