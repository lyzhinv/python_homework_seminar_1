# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = input('Введите номер билета: ')

if 6 == len(str(number)):
    left_number = int(number[0]) + int(number[1]) + int(number[2])
    right_number = int(number[3]) + int(number[4]) + int(number[5])
    if left_number == right_number:
        print(f'Билет {number} - счастливый')
    else:
        print(f'Билет {number} - НЕ счастливый')
else:
    print('Ошибка! Номер билета должен быть шестизначным')