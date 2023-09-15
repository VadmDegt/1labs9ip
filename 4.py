my_dict = dict(имя='Артем', фамилия="Жушма", образование="Высшее")
print(sorted(my_dict, key=my_dict.get))
print(sorted(my_dict, key=my_dict.get,reverse=True))
