from django.urls import path

from . import views

app_name = 'studentrisk'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('<str:study>/<str:cohort>/<str:semester>', views.index, name='index')
]
