# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


s = int(input('Введите количество сделанных журавликов '))

if s % 6 > 0:
    print("Количество журавлииков не соответсвует условаиям задачи")
else:
    x = s / 3 / 2 # Количество жравликов, сделанные Петей и Сережей 
    y = (x * 2) * 2 # Количество жравликов, сделанные Катей
    print(int(x), int(y), int(x))