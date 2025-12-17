from data_villa import daftar_villa,kode_villa

def tampilan_menu_villa ():
  print(f"===Daftar Villa di Puncak===")
  list_villa = daftar_villa()
  for x, y in list_villa.items():
    print(f"{x}. {y ["Nama"]}")

def detail_villa(nomor_villa):
  data = kode_villa(nomor_villa)

  if data is None:
    print("Nomor Villa Tidak Ditemukan")
    print()
    tampilan_menu_villa()
    pilihan = int(input("Masukan nomor villa untuk melihat detail: "))
    print()
    detail_villa(pilihan)
    return

  print(f"===INFORMASI {data["Nama"].upper()}===")
  print("Lokasi:",data["Lokasi"])
  print("Kapasitas:",data["Kapasitas"])
  print("Harga:",data["Harga"])
  print("Fasilitas:")
  for f in data["Fasilitas"]:
    print('-',f)

def bayar(nomor_villa):
  while True:
    data = kode_villa(nomor_villa)
    print(f"===Harga {data['Nama']}===")
    print(f"Harga: {data['Harga']}")
    malam = int(input("Mau Booking Berapa Malam? [Masukan Dalam Bentuk Angka]: "))

    harga = data['Harga']
    total = malam * harga

    if malam >= 1:
      print(f"Total: {total}")
      uang = int(input("Masukan Jumlah Uang yang Ingin Anda Bayarkan: "))
      if uang > total:
        kembalian = uang - total
        print(f"Kembalian: {kembalian}")
        print("Terimakasih Telah Menggunakan Aplikasi Layanan Kami")
        break
      elif uang == total:
        print("Terimakasih Telah Menggunakan Aplikasi Layanan Kami")
        break
      elif uang < total:
        print("Uang yang Anda Masukan Kurang")

      else:
        print("Masukan Nominal Bayar ")
        break
    else:
      print("Anda Hanya Bisa Memasukan Jumlah Sewa Dalam Bentuk Angka")
      












