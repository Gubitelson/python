# 4.1[22]: Даны два неупорядоченных набора
# целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих
# наборах. Если таких чисел нет - выдать внятное
# диагностическое сообщение
# Наборы (списки) чисел можно считать заданными
# и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек,
# в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет


new_set_1 = {2, 4, 6, 8, 10, 10, 8, 6, 4, 2}
new_set_2 = {3, 9, 12, 15, 18, 2, 8}

new_set_3 = new_set_1.intersection(new_set_2)

print(*new_set_3 if len(new_set_3) != 0 else ["Повторяющихся чисел нет"])

# if len(new_set_3) != 0:
#     print(*new_set_3)
# else:
#     print("Повторяющихся чисел нет")

# * - Это распаковка
# a,b = new_set_2.intersection(new_set_1)
# print(type(a))