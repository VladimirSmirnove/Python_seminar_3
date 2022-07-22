#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


from audioop import reverse


n = int(input('Введите число: '))
list_fib = []

f1 = 1
f2 = -1
for i in range(n+1):
    f1,f2 = f2, f1+f2
    list_fib.append(f2)
list_fib.reverse()
f1 = 1
f2 = 0
for i in range(n):
    f1,f2 = f2, f1+f2
    list_fib.append(f2)
print(list_fib)


