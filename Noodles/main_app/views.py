from rest_framework import viewsets
from .models import Noodle
from .serializers import NoodlesSerializer
from django.shortcuts import render
import requests


class NoodlesViewSet(viewsets.ModelViewSet):
    queryset = (
        Noodle.objects.select_related("manufacturer_id")
        .select_related("country_id")
        .all()
    )
    serializer_class = NoodlesSerializer


def noodle_list_view(request):
    response = requests.get("http://127.0.0.1:8000/api/noodles/")
    noodles = response.json()
    return render(request, "index.html", {"noodles": noodles})
