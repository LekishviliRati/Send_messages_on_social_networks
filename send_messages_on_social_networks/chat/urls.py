from django.urls import path

from chat import views

urlpatterns = [
    path('', views.list_message, name="list_message"),
]
