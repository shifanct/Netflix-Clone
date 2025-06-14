from . import views
from django.urls import path

urlpatterns = [
    path('signup',views.signin, name = 'signin'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('',views.home,name = 'home')

]