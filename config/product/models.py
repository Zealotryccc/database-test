from django.db import models

# Create your models here.
# Создаем обычную модель
class Product(models.Model):
    name = models.CharField(max_length=100) # поле с огр по симв
    price = models.DecimalField(max_digits=10,decimal_places=2) # поле для деняг цельная валюта слева копейки справа
    in_stock = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    #Создаем метод
    def apply_discount(self,percent):
        #применяем скидку
        self.price = self.price*(100-percent)/100
        self.save ()
