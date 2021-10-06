# 단어 정렬 [ 티어 : 실버 5]
# https://www.acmicpc.net/problem/1181

N = int(input())
words_list = []

for _ in range(N):
  word = str(input())
  word_cnt = len(word)
  words_list.append((word, word_cnt))

# 중복 삭제
words_list = list(set(words_list))

# 단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))

for word in words_list:
  print(word[0])