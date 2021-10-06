# 수 정렬하기 [ 티어 : 브론즈 1 ]
# https://www.acmicpc.net/problem/2750

N = int(input())
values = []
for i in range(N):
  values.append(int(input()))
values.sort()
for i in values:
  print(i)