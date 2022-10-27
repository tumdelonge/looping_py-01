# menggunakan while() lakukan print Push Up ke x, lalu pada  push up ke-50 print minum, lalu apaila push up = 100 print capek
print("Push Up")
x = int(input("masukkan niai max : "))
awal = 1

while awal <= x:
    if awal == 50:
        print("Minum")
    elif awal == 100:
        print("Capek")
    else:
        print("Push up ke-",awal)
    awal +=1