def hasili_9_dan_boyuk(B):
    hasil = 1
    say = 0
    for eded in B:
        if eded > 9:
            hasil *= eded
            say += 1
    if say == 0:
        return 0  # Əgər 9-dan böyük heç bir element yoxdursa, 0 qaytarırıq
    return hasil

# Nümunə massiv
B = [3, 12, 7, 15, 2, 10]

netice = hasili_9_dan_boyuk(B)
print("9-dan böyük elementlərin hasili:", netice)
