class ProdIterator:
    """Итератор"""

    def __init__(self, category_obj):
        """Инициализация итератора"""
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """Получение объекта для итератора"""
        return self

    def __next__(self):
        """Переход к следующему значению"""
        if self.index < len(self.category.products_list):
            prod = self.category.products_list[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration
