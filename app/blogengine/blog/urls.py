from django.urls import path

from .views import *

urlpatterns = [
    #для пути blog/
    #для использования относительного пути в ссылках используем атрибут "name="
    path('', posts_list, name='post_list_url'),
    #то, что в '<>' - именнованая группа символов. Указание типа - 'str:'
    #обязательно ставим '/' (>/')
    path('post/<str:slug>/', post_detail, name='post_detail_url')

]