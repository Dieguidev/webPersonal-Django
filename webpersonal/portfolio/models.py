from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    url_filed = models.URLField(verbose_name="URL", null=True, blank=True)

    #* añadir metadatos extendidos
    class Meta:
        # asignando nombre publico a la app
        verbose_name = "proyecto"
        # asignando nombre publico en plural a la app
        verbose_name_plural = "proyectos"
        # ordenando por fecha de creacion
        ordering = ["-created"]
    
    #* metodo para mostrar el titulo en el admin
    # redefiniendo el metodo __str__ 
    def __str__(self):
        return self.title
    