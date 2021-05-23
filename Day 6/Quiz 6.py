from random import *
sub = 0
ans = randrange(1, 101)
count = 0
while True:
    count += 1
    sub = input("1~100사이 숫자를 입력하세요\n")
    print(sub)
    if int(sub) < ans:   
        print(f"{count}번째 시도 : 더 큰수를 입력하세요")
    elif int(sub) > ans:   
        print(f"{count}번째 시도 : 더 작은수를 입력하세요")
    elif int(sub) == ans:
        break
print(f"{count}번째 시도 정답")