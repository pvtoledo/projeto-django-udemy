from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.criar_conta, name='criar_conta')
]

htmx_urlpatterns = [
    path('criar_conta/htmx_valida_username', views.htmx_valida_username, name='htmx_valida_username'),
    path('criar_conta/htmx_valida_senha', views.htmx_valida_senha, name='htmx_valida_senha'),
    path('criar_conta/htmx_valida_email', views.htmx_valida_email, name='htmx_valida_email'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += htmx_urlpatterns