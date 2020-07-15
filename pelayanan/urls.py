from django.urls import path
from . import views
from .views import pelayanan, editstatus, tambahpelayanan, detaildaftar

urlpatterns = [
    path('', pelayanan, name='pelayanan'),
    path('tambahpelayanan', views.tambahpelayanan, name='tambahpelayanan'),
    path('editstatus/<str:pk>/', views.editstatus, name='editstatus'),
    path('detailpelayanan/<str:pk>/', views.detailpelayanan, name='detailpelayanan'),
    path('detaildaftar/<str:pk>/', views.detaildaftar, name='detaildaftar'),
    path('<str:pk>/delete', views.deletepelayanan, name='deletepelayanan'),
]
