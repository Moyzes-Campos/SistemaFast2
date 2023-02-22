from django.db import models
from stdimage import StdImageField


class Patrocinador(models.Model):
    nome = models.CharField(max_length=50)
    logo = StdImageField('foto', upload_to='integrantes', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Patrocinador'
        verbose_name_plural = 'Patrocinadores'
