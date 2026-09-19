#Bagasi_1 = 12
#Bagasi_2 = 18
#Bagasi_3 = 7
#Bagasi_4 = 15
#Bagasi_5 = 20
#Bagasi_6 = 10

Bagasi = [12, 18, 7, 15, 20, 10]

Total_Berat_Akhir = Bagasi[0] + Bagasi[1] + Bagasi[2] + Bagasi[3] + Bagasi[4] + Bagasi[5]

Total_Berat_Akhir_Fix = Total_Berat_Akhir * 1000

Kompensasi = Total_Berat_Akhir * 5/100

Total_Berat_Akhir_Dengan_Kompensasi_KG = Total_Berat_Akhir + Kompensasi

Total_Berat_Akhir_Dengan_Kompensasi = Total_Berat_Akhir_Dengan_Kompensasi_KG * 1000

Jumlah_Data = len (Bagasi)

Rata_Rata = Total_Berat_Akhir / Jumlah_Data

NIM = 24

Bolean = NIM < Rata_Rata

print("Total Berat Akhir Bagasi Adalah : ", Total_Berat_Akhir_Fix,"gram"), print("Rata-Rata Berat Bagasi Adalah : ", Rata_Rata,"Kg"), print("Kompensasi Adalah : ", Kompensasi,"Kg"), print("Total Berat Akhir ditambah Kompensasi : ", Total_Berat_Akhir_Dengan_Kompensasi,"gram"), print("Jumlah Data Bagasi Adalah : ", Jumlah_Data), print("NIM : ", NIM), print("Apakah NIM Lebih Kecil dari Rata-Rata? : ", Bolean), print("berat bagasi milik para penumpang tengah adalah : ", Bagasi[2:5])