from django.urls import path
from django.contrib.auth.decorators import login_required


from chat import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('messages/', login_required(views.list_message), name="list_message"),
]
