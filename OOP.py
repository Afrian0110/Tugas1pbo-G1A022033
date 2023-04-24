class luas_Segitiga:

  def get_luas(self,alas,tinggi):
    return 0.5 * alas * tinggi

operasi = luas_Segitiga()
print("Luas segitiga dengan alas 4 dan tinggi 5 adalah = "+ str(operasi.get_luas(4,5)))
print("Luas segitiga dengan alas 7 dan tinggi 9 adalah = "+ str(operasi.get_luas(7,9)))
