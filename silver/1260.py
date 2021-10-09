# DFS와 BFS [ 티어 : 실버 2 ]
# https://www.acmicpc.net/problem/1260

'''
이 문제를 풀기 위해서는 비선형 자료구조 [트리, 그래프]를 사용할줄 알아야한다.
  - DFS(깊이 우선 탐색)
  - BFS(넓이 우선 탐색)
'''
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False] * (n + 1)

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  visited = [False] * (n + 1)
  queue = deque([v])
  visited[v]  = True
  while queue:
    pop = queue.popleft()
    print(pop, end=' ')
    for i in graph[pop]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(graph, v, visited)
print()
bfs(graph, v, visited)