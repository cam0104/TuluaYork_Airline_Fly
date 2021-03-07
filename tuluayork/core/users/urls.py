from django.urls import path
from core.users import views

urlpatterns = [
    path('login', views.singinView.as_view(), name = 'Login'),
    path('signup/', views.signup, name='Signup'),
    path('logout', views.LogoutView.as_view(), name = 'Logout')

]