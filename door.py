door = ["Kayu Jati", "Kayu Pinus", "Kayu Mahoni", "Kayu Akasia", "Kayu Nangka"]
print(door[3])

#append itu menambahkan data dari belakang
door.append("Kayu Kamper")

#pop menghapus data
door.pop(2)
print(door)

door = ("Kayu Biasa", "Kayu Premiumn", "Kayu best Quality")
update = list(door)
update[0] = "Kayu Jelek"
tuple = tuple(update)
print(tuple)