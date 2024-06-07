from django.urls import path
from . import views

urlpatterns = [
    path('deposito/<int:conta_filha_id>/', views.realizar_deposito, name='realizar_deposito'),
]
