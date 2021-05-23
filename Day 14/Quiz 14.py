class Account:
    account_count = 0

    @classmethod
    def get_account_num(cls):
        print('계좌수 : ',cls.account_count)

    def __init__(self, name, balance):
        Account.account_count += 1
        self.deposit_count = 0
        self.total_log = []
        self.name = name
        self.balance = balance
        self.account_number = str(Account.account_count)
    
    def deposit(self, amount):
        if amount >= 1:
            self.total_log.append(('입금',amount))
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                interest = int(self.balance * 0.01)
                self.balance += interest
                self.total_log.append(('이자지급',interest))
                print(interest,'원의 이자가 지급되었습니다.')
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.total_log.append(('출금',amount))
            self.balance -= amount
            print(amount,'원이 출금되었습니다.')
        else:
            print('잔액이 부족합니다.')
    
    def display_info(self):
        print('예금주 : ',self.name)
        print('계좌번호 : ',self.account_number)
        print('잔고 : ',self.balance)
    
    def __str__(self):
        return '예금주:'+self.name+',계좌번호:'+self.account_number+',잔고:'+str(self.balance)
        
account_list = []
while True:
    menu = input('1.계좌개설 2.입금 3.출금 4.입출금내역 5.총계좌수출력 6.종료 \n>>')
    if menu == '1':
        name = input('이름 >>> ')
        balance = int(input('입금금액 >>> '))
        a = Account(name, balance)
        account_list.append(a)
        print(a)
        print('계좌가 개설되었습니다.')
    elif menu == '2':
        account_num = input('계좌번호를 입력하세요 >>> ')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                amount = int(input('입금할 금액을 입력하세요 >>> '))
                acc.deposit(amount)
                print(amount,'원이 입금되었습니다.')
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu == '3':
        account_num = input('계좌번호를 입력하세요 >>> ')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                amount = int(input('출금할 금액을 입력하세요 >>> '))
                acc.withdraw(amount)
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu == '4':
        account_num = input('계좌번호를 입력하세요 >>> ')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                for data in acc.total_log:
                    print(data[0],data[1])
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu == '5':
        Account.get_account_num()
    elif menu == '6':
        print('프로그램 종료!')
        break
    else:
        print('메뉴를 잘못선택했습니다.')