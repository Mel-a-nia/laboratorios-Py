Min=int(input("Введите минуты:"))
Hour=Min//60
остаток=Min%60
print(f"{Hour}:{остаток:02d}")