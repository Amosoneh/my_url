from django.urls import path
from . import views
app_name = 'url'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.urlShort, name='shorten-url'),
    path('<str:pk>', views.urlRedirect, name='redirected-url')
]