from django.urls import path
# from products.views import product
from .views import bycategory, index
urlpatterns = [
    path('', index, name='categories'),
    path('<int:categori_id>', bycategory, name='bycategory'),
]
