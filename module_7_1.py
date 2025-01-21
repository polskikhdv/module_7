from tkinter.font import names


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self._products = set()

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return file.read()

    def add(self, *products):
        for product in products:
            if product not in self._products:
                self._products.add(product)
                with open(self.__file_name, 'a', encoding='utf-8') as file:
                    file.write(str(product) + '\n')
            else:
                print("Продукт", product.name, "уже есть в магазине")

# Пример использования классов
shop = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")
p4 = Product('potato', 12, "veg")


shop.add(p1)

print(shop.get_products())