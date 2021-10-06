# 수 정렬하기 2 [ 티어 : 실버 5 ]
# https://www.acmicpc.net/problem/2751

from sys import stdin

def result1():
  numbers.sort()
  for num in numbers:
    print(num)

def result2():
  for num in sorted(numbers):
    print(num)


N = int(stdin.readline())
numbers = []
for i in range(N):
  numbers.append(int(stdin.readline()))
result2()