from django.db import models

# Criando model departamento.
class Departamento(models.Model):
    nome = models.CharField(max_length=50, help_text="Nome do departamento")

    def __str__(self):
        return self.nome