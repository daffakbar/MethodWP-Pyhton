# Metode WP (Weight Product)
Metode Weighted Product (WP) menggunakan perkalian untuk menghubungkan rating atribut, dimana rating setiap atribut harus dipangkatkan dengan bobot atribut yang bersangkutan. Proses tersebut sama halnya dengan normalisasi (Sri Kusumadewi, 2006)

## Studi kasus
Menentukan pemilihan karyawan terbaik
kriteria yang digunakan :

1. C1 = Kedisiplinan 
2. C2 = Kinerja 
3. C3 = Tanggung Jawab 
4. C4 = Prestasi 
5. C5 = Kerjasama 

Bobot Kriteria
| Kriteria  | Bobot  |
| :------------ |---------------:| 
| C1. | 3 | 
| C2. | 3 | 
| C3. | 1 | 
| C4. | 1 | 
| C5. | 2 | 
| Total | 10 | 

Perhitungan Bobot kriteria\
Cn = nilai Cn/Total kriteria \

contoh perhitungan\
C1 = 3/10 = 0,3\
C2 = 3/10 = 0,3\
C3 = 1/10 = 0,1\
dst

Diperoleh :\
C1 = 0,3\
C2 = 0,3\
C3 = 0,1\
C4 = 0,1\
C5 = 0,2

---
#### Daftar nama karyawan (Alternatif)
Diberikan nilai dari angka 1 - 100, sebagai berikut :

| No.  | Nama karyawan  | Kedisiplinan | Kinerja | Tanggung Jawab | Prestasi | Kerjasama |
| :------------ |:---------------:|:---------------:|:---------------:|:---------------:|:---------------:| -----:|
| A1. | Azmi | 74 | 75 | 60 | 63 | 75 |
| A2. | Ayu | 75 | 85 | 75 | 64 | 75 |
| A3. | Antoni | 85 | 78 | 80 | 70 | 60 |

---
Proses menentukan prioritas alternatif terbaik dibutuhkan pembobotan pada
setiap kriteria

#### Disiplin (C1)
| C1.  | Keterangan  | Nilai |
| :------------ |:---------------:| -----:|
| >= 85. | Sangat Baik(SB)  | 1 |
| 84 – 75 | Baik (B) | 0,75 |
| 74 – 65 | Cukup Baik (CB)  | 0,50 |
| 64 <= | Kurang Baik(KB)  | 0,25 |

#### Kinerja (C2)
| C2.  | Keterangan  | Nilai |
| :------------ |:---------------:| -----:|
| >= 85. | Sangat Baik(SB)  | 1 |
| 84 – 75 | Baik (B) | 0,75 |
| 74 – 65 | Cukup Baik (CB)  | 0,50 |
| 64 <= | Kurang Baik(KB)  | 0,25 |

#### Tanggung Jawab (C3)
| C3.  | Keterangan  | Nilai |
| :------------ |:---------------:| -----:|
| >= 85. | Sangat Baik(SB)  | 1 |
| 84 – 75 | Baik (B) | 0,75 |
| 74 – 65 | Cukup Baik (CB)  | 0,50 |
| 64 <= | Kurang Baik(KB)  | 0,25 |

#### Prestasi (C4)
| C4.  | Keterangan  | Nilai |
| :------------ |:---------------:| -----:|
| >= 85. | Sangat Baik(SB)  | 1 |
| 84 – 75 | Baik (B) | 0,75 |
| 74 – 65 | Cukup Baik (CB)  | 0,50 |
| 64 <= | Kurang Baik(KB)  | 0,25 |

#### Kerjasama (C5)
| C5.  | Keterangan  | Nilai |
| :------------ |:---------------:| -----:|
| >= 85. | Sangat Baik(SB)  | 1 |
| 84 – 75 | Baik (B) | 0,75 |
| 74 – 65 | Cukup Baik (CB)  | 0,50 |
| 64 <= | Kurang Baik(KB)  | 0,25 |

#### Daftar nama karyawan (Nilai alternatif setiap kriteria)
| No.  | Nama karyawan  | C1 | C2 | C3 | C4 | C5 |
| :------------ |:---------------:|:---------------:|:---------------:|:---------------:|:---------------:| -----:|
| A1. | Azmi | 0,50 | 0,75 | 0,25 | 0,25 | 0,75 |
| A2. | Ayu | 0,75 | 1 | 0,75 | 0,25 | 0,75 |
| A3. | Antoni | 1 | 0,75 | 0,75 | 0,50 | 0,25 |

---
### Menghitung nilai vektor S
RUMUS\
Sn = alternatif1 pangkat W1 x alternatif2 pangkat W2 x ... x alternatif5 pangkat W5

S1 (Azmi) = (0.50^0,3) (0.75^0,3) (0.25^0,1)(0.25^0,1)(0.75^0,2) = 0,533 \
S2 = (0.75^0,3) (1^0,3) (0.75^0,1) (0.25^0,1) (0.75^0,2) = 0,630 \
S3 = (1^0,3) (0.75^0,3) (0.75^0,1) (0.50^0,1) (0.25^0,2) = 0,733 \
Total S = S1+S2+S3 = 1,896
### Menghitung nilai vektor V
RUMUS\
Vn = Sn/Total S

V1 = 0,533/1,896 = 0,281 \ 
V2 = 0,630/1,896 = 0,332 \
V3 = 0,733/1,896 = 0,386 \

#### HASIL 
| No.  | Nama Karyawan  | Nilai |
| :------------ |:---------------:| -----:|
| 1. | Antoni  | 0,386 |
| 2 | Ayu | 0,332 |
| 3 | Azmi  | 0,281 |

Keputusan Alternatif Terbaik adalah ANTONi dengan nilai 0,386 

