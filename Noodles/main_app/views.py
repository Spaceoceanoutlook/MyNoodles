from rest_framework import viewsets
from .models import Noodle
from .serializers import NoodlesSerializer


class NoodlesViewSet(viewsets.ModelViewSet):
    queryset = Noodle.objects.all()
    serializer_class = NoodlesSerializer
