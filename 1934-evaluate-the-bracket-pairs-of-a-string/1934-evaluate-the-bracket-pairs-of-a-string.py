class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {key:sol for key, sol in knowledge}
        ans = add = ''

        for char in s:
            if char == '(':
                ans += add
                add = ''
            elif char == ')':
                ans += d[add] if add in d else '?'
                add = ''
            else:
                add += char

        return ans + add

        