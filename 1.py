Num = input("Введите натуральное число: ")
if Num.isdigit() and int(Num)>0:
    sum = 0
    for el in Num:
        el = int(el)
        if el % 2 != 0:
            sum = sum + el
    print(sum)
else:
    print("ошибка")
