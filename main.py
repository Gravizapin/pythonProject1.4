

number =  int(input('Введите число :'))

er_num = 0
num = number

while num > 0:
    digit = num % 10
    if digit > er_num:
        er_num = digit
        er_num == 9
        break
    num = num // 10
print(f'Наибольшая цифра в числе {number} равна {er_num}')