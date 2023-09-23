import math

def a(d, h):
    radius = d / 2
    volume = (1/3) * math.pi * radius**2 * h
    return volume

d1 = float(input("Діаметр основи першого конуса: "))
h1 = float(input("Висота першого конуса: "))

d2 = float(input("Діаметр основи другого конуса: "))
h2 = float(input("Висота другого конуса: "))

v = a(d1, h1)
v2 = a(d2, h2)

if v > v2:
    print("Об'єм першого конуса більший за об'єм другого конуса.")
elif v < v2:
    print("Об'єм другого конуса більший за об'єм першого конуса.")
else:
    print("Об'єми обох конусів рівні.")
