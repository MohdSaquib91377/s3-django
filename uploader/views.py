from django.shortcuts import render
from rest_framework import viewsets,parsers
from .models import DropBoxer
from .serializers import DropBoxerSerializer

# Create your views here.
class DropBoxViewset(viewsets.ModelViewSet):
    queryset = DropBoxer.objects.all()
    serializer_class = DropBoxerSerializer
    parser_classes = [parsers.MultiPartParser,parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']