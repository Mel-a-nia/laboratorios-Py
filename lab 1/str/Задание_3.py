Price=float(input("Введите цену продукта ₽:"))
Discount=float(input("введите скидку (%):"))
Vat=float(input("ввести НДС:"))
Бпс= Price - (Price * Discount/100)
НДС= Бпс* Vat/100
Total=Бпс+НДС
print(f"База после скидки : {Бпс:.2f} ₽")
print(f"НДС: {НДС:.2f} ₽")
print(f"Итого к оплате: {Total:.2f} ₽")