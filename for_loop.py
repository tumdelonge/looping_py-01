# looping
# while loop
# for loop
# nested loop

# 2. for_loop
# for i in range(10):
#     print("cetak ke-",i)

# # coba2
# for i in range(1, 10):
#     print("cetak ke-",i)

# # coba3
# for i in range(2, 11, 2):
#     print("angka ke-",i)


# # coba4
# for i in range(1, 11, 2):
#     print("angka ke-",i)

# # coba4.1
# buah = ['apel', 'nanas','mangga','jeruk']
# for item in buah:
#     print(item)

# # coba5
# listBilangan = [1,2,3,4,5,6,7,8,9,1,22,23,46,78,90,100]
# for bilangan in listBilangan:
#     if bilangan % 2 == 1:
#         print("angka", bilangan,"bilangan ganjil")

# # coba6
# hewan = ['kuving','ayam','bebek']
# warna = ['merah','biru', 'kuning']

# for i in range(len(hewan)):
#     print(hewan[i], warna[i])

# coba7
hewan = ['kuving','ayam','bebek']
warna = ['merah','biru', 'kuning']

for i in hewan:
    for j in warna:
        print(i, j)
