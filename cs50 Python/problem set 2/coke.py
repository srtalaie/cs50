cost = 50

while True:
    coin = int(input("Insert coin: "))
    while cost > 0:
        if cost < coin:
            change = coin - cost
            cost = cost - coin
            print("Change Owed:", change)
            break
        elif (coin == 25 or coin == 10 or coin == 5) and ((cost - coin) == 0):
            cost = cost - coin
            print("Change Owed:", cost)
            break
        elif coin == 5 and cost >= coin:
            cost = cost - coin
            print("Amount Due:", cost)
            break
        elif coin == 10 and cost >= coin:
            cost = cost - coin
            print("Amount Due:", cost)
            break
        elif coin == 25 and cost >= coin:
            cost = cost - coin
            print("Amount Due:", cost)
            break
        elif coin != 5 or coin != 10 or coin != 25:
            print("Amount Due:", cost)
            break

    if cost <= 0:
        break
