# 스택 (티어 : 실버 4)
# https://www.acmicpc.net/problem/10828

import sys

class Stack:
  def __init__(self):
    self.stack = []
  def push(self, value):
    self.stack.append(value)
  def pop(self):
    if len(self.stack) == 0:
      return -1
    else :
      return self.stack.pop()
  def size(self):
    return len(self.stack)
  def empty(self):
    if len(self.stack) == 0:
      return 1
    else :
      return 0
  def top(self):
    if len(self.stack) == 0:
      return -1
    else :
      return self.stack[-1]

N = int(sys.stdin.readline()) 

stack = Stack()

for _ in range(N):
  word = sys.stdin.readline().split()
  order = word[0]

  if order == "push":
    value = word[1]
    stack.push(value)
  elif order == "pop":
    result = stack.pop()
    print(result)
  elif order == "size":
    result = stack.size()
    print(result)
  elif order == "empty":
    result = stack.empty()
    print(result)
  elif order == "top":
    result = stack.top()
    print(result)