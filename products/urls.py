from django.urls import path
from . import views
# from categories.views import bycategory

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:product_id>', views.product, name='product'),
    # path('<int:categori_id>', bycategory, name='bycategory'),
    path('search', views.search, name='search'),
]
