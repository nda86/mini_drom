from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.urls import reverse


class Car(models.Model):
    """класс для модели элементов бд - автомобилей"""

    model = models.CharField(max_length=255, verbose_name="Марка авто")
    price = models.DecimalField(verbose_name="Цена авто", max_digits=9, decimal_places=2)
    year = models.IntegerField(verbose_name="Год выпуска авто", validators=[MinValueValidator(1900), MaxValueValidator(2021)])

    phone_regex = RegexValidator(regex=r'^\+7\d{10}$', message="Номер телефона должен быть в формате +79999999999")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона продавца", validators=[phone_regex])

    photo = models.ImageField(upload_to="photos/", verbose_name="Фото авто")

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={'pk': self.id})

    def __str__(self):
        return f"{self.model} - {self.year}: {self.price}"
