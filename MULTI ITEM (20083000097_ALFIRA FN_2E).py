# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("")
print("================================")
print("KANTIN UNIV. TEKNOLOGI INFORMASI")
print("================================")
print("Menu Makanan")
print("a. Nasi Goreng          Rp. 15.000")
print("b. Lontong Goreng       Rp. 14.900")
print("c. Bakso Goreng         Rp. 12.900")
print("d. Rujak Goreng         Rp. 13.000")
print("e. Rujak Bakso          Rp. 15.000")
print("f. Rujak Bakso Pecel    Rp. 17.000")
print("================================")
print("Menu Minuman")
print("a. Teh dingin/hangat/panas    2500")
print("b. Kopi Dingin                5000")
print("c. Kopi Teh Panas             6500")
print("d. Coca Cola Dingin           3500")
print("e. Coca Cola Panas            5000")
print("================================")
print("")


#1. SIAPKAN VARIABEL
kode =['a','b','c','d','e','f','g','h','i','j','k']
namaMakanan_Minuman =['Nasi Goreng','Lontong Goreng','Bakso Goreng',
                      'Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel',
                      'Teh dingin/hangat/panas','Kopi dingin','Kopi Teh Panas',
                      'Coca Cola Dingin','Coca Cola Panas']
harga =[15000,14900,12900,13000,1000,17000,2500,5000,6500,3500,5000]

#2. INPUT BARANG
pilihan = input(">> Masukkan Kode Makanan atau Minuman    = ")

#3. INPUT QTY
qty     = input(">> Masukkan Jumlah Pesanan  = ")

#4. HITUNG BAYAR
##cek nama barang dan ambil harga satuan
i = 0
while i<len(namaMakanan_Minuman):
        #jika value pada list kode[i] == pilihan
            if kode[i] == pilihan:
            #ambil nama barang
                nm_brg = namaMakanan_Minuman[i]

            #ambil harga satuan
                hrgsat = harga[i]
            
        #jika tidak cocok, lanjut ke i berikutnya
                i+=1
            
            
            tot_byr = int(hrgsat) * int(qty)
            
#5. TAMPILKAN
print(">>> NAMA BARANG      : " + nm_brg)
print(">>> HARGA BARANG     : Rp." + str(hrgsat))
print(">>> JUMLAH BARANG    : " + qty)
print(("-------------------------------"))
print(">>> TOTAL BAYAR      : Rp." + str(tot_byr))
uang = input(">>> UANG             : Rp.")
x = int(uang)
kembalian = x - tot_byr
print("Kembalian            : Rp."+ str(kembalian))

