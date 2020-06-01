from rest_framework import serializers
from .models import Language,Programmers,Paradigm


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')


class ProgrammersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmers
        fields = ('id', 'url', 'name', 'languages')
