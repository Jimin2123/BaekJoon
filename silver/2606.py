# 바이러스 [ 티어 : 실버 2 ]
# https://www.acmicpc.net/problem/2606

'''
DFS , BFS 방식을 알고 있어야 풀 수 있는 문제.
'''

from sys import stdin

# DFS를 사용하여 푸는 방식
readline = stdin.readline
dic = {}
for i in range(int(readline())):
  dic[i+1] = set()
  for j in range(int(readline())):
    a,b = map(int, readline().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
  for i in dic[start]:
    if i not in visited:
      visited.append(i)
      dfs(i, dic)

visited = []
dfs(1,dic)
print(len(visited) - 1)


# BFS를 사용하여 푸는 방식
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
visited = []
bfs(1, dic)
print(len(visited)-1)