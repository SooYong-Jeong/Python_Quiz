from datetime import datetime

resi_num = input("주민등록번호를 입력하여 주세요 ex) 111111-1111111 : ")

if resi_num[8] == 1 or 2:
    age = datetime.today().year - (1900 + int(resi_num[0:2]))
elif resi_num[8] == 3 or 4:
    age = datetime.today().year - (2000 + int(resi_num[0:2]))

if (datetime.today().month - int(resi_num[2:4])) <= 0 and (datetime.today().day - int(resi_num[4:6])) < 0:
    age -= 1

print(f"만 {age}세")