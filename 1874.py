# 스택 수열 (티어 : 실버 3)
# https://www.acmicpc.net/problem/1874

from sys import stdin

N = int(stdin.readline())
cnt = 0
stack = []
result = []
status = True

def push(value):
  stack.append(value)
  result.append("+")

def pop():
  stack.pop()
  result.append("-")

for i in range(N):
    num = int(stdin.readline())

    while cnt < num:
      cnt += 1
      push(cnt)

    if stack[-1] == num: pop()
    else: status = False

if status == False:
    print("NO")
else:
  for i in result:
    print(i)