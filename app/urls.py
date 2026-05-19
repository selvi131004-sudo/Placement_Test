from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),

    path('register/', views.register),

    path('login/', views.login),

    path('dashboard/', views.dashboard),

    path('test/<str:section>/', views.test),

    path('result/', views.result),

    path('retry/<str:section>/',
    views.retry_test),

]