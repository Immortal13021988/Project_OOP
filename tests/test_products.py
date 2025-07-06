import pytest
from src.products import Product, Category


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
    assert len(category_1.products) == 2
    assert len(category_2.products) == 1
    assert category_1.product_count == 3
    assert category_2.product_count == 3
    assert category_1.category_count == 2
    assert category_2.category_count == 2





