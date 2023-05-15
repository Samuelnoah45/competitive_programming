from collections import defaultdict
from collections import deque

def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = defaultdict(list)
    courses = set()
    degree = defaultdict(int)
    for pre, course in prerequisites:
        graph[pre].append(course)
        courses.add(course)        
        courses.add(pre)
        degree[course] += 1
    queue = deque()
    for course in range(1, n + 1):
        if degree[course] == 0:
            queue.append(course)
    courses_taken, semisters = bfs(graph, queue, n, degree)
    if len(courses_taken) == n:
        return semisters
    return -1

def bfs(graph, queue, n, degree):
    level = 0
    courses = []
    while queue:
        length = len(queue)
        for _ in range(len(queue)):
            curr = queue.popleft()
            courses.append(curr)
            for adj in graph[curr]:
                degree[adj] -= 1
                if degree[adj] == 0:
                    queue.append(adj)
        level += 1
    
    return courses, level