from django.urls import path
from . import views
from .views import accounts, daftarclient, tambahclient, detailclient, deleteClient, ubahpassword, tambahuser, ubahpassuser

urlpatterns = [
    path('', accounts, name='accounts'),
    path('daftarclient/', views.daftarclient, name='daftarclient'),
    path('daftarclient/tambahuser/', views.tambahuser, name='tambahuser'),
    path('daftarclient/tambahclient/', views.tambahclient, name='tambahclient'),
    path('daftarclient/detailclient/<str:pk>/', views.detailclient, name='detailclient'),
    path('daftarclient/<str:pk>/delete', views.deleteClient, name='deleteclient'),

    path('ubahpassword/', views.ubahpassword, name='ubahpassword'),
    path('ubahpassuser/', views.ubahpassuser, name='ubahpassuser'),
]
