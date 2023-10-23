from rest_framework import serializers

from data.models import Code


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        # fields = ['id', 'file', 'title', 'code_description', 'url',]
        fields = ['id', 'file', 'title', 'code_description',]
        
