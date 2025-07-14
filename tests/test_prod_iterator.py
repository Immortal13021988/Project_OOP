import pytest

from src.prod_itarator import ProdIterator


def test_prod_iterator(prod_iterator):
    iter(prod_iterator)
    assert prod_iterator.index == 0
    assert next(prod_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(prod_iterator).name == "Iphone 15"
    with pytest.raises(StopIteration):
        next(prod_iterator)
