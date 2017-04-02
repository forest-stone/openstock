"""
from rest_framework.serializers import ModelSerializer
from stockScreener.models import stock


class stockSerializer(ModelSerializer):
    class Meta:
        model = stock
        fields = [
            'stockCode',
            'now',
        ]
"""
