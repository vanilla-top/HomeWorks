def coy(X, Y, P):
    years = 0
    while X < Y:
        X = int(X * (1 + P / 100))
        years += 1
    return years

X = float(input("Введите начальный вклад (в рублях): "))
Y = float(input("Введите целевую сумму (в рублях): "))
P = float(input("Введите ежегодный процент увеличения (%): "))

years = coy(X, Y, P)
print(f"'это займет {years} лет.чтобы депозит достиг {Y} рублей.")