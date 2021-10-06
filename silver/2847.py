# 게임을 만든 동준이 [ 티어 : 실버 4 ]
# https://www.acmicpc.net/problem/2847

from sys import stdin

N = int(stdin.readline())
level = [int(stdin.readline()) for _ in range(N)]
result = 0

for i in range(N-1, 0, -1):
  if level[i] <= level[i-1]:
    result += (level[i-1]-level[i]+1)
    level[i-1] = level[i]-1

print(result)


