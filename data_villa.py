villa = {
  1:{
    "Nama":"Villa Harmonia",
    "Lokasi":"Cisarua",
    "Kapasitas":"40-50 orang",
    "Harga":3500000,
    "Fasilitas":[
      "2 Lantai","6 Kamar tidur","4 Kamar mandi","BBQ set","Kitchen set","Karaoke","Private pool","Wifi","Smart TV","Billiard","Tenis meja","Space api unggun","Halaman luas","Parkir luas","View pegunungan"
    ]
  },

  2:{
    "Nama":"Villa Teduh",
    "Lokasi":"Cisarua",
    "Kapasitas":"25-30 orang",
    "Harga":2350000,
    "Fasilitas":[
      "4 Kamar tidur","2 Kamar mandi","BBQ set","Kitchen set","Karaoke","Private pool","Wifi","Kulkas","Billiard","Halaman luas"
    ]
  },

  3:{
    "Nama":"Villa Arandra",
    "Lokasi":"Cisarua",
    "Kapasitas":"35 orang",
    "Harga":3000000,
    "Fasilitas":[
      "5 Kamar tidur","7 Tempat tidur","5 Kamar mandi","BBQ set","Kitchen set","Karaoke","Private pool","Wifi","Water heater","Billiard","Smart TV","Gazebo","Open space"
    ]
  },

  4:{
    "Nama":"Villa Sahila",
    "Lokasi":"Cisarua",
    "Kapasitas":"20 orang",
    "Harga":2800000,
    "Fasilitas":[
      "3 Kamar tidur","4 Kamar mandi","BBQ set","Kitchen set","Karaoke","Private pool","Wifi","Water heater","Billiard","Rooftop","View Pegunungan"
    ]
  },

  5:{
    "Nama":"Villa Bonita",
    "Lokasi":"Cisarua",
    "Kapasitas":"25-30 orang",
    "Harga":2000000,
    "Fasilitas":[
      "4 Kamar tidur","4 Kamar mandi","BBQ space","Kitchen set","Karaoke","Private pool","Wifi","Water heater","Billiard","Smart TV","Halaman luas","Playground","Living room"
    ]
  },

  6:{
    "Nama":"Villa Hala",
    "Lokasi":"Cisarua",
    "Kapasitas":"35 orang",
    "Harga":3250000,
    "Fasilitas":[
      "5 Kamar tidur","7 Kamar mandi","3 Lantai","BBQ space","Kitchen set","Karaoke","Private pool","Wifi","Water heater","Billiard","Tenis meja","Balkon","Living room","Smart TV","Halaman luas","Best view"
    ]
  },

  7:{
    "Nama":"Villa Nawasena",
    "Lokasi":"Megamendung",
    "Kapasitas":"30 orang",
    "Harga":2750000,
    "Fasilitas":[
      "4 Kamar tidur","6 Tempat tidur","6 Kamar mandi","Mushola","BBQ space","Kitchen set","Karaoke","Private pool","Wifi","Water heater","Billiard","Smart TV"
    ]
  },

  8:{
    "Nama":"Villa Almera",
    "Lokasi":"Cisarua",
    "Kapasitas":"25-30 orang",
    "Harga":2300000,
    "Fasilitas":[
      "4 Kamar tidur","4 Kamar mandi","BBQ set","Kitchen set","Karaoke","Private pool","Wifi","Water heater","Billiard","AC","Space api unggun","Halaman luas","Film streaming"
    ]
  },

  9:{
    "Nama":"Villa Harco",
    "Lokasi":"Cisarua",
    "Kapasitas":"30-40 orang",
    "Harga":3100000,
    "Fasilitas":[
      "4 Kamar tidur AC","4 Kamar mandi","BBQ set","Kitchen set","Karaoke","Private pool","Wifi","Water heater","Billiard","AC","Gazebo","Halaman luas","View pegunungan"
    ]
  },

  10:{
    "Nama":"Villa Elhaf",
    "Lokasi":"Cipanas",
    "Kapasitas":"20-30 orang",
    "Harga":2750000,
    "Fasilitas":[
      "4 Kamar tidur","4 Kamar mandi","BBQ","Kitchen set","Karaoke","Private pool","Wifi","Water heater","Billiard","Alat masak","Alat makan","Rice cooker","Dispenser"
    ]
  }
}

def daftar_villa():
  return villa
def kode_villa(nomor_villa):
  return villa.get(nomor_villa)

