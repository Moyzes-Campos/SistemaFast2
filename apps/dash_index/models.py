from django.contrib.auth.models import User
from django.db import models
from stdimage import StdImageField

areas = (
    ('Aerodinâmica', 'Aerodinâmica'),
    ('Direção', 'Direção e Suspenção'),
    ('Elétrica', 'Elétrica'),
    ('Estrutura', 'Estrutura'),
    ('Freio e Ergonomia', 'Freio e Ergonomia'),
    ('Powewtrain', 'Powewtrain'),
    ('Comercial', 'Comercial'),
    ('Financeiro', 'Financeiro'),
    ('Gestão', 'Gestão de Pessoas'),
    ('Marketing', 'Marketing'),
    ('NA', 'Nenhuma'),
)

situacao = (
    ('AF', 'A fazer'),
    ('FA', 'Fazendo'),
    ('FE', 'Feito'),
)

funcao_choices = (
    ('Cordenador', 'Cordenador'),
    ('Assesor', 'Assesor'),
    ('Conselheiro', 'Conselheiro'),
    ('Capitão', 'Capitão(ã)'),
    ('Vice Capitão', 'Vice Capitão(ã)'),
    ('Diretor de Projetos', 'Diretor(a) de Projetos'),
    ('Diretor Administrativo', 'Diretor(a) Administrativo'),
)


class Atividade(models.Model):
    area = models.CharField(max_length=100, choices=areas)
    situacao = models.CharField(max_length=100, choices=situacao)
    descricao = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.descricao


class ObjetivosArea(models.Model):

    titulo = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    area = models.CharField(max_length=50, choices=areas, default='Nenhuma')

    class Meta:
        verbose_name = 'Objetivo'
        verbose_name_plural = 'Objetivos'


class FluxodeCX(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Fluxo de Caixa'
        verbose_name_plural = 'Fluxo de Caixa'

    def __str__(self):
        return self.data


class Integrantes(models.Model):
    nome = models.CharField(max_length=50)
    funcao = models.CharField(max_length=50, choices=funcao_choices)
    area = models.CharField(max_length=50, choices=areas)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    foto = StdImageField('foto', upload_to='integrantes', blank=True, null=True)

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'

    def __str__(self):
        return self.nome


class Lembrete(models.Model):
    lemb = models.CharField('lembrete', max_length=80)

    def __str__(self):
        return self.lemb

