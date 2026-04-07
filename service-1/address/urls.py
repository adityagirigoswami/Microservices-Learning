from django.urls import path

from . import views

urlpatterns = [
    path('users/<uuid:user_id>/', views.AddressListandCreate.as_view(), name='address-list-create'),
]