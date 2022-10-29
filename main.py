print('Введите три числа: ')  # part 1

a = int(input())
b = int(input())
c = int(input())

print('---------------')

number_name = ["a", "b", "c"]

a_division_by_3 = a % 3
b_division_by_3 = b % 3

if a > 10 and b > 10 and c > 10 and a_division_by_3 == 0 and b_division_by_3 == 0:
    print('yes')
else:
    print('no')

print('---------------')

hometask_2 = [a, b, c]  # part 2. Используем числа a, b, с, которые вводим в 1-й части задания

i = 1
max = hometask_2[0]
k = 0
while i < len(hometask_2):
    for x in hometask_2:
        if hometask_2[i] > hometask_2[i - 1]:
            max = hometask_2[i]
            k = i
    i += 1
print(f'Максимальное число {number_name[k]}, которое равно', max)

print('---------------')

c2 = int(b - a)  # part 3. Сумма чисел a и b, которые вводим в 1-й части задания

if a > b:
    c2 = -c2
i = 0
for x in range(c2 + 1):
    x = a + x
    if x % 2 == 0:
        i += x
    else:
        i += 0
print('Cумма всех четных чисел в диапазоне от a до b равна', i)
