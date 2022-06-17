quantity_elem = input("Введите количество элементов списка: ")
quantity_elem = int(quantity_elem)
element1 = []
for i in range(1,quantity_elem+1):
    element = (input(f'Введите {i}-й элемент: '))
    element = int(element)
    element1.append(element)

print(f'До сортировки: {element1}')
element1.sort()
print(f'После сортировки: {element1}')






