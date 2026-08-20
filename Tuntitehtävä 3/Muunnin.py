grammamäärä = int(input("Kuinka monta grammaa?: "))
gramma = grammamäärä % 1000
kilo = grammamäärä // 1000
print("määrä kiloina ja grammoina: "+str(kilo)+"kg "+str(gramma)+"g")