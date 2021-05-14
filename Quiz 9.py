def sum(a,b):
    return a+b

def diff(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    return a/b

oper = ['+', '-', 'x', '/']
while True:
    choice = int(input('0.종료 1.+ 2.- 3.x  4./ : '))
    if choice == 0:
        print('종료')
        break
    a = int(input('피연산수 : '))
    b = int(input('연산수 : '))
    

    if choice == 1:
        result = sum(a,b)

    elif choice == 2:
        result = diff(a,b)

    elif choice == 3:
        result = multi(a,b)
        
    elif choice == 4:
        result = divi(a,b)


    print('{} {} {} = {:.2f}'.format(a, oper[choice -1], b, result))
        