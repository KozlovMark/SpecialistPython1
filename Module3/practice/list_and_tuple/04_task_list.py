# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

number_list = (-10, 5, 9, 6, 10, 6, 5, -2)
sum = 0

for number in number_list:
    if number > 0:
        sum = sum + number

print("Sum =", sum)
