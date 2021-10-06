# 나이순 정렬 [ 티어 : 실버 5 ]
# https://www.acmicpc.net/problem/10814

from sys import stdin

N = int(stdin.readline())
member_list = []

for _ in range(N):
  age, name = map(str, stdin.readline().split())
  member_list.append((int(age), name))

member_list.sort(key = lambda member: (member[0]))
for member in member_list:
  print(member[0], member[1])