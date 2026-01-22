import pytest 
from product.models import Product

# Тест 1 проверяем создание продукта
@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name="Apples",
        price=999.99,
        in_stock=True
    )
    assert product.name == "Apples"
    assert product.price == 999.99
    assert product.in_stock == True

# Тест 2 проверяем строковое представление
@pytest.mark.django_db
def test_product_str():
    product = Product.objects.create(
        name="IPhone",
        price=100,
        in_stock=True
    )
    assert str(product) == "IPhone"
# Тест 3 использование фикстуры
@pytest.mark.django_db
def test_with_fixture(create_product):
    product = create_product(
        name="Fixture Product",
        price=899
    )
    assert product.name == "Fixture Product"
    assert product.price == 899

# Тест 4 запросы и фильтрация
@pytest.mark.django_db
def test_filter_by_price():
    Product.objects.create(name="Банан", price=69, in_stock=True)
    Product.objects.create(name="Картошка", price=35, in_stock=True)
    Product.objects.create(name="Киви", price=5000, in_stock=True)
    
    # фильтруем дорогие и дешевые
    expensive = Product.objects.filter(price__gt=100)
    assert expensive.count() == 1

    cheap = Product.objects.filter(price__lt=100)
    assert cheap.count() == 2
    
# Тест 5: Обновление и сохранение записи
@pytest.mark.django_db
def test_update_product():
    product = Product.objects.create(
        name="Апельсины",
        price=1200,
        in_stock=True
    )
    product.name = "Голд апельсины"
    assert product.name == "Голд апельсины"

# Тест 6 на удаление данных
@pytest.mark.django_db
def test_delete_product():
    product = Product.objects.create(
        name="Чизбургер", 
        price=92,
        in_stock=True
    )
    product_id = product.id 
    product.delete()

    # проверяем что удалили
    assert Product.objects.filter(id=product_id).count() == 0