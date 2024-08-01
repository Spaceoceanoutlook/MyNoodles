from rest_framework import viewsets
from .models import Noodle
from .serializers import NoodlesSerializer
from django.shortcuts import render


class NoodlesViewSet(viewsets.ModelViewSet):
    serializer_class = NoodlesSerializer

    queryset = (
        Noodle.objects.select_related("manufacturer_id")
        .select_related("country_id")
        .all()
    )


def noodle_list_view(request):
    noodles = NoodlesViewSet.queryset
    return render(request, "index.html", {"noodles": noodles})


def country_noodle_list_view(request, country_id: int):
    response = NoodlesViewSet.queryset
    noodles = response.filter(country_id=country_id)
    return render(request, "index.html", {"noodles": noodles})


def manufacturer_noodle_list_view(request, manufacturer_id: int):
    response = NoodlesViewSet.queryset
    noodles = response.filter(manufacturer_id=manufacturer_id)
    return render(request, "index.html", {"noodles": noodles})


def recommendation_noodle_list_view(request):
    response = NoodlesViewSet.queryset
    noodles = response.filter(recommendation=True)
    return render(request, "index.html", {"noodles": noodles})


def get_pho(request):
    response = NoodlesViewSet.queryset
    noodles = response.filter(title__startswith="Pho")
    return render(request, "index.html", {"noodles": noodles})
