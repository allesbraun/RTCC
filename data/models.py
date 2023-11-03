
import os

from django.db import models


class Code(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=100, blank = True) 
    
    def save(self, *args, **kwargs):
        # Se o título ainda não foi definido, gera-o com base no nome do arquivo
        if not self.title:
            file_name = os.path.basename(self.file.name)
            self.title = os.path.splitext(file_name)[0]
        super(Code, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    


