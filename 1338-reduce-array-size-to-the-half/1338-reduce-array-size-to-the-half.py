class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dicts = collections.defaultdict(int)
        for num in arr:
            dicts[num]+=1
        sets = 0
        ans = 0
        dictsArr = sorted(dicts.items(),key=lambda item: item[1])
        # print(dicts)
        # print(dictsArr)
        for obj in reversed(dictsArr):
            sets +=obj[1]

            print(obj[1])
            ans +=1
            if sets >= len(arr)/2:
                return ans
            

        return 0


        