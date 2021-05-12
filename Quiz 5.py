coffe = {'아메리카노':2500,'카푸치노':3500,'카페라떼':3000,'레몬에이드':2000}
price = list(coffe.values())
coffe_name = list(coffe.keys())
for i in range(len(price) - 1):
    for j in range(len(price) - 1 - i):
        if price[j] > price[j+1]:
            price[j], price[j+1] = price[j+1] ,price[j]
            coffe_name[j], coffe_name[j+1] = coffe_name[j+1], coffe_name[j]

for i in coffe_name:
    print(f"{i}",end = ' ')

choice = input("\n선택 : ")
print(coffe[choice])