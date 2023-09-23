import math

def c(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

def ab(x):
    if x > 0:
        sqr = math.sqrt(x)
        cub = x ** (1/3)
        rlt = sqr + cub
        print(f"Сума квадратного і кубічного коренів числа {x} = {rlt:.2f}")
    else:
        print("Введіть додатне число для обчислення коренів.")

c(10, 5)

ab(8)
