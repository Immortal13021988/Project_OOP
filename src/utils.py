import json
import logging
import os

from src.products import Category, Product

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json(path: str) -> list[dict]:
    """
    Функция чтения JSON-файла, возвращает список словарей с данными
    """
    try:
        logger.info("Выполняем открытия JSON-файла")
        full_path = os.path.abspath(path)
        with open(full_path, encoding="utf-8") as json_file:
            data = json.load(json_file)
        logger.info("Проверяем соответствие содержимого файла")
        if type(data) is list:
            logger.info("Проверка файла прошла успешно")
            return data
        else:
            logger.error("Проверка файла провалена (содержимое файла не соответствует)")
            return []
    except (json.JSONDecodeError, FileNotFoundError) as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []


def create_list_from_json(data: list) -> list:
    """
    Функция получает список словарей с данными, создает объект из полученных данных
    """
    try:
        categories = []
        for category in data:
            products = []
            for prod in category["products"]:
                products.append(Product(**prod))
            category["products"] = products

            categories.append(Category(**category))
        return categories
    except Exception:
        return []


if __name__ == "__main__":  # pragma: no cover
    file_list = read_json("../data/products.json")
    categories = create_list_from_json(file_list)
    prof = categories[0].products_list
    for pr in prof:
        print(pr.name)
        print(pr.description)
        print(pr.price)
        print(pr.quantity)
    print(categories[0].name)
    print(categories[0].description)

    prof = categories[1].products_list
    for pr in prof:
        print(pr.name)
        print(pr.description)
        print(pr.price)
        print(pr.quantity)
    print(categories[1].name)
    print(categories[1].description)

    print(Category.category_count)
    print(Category.product_count)
