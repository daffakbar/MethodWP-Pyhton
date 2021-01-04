# Metode Weight Product (WP)

# Menentukan pemilihan karyawan terbaik, terdapat 5 kriteria sbg berikut:
# C1 = Kedisiplinan
# C2 = Kinerja
# C3 = Tanggung Jawab
# C4 = Prestasi
# C5 = Kerjasama

# Tiap kriteria diberikan nilai bobot
kriteria = [
    3, #C1
    3, #C2
    1, #C3
    1, #C4
    2  #C5
] 
# print(kriteria[2])
n = 0
for key in kriteria :
    n += key
# print(n)
w =[]
c = 0
for key in kriteria :
    w.append(round(kriteria[c]/n,2))
    c+= 1
print("===Bobot W kriteria===")
print(w)
# Hasil [0.3, 0.3, 0.1, 0.1, 0.2]
# ===============================
# nilai pembobotan alternatif
alternatifs = [
    [0.50, 0.75, 0.25, 0.25, 0.75], #Azmi
    [0.75, 1, 0.75, 0.25, 0.75], #Ayu
    [1, 0.75, 0.75, 0.50, 0.25], #Antoni
]

# RUMUS
# S1 = alternatif1 pangkat W1 x alternatif2 pangkat W2 x ... x alternatif5 pangkat W5
# contoh :
# S1 azmi = 0.50^0.3 x 0.75^0.3 x 0.25^0.1 x 0.25^0.1 x 0.75^0.2
# S1 azmi = 0.5333          
s = []
indexalt = 0

for alternatif in alternatifs:
    for alt in alternatifs[indexalt]:
        i = 0
        for value in w:
            # if alt.index == 1
            # print(alt[0])
            print(round(alt**value,3))
            # i+=1
    indexalt+=1
#codingannya masih belum menemukan logikanya mas, outputnya tidak sesuai


# s.append(alternatif[0])
# for key2 in alternatif:
#     for key in alternatif[indexalt]:
#         for key3 in w:  
#             s.append(key)
#     indexalt+=1
# for i in range(0,5):
#     for ss in s :
        # print(ss**w[i])
        # print(ss)
# print(alternatif)
# print("=====")
# print(w)

# for value in alternatif:
#     # print(value)
#     for value2 in w:
#         s.append(value**value2)

# print(s)
# for key3 in w:
#     print(key3)  

# for key2 in alternatif:
#     s.append(alternatif[indexalt])
    # indexalt+=1
# for key2 in alternatif:
#     # print(key2)
#     for key in w :
#         # print(key)
#         # s.append(round(key2[1]**key, 2))
#         s.append(round(alternatif[indexalt][indexalt]))
#         # for i in range(5):
#         # s.append(key2)
#         indexalt+=1


# listy = [[] for i in range(3)]
# print(listy)

# for n in alternatif :
#     for value in n:
#         for key1 in w :
#             s.append(round(value**key1, 2))
    
# for key in alternatif[indexalt] :
#     for key1 in w :
#         # print(key)

#         # listy = [[] for i in range(3)]
#         s.append(key**key1)
#         # nestlist = listy[0]
#     indexalt+= 1
# # print(s)

# print(nestlist)
# arr = []
# for i in range(3):
#     arr.append([])
#     for j in range(5):
#         arr[i].append(i*j)
# print(arr)