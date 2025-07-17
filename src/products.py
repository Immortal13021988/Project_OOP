from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class MixinLog:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, MixinLog):
    """Класс с информацией о продуктах"""

    def __init__(self, name, description, price, quantity=0):
        """Инициализация класса"""
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        """Передача строкового значения продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение стоимости продуктов на складе"""
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, new_dict, prod_list):
        """Добавление нового продукта, с проверкой на наличие и стоимости"""
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
        """Передача приватного параметра прайс"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Обновление цены товара"""
        if new_price > 0:
            if new_price < self.__price:
                user = input("Подтвердите уменьшение цены: y/n\n")
                if user.lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет


class LawnGrass(Product):  # Газонная трава
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country  # страна производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color  # цвет


class Category:
    """Класс с информацией о категориях продуктов"""

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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        """Получение средней цены всех товаров"""
        try:
            return round(
                sum([prod.price for prod in self.__products]) / len(self.__products), 2
            )
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
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


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products_list))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products_list))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
