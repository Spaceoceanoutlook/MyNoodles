from rest_framework import serializers
from .models import Noodle, Manufacturer, Country


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "name"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name"]


class NoodlesSerializer(serializers.ModelSerializer):
    manufacturer_id = ManufacturerSerializer()
    country_id = CountrySerializer()

    class Meta:
        model = Noodle
        fields = "__all__"
