from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"
    #* asignando nombre publico a la app
    verbose_name = "Portafolio"
