from unittest.mock import patch, MagicMock

from src.products import Product


def test_product_init_1(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_2(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == ("Смартфоны, как средство не только коммуникации, "
                                      "но и получения дополнительных функций для удобства жизни")
    assert category_2.name == "Телевизоры"
    assert category_2.description == ("Современный телевизор, который позволяет "
                                      "наслаждаться просмотром, станет вашим другом и помощником")
    assert len(category_1.products_list) == 2
    assert len(category_2.products_list) == 1
    assert category_1.product_count == 3
    assert category_2.product_count == 3
    assert category_1.category_count == 2
    assert category_2.category_count == 2


def test_product_new_product_1(product_new_1, category_1):
    product_new_1 = Product.new_product(product_new_1, category_1.products_list)
    assert product_new_1.quantity == 10
    assert product_new_1.price == 180000.0


def test_product_new_product_2(product_new_2, category_1):
    product_new_2 = Product.new_product(product_new_2, category_1.products_list)
    assert product_new_2.quantity == 11
    assert product_new_2.price == 181000.0


def test_product_new_product_4(product_new_4, category_1):
    product_new_4 = Product.new_product(product_new_4, category_1.products_list)
    assert product_new_4.quantity == 5
    assert product_new_4.price == 100000.0


def test_product_price_1(product_new_3, category_1):
    new_product = Product.new_product(product_new_3, category_1.products_list)
    new_product.price = 181000
    assert new_product.price == 181000
    new_product.price = 0
    assert new_product.price == 181000


@patch('builtins.input')
def test_product_price_2(mock_input, product_new_3, category_1):
    mock_input.return_value = 'y'
    new_product = Product.new_product(product_new_3, category_1.products_list)
    new_product.price = 179000.0
    assert new_product.price == 179000
    mock_input.return_value = 'n'
    new_product.price = 178000.0
    assert new_product.price == 179000
    mock_input.return_value = 'yes'
    new_product.price = 178000.0
    assert new_product.price == 179000


def test_category_add_product(category_1, product_3):
    assert len(category_1.products_list) == 2
    category_1.add_product(product_3)
    assert len(category_1.products_list) == 3


def test_category_prodict_str(category_2):
    assert category_2.products_str == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
