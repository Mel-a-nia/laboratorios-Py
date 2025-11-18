Name=input("Введите ФИО: ")
inic= Name[0].upper()+"."
for i in range(len(Name)):
    if Name[i] == " " and i + 1 < len(Name): 
        inic = inic + Name [i +1]. upper ()+"." 
lage= len(Name.replace( " ",""))

print(f"ФИО:{Name}")
print(f"Инициалы: {inic}")
print(f"длина строки:{lage}")
