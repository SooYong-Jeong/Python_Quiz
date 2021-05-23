import os,pickle
dir = os.path.dirname(__file__)

def Load_data():
    f = open(dir + '/Data_list.pickle', 'rb')
    Data_list = pickle.load(f)
    f.close
    return Data_list

def Save_data(Data_list):
    f = open(dir + '/Data_list.pickle', 'wb')
    pickle.dump(Data_list,f)
    f.close()

def Input_data(Data_list):
    Book_name = input('책 이름 : ')
    Writer = input('저자 : ')
    Publisher = input('출판사 : ')
    data = [Book_name, Writer, Publisher]
    Data_list.append(data)
    return Data_list

def print_data(Data_list):
    for data in Data_list:
        print(f'도서명 : {data[0]}, 저자 : {data[1]}, 주소 : {data[2]}')

Data_list = []
Data_list = Load_data()
while True:
    menu = input('1.입력  2.출력  3.종료 \n >>> ')
    if menu == '1':
        Data_list = Input_data(Data_list)
        Save_data(Data_list)
    elif menu == '2':
        print_data(Data_list)
    elif menu == '3':
        print('프로그램 종료')
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')