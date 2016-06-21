from django.db import models

# Create your models here.

class Participantes(models.Model):
    nome = models.CharField("Nome",max_length=255)
    descricao = models.CharField("Descrição",max_length=100)

class AcompanhamentoAtividades(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    data = models.DateField("Data", auto_now_add=True)
    atividades = models.ForeignKey(Atividades,on_delete=models.PROTECT,verbose_name="Atividades")

class Atividades(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    dataInicio = models.DateField("Data Inicio",auto_now_add=True)
    dataTermino = models.DateField("Data Término")
    custos = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="Custos")
    projetos = models.ForeignKey(Projetos, on_delete=models.PROTECT,verbose_name="Projetos")

class Projetos(models.Model):
    titulo = models.CharField("Título",max_length=100)
    dataInicio = models.DateField("Data Inicio", auto_now_add=True)
    dataTermino = models.DateField("Data Término")
    justificativa = models.CharField("Justificativa", max_length=500)
    metodologia = models.CharField("Metodologia", max_length=800)
    resultados = models.CharField("Resultados Esperados", max_length=500)
    participantes = models.ManyToManyField(Participantes)


