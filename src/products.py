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
        """Передача строкового значения продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение стоимости продуктов на складе"""
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

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
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )
    category_grass = Category(
        "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
    )

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
