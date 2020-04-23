
from .models import PrimaryTable,SecondTable,ThirdTable
from rest_framework import serializers
# from rest_framework import 
from rest_framework.serializers import ModelSerializers

class PrimaryTableSerializer(Serializers.ModelSerializer):

    class meta():
        model=PrimaryTable
        fields=('Unique_id')
