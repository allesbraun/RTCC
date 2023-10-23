import csv
import json
import os

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from data.data_response import data_response
from data.models import Code
from data.serializer import CodeSerializer


class CodesViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        uploaded_file = self.request.data.get('file')
        if 'file' not in request.FILES:
            return Response({'error': 'File not sent'}, status=status.HTTP_400_BAD_REQUEST)
        # Verifica se a extensão do arquivo é .java
        if not uploaded_file.name.endswith('.java'):
                return Response({'error': 'The file must have a .java extension'}, status=status.HTTP_400_BAD_REQUEST)
        # Verifica o tamanho do arquivo
        max_size = 1024 * 1024  # Tamanho máximo permitido em bytes (1 MB)
        if uploaded_file.size > max_size:
            return Response({'error': 'The file is too big. The maximum size allowed is 1MB.'}, status=status.HTTP_400_BAD_REQUEST)
            
        content = uploaded_file.read().decode('utf-8')
        response_data = data_response(content, uploaded_file)
        result_json = json.loads(response_data)  # Converte a string JSON de volta para um dicionário Python

        efficiency = result_json['Efficiency']
        complexity_class = result_json['Complexity class']
        response.data['Efficiency'] = efficiency
        response.data['Complexity class'] = complexity_class
        return response
        
    
# class JavaFileViewSet(APIView):  # Use a classe APIView ao invés de ViewSet
#     def get(self, request, filename=None):  # Use o método 'get' ao invés de 'retrieve'
#         if request.method == 'GET':
#             if filename is not None:
#                 # Verifica se o arquivo Java existe no diretório 'java_files'
#                 java_file_path = os.path.join(settings.MEDIA_ROOT, filename)
#                 if os.path.exists(java_file_path):
#                     # Se o arquivo existir, retorna-o como uma resposta HTTP
#                     with open(java_file_path, 'rb') as file:                      
#                         #o download acontece por causa das linhas de baixo
#                         response = HttpResponse(file)
#                         response['Content-Type'] = 'application/octet-stream'
#                         response['Content-Disposition'] = f'attachment; filename="{filename}"'
#                         return response                  
#                 else:
#                     # Se o arquivo não existir, retorna uma resposta 404
#                     return Response(status=status.HTTP_404_NOT_FOUND)
#             else:
#                 java_files_dir = settings.MEDIA_ROOT
#                 files = os.listdir(java_files_dir)
#                 return Response({"files": files})
            
#     def post(self, request, filename = None):
#         if request.method == 'POST':            
#             uploaded_file = request.FILES['file']
#             content = uploaded_file.read().decode('utf-8')

#             # Verificar se a pasta 'java_files' já existe
#             if not os.path.exists(settings.MEDIA_ROOT):
#                 # Se não existir, criar a pasta
#                 os.makedirs(settings.MEDIA_ROOT)
#             # Salvar o arquivo no diretório 'java_files'
#             file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
#             with open(file_path, 'wb') as file:
#                 # file.write(uploaded_file.read())
#                 file.write(content.encode('utf-8'))
                
#             # Armazena a eficiência e a complexidade do código em um dicionário
#             response_data = data_response(content, uploaded_file)
#             result_json = json.loads(response_data)  # Converte a string JSON de volta para um dicionário Python

#             efficiency = result_json['Efficiency']
#             complexity_class = result_json['Complexity class']

#             # Constrói a string de resposta
#             response_text = f'Efficiency: {efficiency}, Complexity class: {complexity_class}'

#             return HttpResponse(response_text, content_type="text/plain")
            