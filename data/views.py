import csv
import os

from django.conf import settings
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from data.data_response import data_response
from data.models import Code
from data.serializer import CodeSerializer


class CodesViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    
    

class JavaFileViewSet(APIView):  # Use a classe APIView ao invés de ViewSet
    def get(self, request, filename=None):  # Use o método 'get' ao invés de 'retrieve'
        if request.method == 'GET':
            if filename is not None:
                # Verifica se o arquivo Java existe no diretório 'java_files'
                java_file_path = os.path.join(settings.MEDIA_ROOT, filename)
                if os.path.exists(java_file_path):
                    # Se o arquivo existir, retorna-o como uma resposta HTTP
                    with open(java_file_path, 'rb') as file:                      
                        #o download acontece por causa das linhas de baixo
                        response = HttpResponse(file)
                        response['Content-Type'] = 'application/octet-stream'
                        response['Content-Disposition'] = f'attachment; filename="{filename}"'
                        return response                  
                else:
                    # Se o arquivo não existir, retorna uma resposta 404
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                java_files_dir = settings.MEDIA_ROOT
                files = os.listdir(java_files_dir)
                return Response({"files": files})
            
    def post(self, request, filename = None):
        if request.method == 'POST':
            if 'file' not in request.FILES:
                return Response({"error": "Arquivo não enviado"}, status=status.HTTP_400_BAD_REQUEST)
            # Verifica se a extensão do arquivo é .java
            if not uploaded_file.name.endswith('.java'):
                return Response({'error': 'O arquivo deve ter extensão .java'}, status=status.HTTP_400_BAD_REQUEST)
            # Verifica o tamanho do arquivo
            max_size = 1024 * 1024  # Tamanho máximo permitido em bytes (1 MB)
            if uploaded_file.size > max_size:
                return Response({'error': 'O arquivo é muito grande. O tamanho máximo permitido é 1MB.'}, status=status.HTTP_400_BAD_REQUEST)
            
            uploaded_file = request.FILES['file']
            content = uploaded_file.read().decode('utf-8')

            # Verificar se a pasta 'java_files' já existe
            if not os.path.exists(settings.MEDIA_ROOT):
                # Se não existir, criar a pasta
                os.makedirs(settings.MEDIA_ROOT)
            # Salvar o arquivo no diretório 'java_files'
            file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            with open(file_path, 'wb') as file:
                file.write(uploaded_file.read())
                
            # Converte a resposta em formato CSV
            response_data = data_response(content, uploaded_file)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

            # Cria o objeto de escrita CSV e escreve os dados
            writer = csv.writer(response)
            writer.writerows(response_data)
            
            return response
        