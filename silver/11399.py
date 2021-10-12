# ATM [ 티어 : 실버3 ]
# https://www.acmicpc.net/problem/11399

'''
입력받은 시간을 오름차순으로 정렬해준 뒤
합을 계산해주면 최솟값이 된다.
'''

N = int(input())
s = list(map(int, input().split()))
num = 0
s.sort()
for i in range(N):
  for j in range(i + 1):
    num += s[j]

print(num)
