from django.urls import path

from .views import index, recipe_list, recipe1, recipe2
urlpatterns = [
    path('', index, name='index'),
    path('list/', recipe_list, name='recipe_list'),
    path('1/', recipe1, name='list'),
    path('2/', recipe2, name='list'),
]

app_name = 'ledger'