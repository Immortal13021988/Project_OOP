from src.prod_itarator import ProdIterator


class Product:
    """Класс с информацией о продуктах"""

    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity=0):
        """Инициализация класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """ Передача строкового значения продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Сложение стоимости продуктов на складе """
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, new_dict, prod_list):
        """ Добавление нового продукта, с проверкой на наличие и стоимости"""
        for prod in prod_list:
            if new_dict["name"] == prod.name:
                if new_dict["price"] > prod.price:
                    name, description, price, quantity = (
                        new_dict["name"],
                        new_dict["description"],
                        new_dict["price"],
                        new_dict["quantity"] + prod.quantity,
                    )
                else:
                    name, description, price, quantity = (
                        new_dict["name"],
                        new_dict["description"],
                        prod.price,
                        new_dict["quantity"] + prod.quantity,
                    )
            else:
                name, description, price, quantity = (
                    new_dict["name"],
                    new_dict["description"],
                    new_dict["price"],
                    new_dict["quantity"],
                )
            return cls(name, description, price, quantity)

    @property
    def price(self):
        """ Передача приватного параметра прайс"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """ Обновление цены товара"""
        if new_price > 0:
            if new_price < self.__price:
                user = input("Подтвердите уменьшение цены: y/n\n")
                if user.lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """Класс с информацией о категориях продуктов"""

    name = str
    description = str
    products = list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация класса"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Передача строкового значения категории товаров"""
        return f"{self.name}, количество продуктов: {sum(item.quantity for item in self.__products)}"

    def add_product(self, product: Product):
        """Добавление нового продукта в категории"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_str(self):
        """Получение строкового значения о товаре в категории"""
        new_string = ""
        for prod in self.__products:
            new_string += (
                f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
            )
        return new_string

    @property
    def products_list(self):
        """Получение товаров в категории списком"""
        new_list = []
        for prod in self.__products:
            new_list.append(prod)
        return new_list


if __name__ == "__main__":  # pragma: no cover
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    iterator = ProdIterator(category1)
    for i in iterator:
        print(i)
