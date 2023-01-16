class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dict_ = Counter(changed)
        res = []
        changed.sort()
        if len(changed) % 2 != 0: return []
        for el in changed:
            if el == 0:
                continue
            elif 2 * el in dict_ and dict_[el] > 0 and dict_[2 * el] > 0:
                res.append(el)
                dict_[2 * el], dict_[el] = dict_[2 * el] - 1, dict_[el] - 1
                
        if dict_[0] % 2 != 0:
            return []
        elif dict_[0] % 2 == 0:
            for i in range(dict_[0] // 2):
                res.append(0)
        return res if 2 * len(res) == len(changed) else []