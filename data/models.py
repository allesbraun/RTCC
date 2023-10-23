import csv
import json
import os

from django.conf import settings
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from data.data_response import data_response


class Code(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=100, blank = True)  # mudar para blank=True em vez de default='main'?
    # code_description = models.CharField(max_length=500, default = 'A java code.')

    def save(self, *args, **kwargs):
        # Se o título ainda não foi definido, gera-o com base no nome do arquivo
        if self.title == '':
            file_name = os.path.basename(self.file.name)
            self.title = os.path.splitext(file_name)[0]
        super(Code, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    


