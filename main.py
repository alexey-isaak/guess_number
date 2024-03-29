
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print("Введите произведение загаданных чисел:")
p = int(input())
print("Введите сумму загаданных чисел:")
s = int(input())

ar_x = list()
ar_y = list()

if p == 0:
    print("Первое загаданное число:", 0)
    print("Второе загаданное число:", s)

else:
    D = (s * s) - (4 * p) # Вычисление дискриминанта.

    if D == 0:
        y = s / 2
        x = p / y
        print("Первое загаданное число:", x)
        print("Второе загаданное число:", y)
    else:
        y1 = int((s + D ** 0.5) / 2)
        y2 = int((s - D ** 0.5) / 2)

        ar_y.append(y1)
        ar_y.append(y2)
        x1 = int(p / y1)
        x2 = int(p / y2)
        ar_x.append(x1)
        ar_x.append(x2)

    print("Первое загаданное число:", ar_x[1])
    print("Второе загаданное число:", ar_y[1])
