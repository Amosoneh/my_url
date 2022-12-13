from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'url'
urlpatterns = [
                  path('', views.index, name='index'),
                  path('create/', views.urlShort, name='shorten-url'),
                  path('<str:pk>', views.urlRedirect, name='redirected-url')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
