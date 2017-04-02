"""
from rest_framework.serializers import ModelSerializer
from stockScreener.models import stock
from .models import item


class stockSerializer(ModelSerializer):
    class Meta:
        model = stock
        fields = [
            'stockCode',
            'now',
        ]

class itemSerializer(ModelSerializer):
    class Meta:
        model = item
        fields = [
            'title',
            'url',
            'stockNum',
            'stock1Code',
            'stock2Code',
            'stock3Code',
            'createDate',
        ]
"""
