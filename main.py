purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

"""
За место purchases можно использовать другие списки словарей.
Например распарсить и добавить в purchases (.txt, .csv и т.д).
"""

class AnalyzeScript:

    def __init__(self, data):
        self.data = data

    def total_revenue(self):
        """
        Рассчитываем и возвращаем общую выручку (цена * количество для всех записей).
        """
        total = sum([i["price"] * i["quantity"] for i in self.data])
        return f"Общая выручка {total}"

    def items_by_category(self):
        """
        Возвращаем словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
        """
        result = dict()
        for item in self.data:
            result.setdefault(item["category"], []).append(item["item"])
        return f"Товары по категориям: {result}"

    def expensive_purchases(self, min_price = min([i["price"] for i in purchases])): # Указали min_price из purchases
        """
        Выводим все покупки, где цена товара больше или равна min_price.
        """
        result = []
        for item in self.data:
            if min_price <= item["price"] and item["quantity"] != 0:
                result.append(item)
        return f"Покупки дороже {min_price}: {result}"

    def average_price_by_category(self):
        """
        Рассчитываем среднюю цену товаров по каждой категории.
        """
        res_all_prices = dict()
        for i in self.data:
            res_all_prices.setdefault(i["category"], []).append(i["price"]) # Распарсили все цены

        res_avg_prices = dict()
        for j in res_all_prices:
            res_avg_prices.setdefault(j, round(sum(res_all_prices[j]) / len(res_all_prices[j]), 2)) # Из res_all_prices, суммировали словарь с ценами
        return f"Средняя цена по категориям: {res_avg_prices}"

    def most_frequent_category(self):
        """
        Находим и возвращаем категорию, в которой куплено больше всего единиц товаров.
        """
        result = [i["category"] for i in self.data if i["quantity"] == max([i["quantity"] for i in self.data])]
        return f"Категория с наибольшим количеством проданных товаров: {result[0] if len(list(set(result))) == 1 else list(set(result))}"

x = AnalyzeScript(purchases)
print(x.total_revenue(), x.items_by_category(), x.expensive_purchases(), x.average_price_by_category(), x.most_frequent_category(), sep='\n')






