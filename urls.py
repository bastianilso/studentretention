from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'studentrisk'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('<str:study>/<str:cohort>/<str:semester>', views.index, name='index'),
    url(r'^ajax/update_checkbox/$', views.update_checkbox, name='update_checkbox'),
    url(r'^ajax/update_comment/$', views.update_comment, name='update_comment')
]
