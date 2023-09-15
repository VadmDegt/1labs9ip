# Изначальное меню кондитерской
menu = {
    'торт': ['Шоколадный торт', 200, 300],
    'пирожное': ['Ванильное пирожное', 50, 150],
    'маффин': ['Голубика маффин', 70, 100],
    'печенье': ['Ореховое печенье', 30, 200],
    'капкейк': ['Клубничный капкейк', 80, 120],
    'эклер': ['Классический эклер', 60, 180]
}

# Изначальное состояние корзины покупателя
cart = {}

while True:
    print("\nМеню кондитерской:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("n. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        for product, info in menu.items():
            print(f"{product} - {info[0]}")
    elif choice == '2':
        for product, info in menu.items():
            print(f"{product} - {info[1]} рублей за 100гр")
    elif choice == '3':
        for product, info in menu.items():
            print(f"{product} - {info[2]} грамм")
    elif choice == '4':
        for product, info in menu.items():
            print(f"{product}: {info[0]}, Цена: {info[1]} рублей за 100гр, Количество: {info[2]} грамм")
    elif choice == '5':
        product_name = input("Введите название продукции (или 'n' для выхода из покупки): ")
        if product_name == 'n':
            break
        if product_name in menu:
            available_quantity = menu[product_name][2]
            if available_quantity > 0:
                product_quantity = int(input(f"Введите количество ({available_quantity} грамм доступно): "))
                if product_quantity > 0 and product_quantity <= available_quantity:
                    if product_name in cart:
                        cart[product_name] += product_quantity
                    else:
                        cart[product_name] = product_quantity
                    menu[product_name][2] -= product_quantity
                    print(f"Вы добавили {product_quantity} грамм(а) {menu[product_name][0]} в корзину.")
                else:
                    print(
                        f"Некорректное количество. Доступно всего {available_quantity} грамм(а) {menu[product_name][0]}.")
            else:
                print(f"{menu[product_name][0]} закончился.")
        else:
            print("Такой продукции нет в меню.")
    elif choice == 'n':
        break
    else:
        print("Пожалуйста, выберите корректный пункт меню.")
