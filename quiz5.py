# 퀴즈5) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# 출력문 예제)
# [O] 1번째 손님(소요시간: 15분)
# [] 2번째 손님(소요시간: 50분)
# [O] 3번째 손님(소요시간: 5분)
# ...
# [] 50번째 손님(소요시간: 16분)

# 총 탑승 승객: 2 분

from random import *

time = range(5, 51)
time = list(time)
shuffle(time)

ok = ["O", " "]
ok_num = 0
for i in range(50):
    i += 1
    ranT = sample(time, 1)
    if ranT[0] >= 5 and ranT[0] <= 15:
        ok = "O"
    else:
        ok = " "
    print("[{0}] {1}번째 손님(소요시간: {2}분)".format(str(ok), str(i), str(ranT[0])))
    if ok == "O":
        ok_num += 1
    else:
        ok_num = ok_num

print("총 탑승 승객 : "+str(ok_num)+"분")
