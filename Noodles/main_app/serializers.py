from rest_framework import serializers
from .models import Noodle


class NoodlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noodle
        fields = "__all__"
