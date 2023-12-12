from django.shortcuts import render, HttpResponse


html_base = """
<h1>Mi web personaL</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de</a></li>
    <li><a href="/contact/">Contacto</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
</ul>
"""

# Create your views here.
def home(request):
    html_response = "<h2>Portada</h2>"
    return HttpResponse(html_base + html_response + """
        <p>Esto es la portada </p>
    """)

def about(request):
    html_response = "<h2>Acerca de</h2><p>Me llamo Diego y soy programador</p>"
    return HttpResponse(html_base + html_response)

def contact(request):
    html_response = "<h2>Contacto</h2><p>Escribeme a diegogaraycullas@gmail.com</p>"
    return HttpResponse(html_base + html_response)

def portfolio(request):
    html_response = "<h2>Portfolio</h2><p>Mis proyectos</p>"
    return HttpResponse(html_base + html_response)