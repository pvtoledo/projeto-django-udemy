from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.carrega_quiz, name='carrega_quiz'),
    path('quiz/resposta/', views.carrega_resposta, name='resposta'),
]

htmx_urlpatterns = [

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += htmx_urlpatterns
