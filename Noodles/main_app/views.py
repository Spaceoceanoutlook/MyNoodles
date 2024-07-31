from rest_framework import viewsets
from .models import Noodle
from .serializers import NoodlesSerializer
from django.shortcuts import render
import requests


class NoodlesViewSet(viewsets.ModelViewSet):
    serializer_class = NoodlesSerializer

    queryset = (
        Noodle.objects.select_related("manufacturer_id")
        .select_related("country_id")
        .all()
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get("country", None)
        manufacturer = self.request.query_params.get("manufacturer", None)
        if country is not None:
            queryset = (
                Noodle.objects.select_related("manufacturer_id")
                .select_related("country_id")
                .filter(country_id=country)
            )
        if manufacturer is not None:
            queryset = (
                Noodle.objects.select_related("manufacturer_id")
                .select_related("country_id")
                .filter(manufacturer_id=manufacturer)
            )
        return queryset


def noodle_list_view(request):
    response = requests.get("http://127.0.0.1:8000/api/noodles/")
    noodles = response.json()
    return render(request, "index.html", {"noodles": noodles})


def country_noodle_list_view(request, country_id: int):
    response = requests.get(f"http://127.0.0.1:8000/api/noodles/?country={country_id}")
    noodles = response.json()
    return render(request, "index.html", {"noodles": noodles})


def manufacturer_noodle_list_view(request, manufacturer_id: int):
    response = requests.get(
        f"http://127.0.0.1:8000/api/noodles/?manufacturer={manufacturer_id}"
    )
    noodles = response.json()
    return render(request, "index.html", {"noodles": noodles})
