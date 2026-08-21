leiviskamaara = float(input("anna leivisöjen määrä: "))
naulamaara = float(input("anna naulojen määrä: "))
luotimaara = float(input("anna luotien määrä: "))

naula = naulamaara * 32 * 13.3
leiviska = leiviskamaara * 20 * 32 * 13.3
luoti = luotimaara * 13.3

yhteensa = leiviska + naula + luoti

gramma = yhteensa % 1000
kilo = yhteensa // 1000
print(f"kilot {kilo} , grammat {gramma}.")
