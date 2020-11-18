print("Klub A: ",end="")
klubA = input()
print("Klub B: ",end="")
klubB = input()

print("Pertandingan 1 : ",end="")
hasil = input().split()
i = 1
array = []
while int(hasil[0]) != -1 and int(hasil[1]) != -1:
    if int(hasil[0]) > int(hasil[1]):
        array.append(klubA)
    elif int(hasil[1]) > int(hasil[0]):
        array.append(klubB)
    elif int(hasil[0]) == int(hasil[1]):
        array.append("Draw")
    i = i + 1
    print(f"Pertandingan {i} : ",end="")
    hasil = input().split()

for i in range(len(array)):
    print(f"Hasil {i+1} : {array[i]}")
print("Pertandingan selesai")
