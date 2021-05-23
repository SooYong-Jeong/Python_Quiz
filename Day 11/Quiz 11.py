import os
dir = os.path.dirname(__file__)

def input_data():
    Book_name = input('책 이름 : ')
    Writer = input('저자 : ')
    Publisher = input('출판사 : ')
    f = open(dir + '/Books.txt', 'a', encoding = 'utf-8')
    f.write(Book_name + ',' + Writer + ',' + Publisher + '\n')
    f.close()

def Print_data():
    f = open(dir + '/Books.txt', 'r', encoding = 'utf-8')
    for i in f.readlines():
        i = i.replace('\n','')
        data = i.split(',')
        print(f'도서명 : {data[0]}, 저자 : {data[1]}, 주소 : {data[2]}')
    f.close

