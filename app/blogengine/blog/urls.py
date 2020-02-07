from django.urls import path

from .views import *

urlpatterns = [
    #для пути blog/
    path('', posts_list)
]