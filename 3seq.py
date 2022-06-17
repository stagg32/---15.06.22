numbers1 = input("Введите элементы 1 списка через запятую: ").split(",")
print("Список №1: ", (numbers1))
numbers2 = input("Введите элементы 1 списка через запятую: ").split(",")
print("Список №2: ", (numbers2))

for item in numbers1[:]:
    if item in numbers2:
        numbers1.remove(item)
print("Список №1 (без совпадений): ", numbers1)

