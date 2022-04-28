from django.urls import path
from .views import product_list, product_detail, product_chages

urlpatterns = [
    path('<int:spk>/categories/<int:cpk>/', product_list),
    path('<int:spk>/categories/<int:cpk>/<int:pk>/', product_detail),
    path('product/<int:pk>/', product_chages),
]
