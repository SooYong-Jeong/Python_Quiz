import random

rcp = ['가위','바위','보']

while True:
    insert = input('가위바위보를 하세요 : ')
    computer = random.choice(rcp)
    if insert == '':
        print('프로그램 종료')
        break
    print('Computer : ',computer)
    if insert == computer:
        print('무승부')

    elif (insert == '가위' and computer == '보') or (insert == '바위' and computer == '가위') or (insert == '보' and computer == '바위'):
        print('승')

    elif (insert == '가위' and computer == '바위') or (insert == '바위' and computer == '보') or (insert == '보' and computer == '가위'):
        print('패')

    else:
        print('가위, 바위, 보 로 입력하세요.')