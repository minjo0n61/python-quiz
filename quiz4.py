# 퀴즈4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댇글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 둥에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle 과 sample을 활용

# 출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --


# 방법1
from random import *

lst = []
value = 1

for i in range(21):
    lst.append(value)
    value += 1

shuffle(lst)
print(lst)
s1 = sample(lst, 1)
print("chicken: "+str(s1[0]))

setlst = set(lst)
set1 = set(s1)

print(setlst.difference(set1))
lst = list(setlst.difference(set1))
shuffle(lst)
print(lst)
s234 = sample(lst, 3)
print("coffee: "+str(s234[0])+"," + str(s234[1])+"," + str(s234[2]))


# 방법 2
# lst = range(1, 21)
# lst = list(lst)
# print(lst)
# shuffle(lst)
# print(lst)
# winner = sample(lst, 4)
# print(winner)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winner[0]))
# print("커피 당첨자 : {0}".format(winner[1:]))
# print("-- 축하합니다 --")
