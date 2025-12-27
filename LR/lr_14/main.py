"""
- - - ЛАБАРАТОРНАЯ РАБОТА №14 КЛАССЫ - - -
Есть класс товар, который содержит поля:
артикул, наименование, количество поставки товара, цена поставки, количество проданного товара
Пусть значения заданы корректно.
Цена продажи - цена поставки * 1.15

Необходимо реализовать меню со следующими пунктами:
1. Заполнение списка товарами (список товаров из экз класс товар)
2. Выдача остатков по каждому товару
3. Стоимость продаж по каждому товару
4. Общая прибыль
5. Выход
"""

class Product:
    def __init__(self, id, name, amount_buy, price, amount_sale):
        self.id = id
        self.name = name
        self.amount_buy = amount_buy
        self.price = price
        self.amount_sale = amount_sale

    def ost(self):
        return int(self.amount_buy) - int(self.amount_sale)

    def vur(self):
        return int(self.amount_sale) * int(self.price) * 1.15

    def prib(self):
        return (int(self.amount_sale) * int(self.price) * 1.15) - (int(self.amount_sale) * int(self.price))



ww = []

while True:
    inp = int(input("""
1. Добавить товар
2. Выдача остатков по каждому товару
3. Стоимость продаж по каждому товару
4. Общая прибыль
5. Выход
"""))
    if inp == 1:
        idT, nameT, amount_buyT, priceT, amount_saleT = input("Введите артикул, наименование, количество поставки товара, цена поставки, количество проданного товара через пробел\n").split(' ')
        ww.append(Product(idT, nameT, amount_buyT, priceT, amount_saleT))
    if inp == 2:
        for i in ww:
            print(f"Товар: {i.name} Остаток: {i.ost()}\n------------------------")
    if inp == 3:
        for i in ww:
            print(f"Товар: {i.name} Выручка: {i.vur()}\n------------------------")
    if inp == 4:
        for i in ww:
            print(f"Товар: {i.name} Прибыль: {i.prib()}\n------------------------")
    if inp == 5:
        exit(0)