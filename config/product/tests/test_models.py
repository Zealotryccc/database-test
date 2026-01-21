import pytest 
from product.models import Product

#Тест первый проверяем созд продукта
def test_product_creation():
    product = Product.objects.create(
        name = "Apples",
        price = 999.99,
        in_stock = True
    )
    assert product.name == "Aplles"
    assert product.price == 999.99
    assert product.in_stock == True