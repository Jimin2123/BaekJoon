# 최대공약수 [ 티어 : 실버 2 ]
# https://www.acmicpc.net/problem/1850

'''
유클리드 호제법을 알아야 풀 수 있는 문제.
'''
from sys import stdin

# 재귀함수 이용
def gcd(a,b):
  if b == 0:
    return a 
  else:
    return gcd(b, a % b)
a,b = map(int, stdin.readline().split())

print("1"* gcd(a,b)) # 곱으로 표현

'''
from sys import stdin
import math
a, b = map(int, stdin.readline().split())
gcd = math.gcd(a, b)
print('1'*gcd)
'''