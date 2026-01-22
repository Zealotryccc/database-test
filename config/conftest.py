# Фикстура - создает тестовую модель продукта
import pytest
from product.models import Product

@pytest.fixture
def sample_product():
    return Product.objects.create(
        name = "Test Product",
        price = "100.00",
        in_stock = True
    )

@pytest.fixture
def create_product():
    def _create_product(name, price, in_stock=True):
        return Product.objects.create(name=name,price=price,in_stock=in_stock)
    return _create_product