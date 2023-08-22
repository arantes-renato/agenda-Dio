from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    título = models.CharField(max_length=100)
    descrição = models.TextField(blank=True, null=True)
    data_evento = models.DateField(verbose_name='Data do Evento')
    data_criação = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    local = models.CharField(max_length=100, blank=True, null=True)
    usuário = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.título
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y')
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%d')
