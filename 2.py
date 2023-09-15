str = input("Введите строку: ")
ch = 0
Ch = 0
CH = 0
CH1 = 0
if int(str.isdigit()):
    print("Неверно введена строка")
    exit()
else:
    for el in str:

        if el.istitle():
            ch += 1
            CH = 0
            if (ch == 2):
                Ch += 1
                ch = 0
        else:
            ch = 0
            CH += 1
            if (CH == 2):
                CH1 += 1
                CH = 0
print(f"Нижний: {CH1},верхний: {Ch}")
