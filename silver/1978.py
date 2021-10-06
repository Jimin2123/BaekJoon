# 소수 찾기 [ 티어 : 실버 4 ]
# https://www.acmicpc.net/problem/1978

N = int(input())
count = 0
numbers = list(map(int, input().split()))

for num in numbers:
  error = False
  if num > 1:
    for i in range(2, num):
      if num % i == 0:
        error = True
    if error == False:
      count += 1
print(count)