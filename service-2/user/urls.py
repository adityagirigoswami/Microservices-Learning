from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListandCreate.as_view()),
    path('<uuid:pk>/', views.UserRetrieve.as_view()),
]