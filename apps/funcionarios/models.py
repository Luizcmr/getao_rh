from django.db import models

# Criando model funcionario.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do funcionário")

    def __str__(self):
        return self.nome