import math

def c(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

def ab(x):
    if x > 0:
        square = math.sqrt(x)
        cubic = x ** (1/3)
        result = square + cubic
        print(f"Сума квадратного і кубічного коренів числа {x} = {result:.2f}")
    else:
        print("Введіть додатне число для обчислення коренів.")

c(10, 5)

ab(8)
