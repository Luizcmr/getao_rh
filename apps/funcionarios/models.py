from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

# Criando model funcionario.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do funcionário")
    user = models.OneToOneField (User, on_delete=models.PROTECT, null=True )
    id_departamento = models.ManyToManyField(Departamento)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome