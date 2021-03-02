def faktorial(bil):
      if bil == 1:
          return bil
      else:
          return bil * faktorial(bil - 1)
  bil = int(input("Masukkan bilangan : "))
  if bil < 0:
      print("Bilangan faktorial yang cari tidak boleh bilangan negatif")
  elif bil == 0:
      print("Faktorial dari 0 adalah 1")
  else:
      print("Faktorial dari", bil, "adalah", faktorial(bil))
