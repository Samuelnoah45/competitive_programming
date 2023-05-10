class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        needs  = defaultdict(int)
        graph  = defaultdict(list)

        for i in range(len(recipes)):
            needs[recipes[i]] = len(ingredients[i])
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])

        que = deque(supplies)
        print(que)
        ans = []
        while que:
            sup = que.popleft()
            
            for recipe in graph[sup]:
                needs[recipe] -= 1
                if needs[recipe] == 0:
                    ans.append(recipe)
                    que.append(recipe)

        return ans