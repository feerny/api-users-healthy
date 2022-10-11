from django.urls import path
from ApisUsers import views

urlpatterns = [
    path('api/users', views.User_lista),
    path('api/users/<int:pk>',views.User_detalle)
]