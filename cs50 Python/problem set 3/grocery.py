list = {}

while True:
    try:
        item = input()
        item = item.strip().upper()

        if item not in list:
            list[item] = 1
        elif item in list:
            list[item] += 1
    except KeyError:
        pass
    except EOFError:
        sorted_list = sorted(list.items())
        for i in range(len(sorted_list)):
            print(f"{sorted_list[i][1]} {sorted_list[i][0]}")
        break
