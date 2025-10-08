okul=' kayseri fen high school '
print(type(okul))
tarih= '1893'

print(okul+" "+tarih)

#büyükharf

print(okul.upper())
print(okul.lower())

#harfi seçme
print(okul[3])
print(okul[0:3])
print(okul[3:])
print(okul[:-3])

#listeleme splitten sonraki paranteze yazılan harflerden böler yeva boşsa boşluklardan
print(okul.split())
print(okul.replace( "e", "E"))


#kaçış karakteri
print("sınıf başkanımız \"vehbi\"")
print("\ttaş mektep")
print(okul.startswith("M"))
print(okul.count("e"))
print(len(okul))
print(okul)
print(okul.strip())