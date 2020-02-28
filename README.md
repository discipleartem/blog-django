# blog-django

########### lesson 1 ###########
``` 
virtualenv --python=python3.7 venv
source venv/bin/activate
pip install django
mkdir app
``` 

создаем новый проект
``` django-admin startproject blogengine``` 

весь функционал в django разбит на модули, которые "подключаються" в проект
для этого переходим в папку с  manage.py и создаем новый "модуль"

``` python manage.py startapp blog``` 



########### lesson 2 ###########

для запуска сервера переходим в папку с  manage.py

``` ./manage.py runserver 5000``` 

Применение миграций в папку с  manage.py
``` ./manage.py migrate``` 

подключаем же приложения в основной папке проекта в файле settings.py
в разделе 

``` 
INSTALLED_APPS = [
. . .
'blog'
]
``` 

маршрутизация происходит в основной папке проекта в файле в файле ``` urls.py``` 

``` 
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('blog/', hello)
    имя шаблона , имя функции в файле views.py
]
``` 

можно передать путь на файл, в котором указаны свои маршруты (чтобы не загромождать файл и логически 
разделить функционал блога от постов и тегов например)

для этого нужно подключить модуль include

``` from django.urls import include ``` 

``` 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
    папка blogengine --> папка blog --> файл urls.py
]
``` 

####################### blog --> файл urls.py #######################
``` 
from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list)
]
``` 

####################### / blog --> файл urls.py #######################


########### lesson 3 templates ###########

Подключение шаблонов в blogengine --> settings.py в ``` 'DIRS': [],``` 

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
```

########### lesson 4 model ###########
после заполнения model.py в виртуальном окружении выполняем миграции

в папке c файлом ```manage.py```
```./manage.py makemigrations```
схема миграции в папке migrations

а после применяем миграцию
```./manage.py migrate```

переход в консоль django 
```./manage.py shell```

```
from blog.models import Post
p1 = Post(title = 'New Post', slug = 'new-slug', body = 'new post body')
p.save()
p.id
dir(p)

p2 = Post.objects.create(title = 'new post2', slug = 'new-post2', body = 'body')
Post.objects.all()
post = Post.objects.get(slug = 'new-slug')

# регистро-независемый поиск 
post = Post.objects.get(slug__iexact = 'New-slug')

p3 = Post.objects.create(title = 'new post3', slug = 'new-post3', body = 'body of post 3')

p4 = Post.objects.create(title = 'new post4', slug = 'new-post-4', body = 'body of post 4')

p5 = Post.objects.create(title = 'new post5', slug = 'new-post-5', body = 'my 5th post')

```
########### lesson 5 model Tag ###########





https://youtu.be/C_K12QRDE8k