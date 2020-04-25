
from .models import PrimaryTable,SecondTable,ThirdTable
from rest_framework import serializers
# from rest_framework import 
from rest_framework.serializers import ModelSerializer

class PrimaryTableSerializer(serializers.ModelSerializer):

    class Meta():
        model=PrimaryTable
        fields="__all__"
