# 별 찍기 - 9 [ 티어 : 브론즈 : 3 ]
# https://www.acmicpc.net/problem/2446

from sys import stdin

N = int(stdin.readline())
for i in range(N):
  print(" " * i + "*" * ((N - i) * 2 - 1))
for i in range(N - 2, -1, -1):
  print(" " * i + "*" * ((N - i) * 2 - 1))