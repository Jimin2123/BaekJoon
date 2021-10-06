# 수 정렬하기 3 [ 티어 : 실버 5 ]
# https://www.acmicpc.net/problem/10989

from sys import stdin

N = int(stdin.readline())
numbers = [0] * 10001
for i in range(N):
  value = int(stdin.readline())
  numbers[value] = numbers[value] + 1

for i in range(10001):
  if numbers[i] != 0:
    for j in range(numbers[i]):
      print(i)