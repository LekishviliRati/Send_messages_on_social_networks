from django.urls import path

from chat import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('messages/', views.list_message, name="list_message"),
]
