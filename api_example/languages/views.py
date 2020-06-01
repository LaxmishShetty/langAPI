from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Programmers, Paradigm
from .serializers import LanguageSerializer, ProgrammersSerializer, ParadigmSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammersView(viewsets.ModelViewSet):
    queryset = Programmers.objects.all()
    serializer_class = ProgrammersSerializer

