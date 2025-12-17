import menu_villa as mv
import data_user as dur

print("SELAMAT DATANG DI BOOKING.COM")
mv.tampilan_menu_villa()
pilihan = int(input("Masukan nomor villa untuk melihat detail: "))
print()
mv.detail_villa(pilihan)

while True:
  booking = input("Apakah anda ingin melakukan booking villa?  [YES?NO]: ").upper()
  print()
  if booking == "YES":
    print("Silahkan masukan data diri anda")
    dur.info_user()
    print()
    transaksi = input("apakah anda ingin melakukan transaksi? [Ya/Tidak]: ").upper()

    if transaksi == 'YA':
      mv.bayar(pilihan)
      keluar = input("Klik Exit Untuk Keluar Aplikasi: ").upper()
      if keluar == "EXIT":
        break
      else:
        keluar = input("Inputan Anda Salah Silahkan Masukan Ulang: ").upper()
        break

    elif transaksi =='TIDAK':
      print("Terimakasih Semoga Datang Kembali")
      print()
      mv.tampilan_menu_villa()
      pilihan = int(input("Masukan nomor villa untuk melihat detail: "))
      print()
      mv.detail_villa(pilihan)
    else:
      print("inputan salah")

  elif booking == "NO":
    mv.tampilan_menu_villa()
    pilihan = int(input("Masukan nomor villa untuk melihat detail: "))
    print()
    mv.detail_villa(pilihan)

  else:
    print("Inputan anda salah")

