from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('edit_status/<str:pk>/', views.edit_status, name='edit_status'),
    path('det_penanganan/<str:pk>/', views.det_penanganan, name='det_penanganan'),
    path('pengsel/', views.pengsel, name='pengsel'),
    path('pengsel/<str:pk>/delete', views.deletePeng, name='deletePeng'),
    path('akun/', views.akun, name='akun'),

    path('user/', views.user_page, name='user_page'),
]
