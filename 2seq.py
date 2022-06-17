import re
numbers = input("Введите любые цифры через разделители (,) (;) (/): ")
numbers1 = re.split(",|;|/", numbers)
print("Список исходный: ", (numbers1))
result_numbers = []
for item in numbers1:
    if numbers1.count(item) == 1:
        result_numbers.append(item)

print("Список не повторяющихся (уникальных) данных: ", result_numbers)