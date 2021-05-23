import random,time

count = 0
oper = ['+', '-', '*', '/']
start = time.time()
for i in range(5):
    a = random.randint(1,50)
    b = random.randint(1,50)
    op = random.choice(oper)
    quiz = str(a) + op + str(b)
    print(quiz,'=')
    result = int(input('정답 = '))
    if int(eval(quiz)) == result:
        print('정답')
        count += 1
    else:
        print('오답')
end = time.time()
print('{}개 맞음 {:.2f}초 경과'.format(count,end - start))