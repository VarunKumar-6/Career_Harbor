from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='career'),
    path('login',views.login_views,name='login'),
]    