from django.contrib import admin
from .models import Project

# Register your models here.


#*Configuracion del panel de administracion
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



#Registrando los modelos
admin.site.register(Project, ProjectAdmin)
