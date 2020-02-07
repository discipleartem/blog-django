# blog-django

########### lesson 1 ###########

virtualenv --python=python3.7 venv
source venv/bin/activate
pip install django
mkdir app

создаем новый проект
django-admin startproject blogengine

весь функционал в django разбит на модули, которые "подключаються" в проект
для этого переходим в папку с  manage.py и создаем новый "модуль"

python manage.py startapp blog



########### lesson 2 ###########

для запуска сервера переходим в папку с  manage.py

./manage.py runserver 5000

Применение миграций в папку с  manage.py
./manage.py migrate

подключаем же приложения в основной папке проекта в файле settings.py
в разделе INSTALLED_APPS = [
...
'blog'
]

маршрутизация происходит в основной папке проекта в файле в файле urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('blog/', hello)
    имя шаблона , имя функции в файле views.py
]

можно передать путь на файл, в котором указаны свои маршруты (чтобы не загромождать файл и логически 
разделить функционал блога от постов и тегов например)

для этого нужно подключить модуль include

from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
    папка blogengine --> папка blog --> файл urls.py
]


####################### blog --> файл urls.py #######################

from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list)
]


####################### / blog --> файл urls.py #######################


########### lesson 3 ###########
