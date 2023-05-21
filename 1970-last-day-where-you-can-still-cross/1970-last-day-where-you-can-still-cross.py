class Solution:
  def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
			heads = list(range(row * col + 2))
			lands = {0, row * col + 1}
						
			def index(r, c):
				if r == 0:
					return 0
				if r == row + 1:
					return row * col + 1
				return (r - 1) * col + c
						
			def find(node):
				while node != heads[node]:
					heads[node] = heads[heads[node]]
					node = heads[node]
				return node
						
			def union(i, j):
				i, j = find(i), find(j)
				if i > j:
					i, j = j, i
				heads[j] = i     
				
			for i, [r, c] in enumerate(cells[::-1], 1):
				curr = index(r, c)
				lands.add(curr)
				for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
					nei = index(x, y)
					if 0 <= x <= row + 1 and 0 < y <= col and nei in lands:
						union(curr, nei)
					if find(0) == find(row * col + 1):
						return row * col - i
			return -1