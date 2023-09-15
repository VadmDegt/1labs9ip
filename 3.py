my_list = [1612, 49, 'hello', 6, 19, 'world']
vowels = 'aeiouy'
sumV = 0
sumС = 0
sumarr = []
indexlist = 0
for el in my_list:
    sum = 0
    if isinstance(el, int):
        if el % 2 == 0:
            el = str(el)
            for i in el:
                sum += int(i)
            sumarr.append(sum)
        elif el % 2 != 0:
            indexlist = my_list.index(el)
            my_list.remove(el)
            el = 1
            my_list.insert(indexlist,el)



    else:
        for i in el:
            for l in vowels:

                if i == l:
                    sumV += 1
                    break
                elif i != l and l == 'y':
                    sumС += 1

print(f"Количество гласных: {sumV} Количество согласных: {sumС}")
print(my_list, "список сумм цифр четных чисел: ", sumarr)
