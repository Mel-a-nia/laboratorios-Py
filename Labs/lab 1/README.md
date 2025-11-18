# python_labs

## Лабораторная работа 1

### Задание 1

<img width="1158" height="406" alt="Foto 1" src="https://github.com/user-attachments/assets/97f174d8-7d93-49b6-9fbf-4a7f50c5ace5" />

```
имя=input("имя:")
Возраст=int(input("Возраст:"))
print(f"Привет, {имя}!Через год тебе будет {Возраст+1}")
```

<img width="387" height="101" alt="Captura de pantalla 2025-09-29 155313" src="https://github.com/user-attachments/assets/b8d5fe38-3cda-4adb-8289-d9c174425e74" />

### Задание 2}

<img width="1080" height="482" alt="Foto 2" src="https://github.com/user-attachments/assets/b28c637e-05d8-42c1-a35c-2ba853c199d6" />

```
n1=float(input("Номер 1="))
n2=float(input("Номер 2="))
sum=n1+n2
res=n1-n2
print(f"Cложение={sum:.1f}, a вычитание={res:.1f}")
```

<img width="425" height="155" alt="Captura de pantalla 2025-09-29 160304" src="https://github.com/user-attachments/assets/9c59aa7a-a50c-4902-a919-4fb514318ffd" />

### Задание 3

<img width="1004" height="634" alt="Foto 3" src="https://github.com/user-attachments/assets/fd9ecd13-bd2e-4f82-8ca9-9059efaba86f" />

```
Price=float(input("Введите цену продукта ₽:"))
Discount=float(input("введите скидку (%):"))
Vat=float(input("ввести НДС:"))
Бпс= Price - (Price * Discount/100)
НДС= Бпс* Vat/100
Total=Бпс+НДС
print(f"База после скидки : {Бпс:.2f} ₽")
print(f"НДС: {НДС:.2f} ₽")
print(f"Итого к оплате: {Total:.2f} ₽")
```

<img width="428" height="179" alt="Captura de pantalla 2025-09-29 160421" src="https://github.com/user-attachments/assets/d41b2c66-0e0e-4b36-bb2e-9ff6cfb9111a" />

### Задание 4

<img width="804" height="444" alt="Foto 4" src="https://github.com/user-attachments/assets/2d5c08ac-462e-40f3-8df3-b408f2a89ba2" />


```
Min=int(input("Введите минуты:"))
Hour=Min//60
остаток=Min%60
print(f"{Hour}:{остаток:02d}")
```

<img width="422" height="97" alt="Captura de pantalla 2025-09-29 160527" src="https://github.com/user-attachments/assets/073e9b44-596e-4a27-8ae9-eb1f69140096" />

### Задание 5

<img width="1048" height="672" alt="Foto 5" src="https://github.com/user-attachments/assets/64887afe-5608-4f32-a966-52e79a9971b5" />


```
Name=input("Введите ФИО: ")
inic= Name[0].upper()+"."
for i in range(len(Name)):
    if Name[i] == " " and i + 1 < len(Name): 
        inic = inic + Name [i +1]. upper ()+"." 
lage= len(Name.replace( " ",""))

print(f"ФИО:{Name}")
print(f"Инициалы: {inic}")
print(f"длина строки:{lage}")

```

<img width="1322" height="535" alt="Captura de pantalla 2025-09-29 161506" src="https://github.com/user-attachments/assets/abbe292b-a3c0-4b2f-807e-c045d9d2efbd" />

### Задание 6

<img width="1202" height="748" alt="Foto 6" src="https://github.com/user-attachments/assets/1bc70710-0563-4dbf-92ad-acce03888e50" />


```
X=int(input("сколько строк?: ").strip())
присутствующие= 0
online = 0
for i in range (X):
    фамилия, имя, возраст, format =input().strip().split()
    возраст1=int(возраст)
    present=format.lower()=="true"
    if present:
        присутствующие += 1
    else:
        online += 1
print(присутствующие, online)
```

<img width="1582" height="342" alt="Captura de pantalla 2025-09-29 174946" src="https://github.com/user-attachments/assets/9ea40b10-9734-4dd7-99b6-4b5395c18574" />
