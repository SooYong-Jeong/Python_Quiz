menues = ['돌체 라떼', '카페 모카', '카페 라떼', '아메리카노']
menues_charge = [6100,5600,5100,4600]
c10k = 0
c5k = 0
c1k = 0
c5h = 0
c1h = 0
c5t = 0
c1t = 0
input_money = 0
input_menu = 0
for i in range(len(menues)):
    print(f"{(i + 1)}. {menues[i]}\t {menues_charge[i]}")

input_menu = int(input("구입하실 물건의 번호를 입력하세요."))
print(f"{menues_charge[(input_menu - 1)]}원 입니다.")
while input_money <= menues_charge[(input_menu - 1)]:
    money_num = int(input("돈주세요\n1. 5만원  2. 1만원  3. 5천원 4. 1천원\n"))
    if money_num == 1:
        input_money += 50000
    elif money_num == 2:
        input_money += 10000
    elif money_num == 3:
        input_money += 5000
    elif money_num == 4:
        input_money += 1000
    print(f"{input_money}원")
change = input_money - menues_charge[(input_menu - 1)]
if change == 0:
    print("거스름돈이 없다")
while change > 10000:
    change -= 10000
    c10k += 1

while change >= 5000:
    change -= 5000
    c5k += 1

while change >= 1000:
    change -= 1000
    c1k += 1

while change >= 500:
    change -= 500
    c5h += 1

while change >= 100:
    change -= 100
    c1h += 1

while change >= 50:
    change -= 50
    c5t += 1

while change >= 10:
    change -= 10
    c1t += 1
print("총 ")
print(f"만원권 {c10k}장, 오천원권 {c5k}장, 천원권 {c1k}장, 오백원{c5h}개, 백원{c1h}개, 오십원{c5t}개, 십원{c1t}개")