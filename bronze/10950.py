# A + B -3 [ 티어 : 브론즈 3 ]
# https://www.acmicpc.net/problem/10950

T = int(input())

value = []

for i in range(T):
  a,b = map(int, input().split())
  result = a + b
  value.append(result)

for i in value:
  print(i)