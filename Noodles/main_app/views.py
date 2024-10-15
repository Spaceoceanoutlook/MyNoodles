from rest_framework import viewsets
from .models import Noodle, Country
from .serializers import NoodlesSerializer
from django.shortcuts import render
from django.db.models import Q


class NoodlesViewSet(viewsets.ModelViewSet):
    serializer_class = NoodlesSerializer

    queryset = (
        Noodle.objects.select_related("manufacturer_id")
        .select_related("country_id")
        .order_by("-id")
    )


def noodle_list_view(request):
    noodles = NoodlesViewSet.queryset
    countries = Country.objects.all()
    return render(request, "index.html", {"noodles": noodles, "countries": countries})


def country_noodle_list_view(request, country_id: int):
    response = NoodlesViewSet.queryset
    noodles = response.filter(country_id=country_id)
    countries = Country.objects.all()
    manufactures = {}
    for i in noodles:
        if i.manufacturer_id not in manufactures:
            manufactures[i.manufacturer_id] = i.manufacturer_id.id
    return render(
        request,
        "index.html",
        {
            "noodles": noodles,
            "countries": countries,
            "manufactures": manufactures,
        },
    )


def manufacturer_noodle_list_view(request, manufacturer_id: int):
    response = NoodlesViewSet.queryset
    noodles = response.filter(manufacturer_id=manufacturer_id)
    countries = Country.objects.all()
    return render(request, "index.html", {"noodles": noodles, "countries": countries})


def recommendation_noodle_list_view(request):
    response = NoodlesViewSet.queryset
    noodles = response.filter(recommendation=True)
    countries = Country.objects.all()
    return render(request, "index.html", {"noodles": noodles, "countries": countries})


def search(request):
    query = request.GET.get("query", "").title()
    response = NoodlesViewSet.queryset
    noodles = response.filter(
        Q(title__startswith=query)
        | Q(manufacturer_id__name__startswith=query)
        | Q(country_id__name__startswith=query)
    )
    countries = Country.objects.all()
    return render(request, "index.html", {"noodles": noodles, "countries": countries})


def noodle(request, noodle_id: int):
    response = NoodlesViewSet.queryset
    noodles = response.filter(id=noodle_id)
    countries = Country.objects.all()
    return render(request, "index.html", {"noodles": noodles, "countries": countries})
