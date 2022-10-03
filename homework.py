# Задача 1 Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
a = float(input())
c = 0
sum = 0
while a!=int(a):
    a *= 10
b = a
while b != 0:
    sum += b%10
    b = b//10
print(int(sum))



# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input())
operation = 1
for i in range(1, n+1):
    operation *= i
    print(operation, end=" ")

# Задача 3. Реализуйте алгоритм перемешивания списка. 
# Список размерностью 10 задается случайными целыми числами, выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!
import random
spisok = list(map(int, input().split()))
num = 0
while num != 10:
    randomONE = random.randint(0, 9)
    randomTWO = random.randint(0, 9)
    if randomONE != randomTWO:
        spisok[randomONE], spisok[randomTWO] = spisok[randomTWO], spisok[randomONE]
        num += 1
print(spisok)