for i in range(1, 10):
        for j in range(2, 10):  # 단 수가 안에 들어왔다.
            print(f"{j} x {i} = ", end = ' ')
            if i * j < 10: print("",end = ' ')
            print(f"{i * j}", end = '\t')
        print()