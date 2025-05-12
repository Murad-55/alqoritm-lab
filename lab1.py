import math

# Verilmişlər
x = 0.8
epsilon = 0.001

# Cəmi hesablamaq
term = x  # İlk termin (n=1 üçün)
n = 1
total = 0

while term >= epsilon:
    total += term
    n += 1
    term = x ** n / math.factorial(n)

# Mənfi işarəni əlavə edirik, çünki ifadə mənfidir
P = -total

print(f"Son nəticə (ε ≤ {epsilon} dəqiqliklə): {P:.5f}")
