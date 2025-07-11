class Product:
    """Класс с информацией о продуктах"""
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_dict, products_list):
        if new_dict['name'] in products_list:
            re
        else:
            name, description, price, quantity  = new_dict['name'], new_dict['description'], new_dict['price'], new_dict['quantity']
            return Product(name, description, price, quantity)




class Category:
    """Класс с информацией о категориях продуктов"""
    name = str
    description = str
    products = list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1
    @property
    def products(self):
        new_string = ""
        for prod in self.__products:
            new_string += f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n'
        return new_string

    @property
    def products_list(self):
        new_list = []
        for prod in self.__products:
            new_list.append(prod)
        return new_list

if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    # new_product = Product.new_product(
    #     {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
    #      "quantity": 8})
    # print(new_product.name)
    # print(new_product.description)
    # print(new_product.price)
    # print(new_product.quantity)
    # print(category1.products)
    # # new_product.price = 800
    # # print(new_product.price)
    # #
    # # new_product.price = -100
    # print(new_product.price)
    # new_product.price = 0
    # print(new_product.price)