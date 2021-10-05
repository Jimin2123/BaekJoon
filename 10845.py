# 큐 (티어 : 실버 4)
# https://www.acmicpc.net/problem/10845

import sys

class Queue:
  def __init__(self):
    self.que = []

  def push(self, value):
    self.que.insert(0, value)
    # self.que.append(value)

  def pop(self):
    if len(self.que) == 0: return -1
    else: return self.que.pop()

  def size(self):
    return len(self.que)

  def empty(self):
    if len(self.que) == 0: return 1
    else: return 0

  def front(self):
    if len(self.que) == 0: return -1
    else: return self.que[-1]
    # else: return self.que[0]

  def back(self):
    if len(self.que) == 0: return -1
    else: return self.que[0]
    # else: return self.que[-1]

que = Queue()
que.push(1)
que.push(2)
que.push(3)
que.push(4)
print(que.que)
print(que.front())
print(que.back())

# N = int(sys.stdin.readline()) 

# for _ in range(N):
#   word = sys.stdin.readline().split()
#   order = word[0]

#   if order == "push": que.push(word[1])
#   elif order == "pop": print(que.pop())
#   elif order == "size": print(que.size())
#   elif order == "empty": print(que.empty())
#   elif order == "top": print(que.top())
#   elif order == "front": print(que.front())
#   elif order == "back": print(que.back())