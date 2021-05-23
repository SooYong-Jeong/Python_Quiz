import re

member = dict()

def namecheck():
    name_p = re.compile('^[ㄱ-ㅣ가-힣]+$')
    name_c = 0
    while not name_c:
        name = input('이름 >>> ')
        name_c = name_p.match(name)
        print(name_c)
    return name

def idcheck():
    id_p = re.compile('^[a-z][a-z0-9]{4,11}$')
    id_c = 0
    while not id_c:
        id = input('아이디(영어, 숫자) >>> ')
        id_c = id_p.match(id)
        print(id_c)
    return id

def telcheck():
    tel_p = re.compile('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}$')
    tel_c = 0
    while not tel_c:
        tel = input('전화번호 >>> ')
        tel_c = tel_p.match(tel)
        print(tel_c)
    return tel

def jumincheck():
    jumin_p = re.compile('^[0-9]{6}-[1-8][0-9]{6}$')
    jumin_c = 0
    while not jumin_c:
        jumin = input('주민번호 >>> ')
        jumin_c = jumin_p.match(jumin)
        print(jumin_c)
    return jumin

def emailcheck():
    email_p = re.compile('(http|https)://[a-z]+.[a-z]+.[a-z]+$')
    email_c = 0
    while not email_c:
        email = input('이메일을 입력하세요 >>> ')
        email_c = email_p.match(email)
        print(email_c)
    return email

def signup(member):
    name = namecheck()
    id = idcheck()
    tel = telcheck()
    jumin = jumincheck()
    email = emailcheck()
    member[id] = [name, tel, jumin, email]
    return member

member = signup(member)
print(member)
