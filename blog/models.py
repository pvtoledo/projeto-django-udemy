from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = RichTextUploadingField()
    data_publicacao = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.titulo
