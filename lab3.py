import numpy as np

def hesabla_hendesi_orta(matris):
    diaqonal_elementlər = [matris[i][i] for i in range(len(matris))]
    
    hasil = 1
    for element in diaqonal_elementlər:
        hasil *= element
    
    hendesi_orta = hasil ** (1 / len(diaqonal_elementlər))
    return hendesi_orta

# Nümunə matris (n x n)
A = [
    [2, 5, 3],
    [4, 3, 6],
    [7, 8, 1]
]

nəticə = hesabla_hendesi_orta(A)
print(f"Baş diaqonalın həndəsi ortası: {nəticə:.4f}")
