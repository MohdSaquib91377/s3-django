from rest_framework import serializers
from .models import DropBoxer


class DropBoxerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropBoxer
        fields = "__all__"
