# Ədədi massiv yaradılır və fayla yazılır
massiv = [12, 15, 7, 20, 9, 5, 3, 25, 13, 11]

with open("ededi_massiv.txt", "w") as f:
    for eded in massiv:
        f.write(f"{eded}\n")

# Fayl oxunur və 5-ə bölünməyən ədədlər seçilir
bolunmeyenler = []
with open("ededi_massiv.txt", "r") as f:
    for sətr in f:
        eded = int(sətr.strip())
        if eded % 5 != 0:
            bolunmeyenler.append(eded)

# Yeni fayla yazılır
with open("bolunmeyenler.txt", "w") as f:
    for eded in bolunmeyenler:
        f.write(f"{eded}\n")

# Hasil hesablanır
hasil = 1
for eded in bolunmeyenler:
    hasil *= eded

print("5-ə bölünməyən ədədlər:", bolunmeyenler)
print("Onların hasili:", hasil)
