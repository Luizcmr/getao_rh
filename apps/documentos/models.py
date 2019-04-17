from django.db import models

# Criando model documentos.
class Documento(models.Model):
    descricao = models.CharField(max_length=50, help_text="Descrição do documento")

    def __str__(self):
        return self.descricao