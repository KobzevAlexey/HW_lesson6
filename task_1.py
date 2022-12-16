# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

import math

num = int(input('Введите число: '))
print(list(map(lambda x: x * math.factorial(x - 1), range(1, num + 1))))
