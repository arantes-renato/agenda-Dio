from django.contrib import admin
from core.models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'título', 'data_evento', 'data_criação', )
    list_filter = ('usuário', 'data_evento',)

admin.site.register(Evento, EventoAdmin)
