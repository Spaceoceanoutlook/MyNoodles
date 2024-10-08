# Generated by Django 5.0.7 on 2024-07-29 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Страна"),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Производитель"),
        ),
        migrations.AlterField(
            model_name="noodle",
            name="country_id",
            field=models.ForeignKey(
                default="Страна неизвестна",
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="main_app.country",
                verbose_name="Страна",
            ),
        ),
        migrations.AlterField(
            model_name="noodle",
            name="description",
            field=models.TextField(verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="noodle",
            name="image",
            field=models.ImageField(
                upload_to="main_app/static/img", verbose_name="Фотография упаковки"
            ),
        ),
        migrations.AlterField(
            model_name="noodle",
            name="manufacturer_id",
            field=models.ForeignKey(
                default="Производитель неизвестен",
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="main_app.manufacturer",
                verbose_name="Производитель",
            ),
        ),
        migrations.AlterField(
            model_name="noodle",
            name="recommendation",
            field=models.BooleanField(verbose_name="Рекомендуется"),
        ),
        migrations.AlterField(
            model_name="noodle",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Название лапши"),
        ),
    ]
