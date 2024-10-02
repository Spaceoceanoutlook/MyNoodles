from django.db import models


class Country(models.Model):
    name: str = models.CharField(max_length=100, verbose_name="Страна", unique=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name: str = models.CharField(
        max_length=100, verbose_name="Производитель", unique=True
    )

    def __str__(self):
        return self.name


class Noodle(models.Model):
    manufacturer_id: int = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_DEFAULT,
        default="Производитель неизвестен",
        verbose_name="Производитель",
    )
    title: str = models.CharField(max_length=100, verbose_name="Название лапши")
    country_id: int = models.ForeignKey(
        Country,
        on_delete=models.SET_DEFAULT,
        default="Страна неизвестна",
        verbose_name="Страна",
    )
    description: str = models.TextField(verbose_name="Описание")
    image: models.ImageField = models.ImageField(
        upload_to="main_app/static/img", verbose_name="Фотография упаковки"
    )
    recommendation: bool = models.BooleanField(verbose_name="Рекомендуется")

    objects = models.Manager()

    def __str__(self):
        return self.title
