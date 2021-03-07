from django.urls import path
from core.homepage import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'Index'),
]