import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from data.data_response import data_response
from data.models import Code
from data.serializer import CodeSerializer


class CodesAPIView(APIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    def get(self, request, format=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def post(self, request, format=None):
        
        if 'file' not in request.FILES:
            return Response({'error': 'File not sent'}, status=status.HTTP_400_BAD_REQUEST)
        
        uploaded_file = request.FILES['file']
        
        if not uploaded_file.name.endswith('.java'):
            return Response({'error': 'The file must have a .java extension'}, status=status.HTTP_400_BAD_REQUEST)
        
        max_size = 1024 * 1024  # Tamanho máximo permitido em bytes (1 MB)
        if uploaded_file.size > max_size:
            return Response({'error': 'The file is too big. The maximum size allowed is 1MB.'}, status=status.HTTP_400_BAD_REQUEST)
            
        content = uploaded_file.read().decode('utf-8')
        print(f'O conteúdo do arquivo é: {content}')
        
        response_data = data_response(content, uploaded_file)
        result_json = json.loads(response_data)  # Converte a string JSON de volta para um dicionário Python

        efficiency = result_json['Efficiency']
        complexity_class = result_json['Complexity class']
        
        response_data = {
            'Efficiency': efficiency,
            'Complexity class': complexity_class
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)
