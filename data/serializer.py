from rest_framework import serializers

from data.models import Code


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['id', 'file', 'title',]
        
