arrBerat = []
bMin = 0
bMax = 0


def hitungMinMax(arrBerat):
    global bMin, bMax
    bMin = arrBerat[0]
    bMax = arrBerat[0]
    for i in range(len(arrBerat)):
        if bMin > arrBerat[i]:
            bMin = arrBerat[i]
        if bMax < arrBerat[i]:
            bMax = arrBerat[i]


def rerata(arrBerat):
    total = 0

    for i in range(len(arrBerat)):
        total = total + arrBerat[i]
    return total / (i + 1)


print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    beratBalita = float(input())

    arrBerat.append(beratBalita)


hitungMinMax(arrBerat)
print("Berat balita minimum: {0:.2f}".format(bMin))
print("Berat balita maksimum: {0:.2f}".format(bMax))
print("Rerata berat balita: {0:.2f}".format(rerata(arrBerat)))
