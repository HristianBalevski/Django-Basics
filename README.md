# Plans

**01.Internet and HTTP**

 1.Какво е интернет
 
 - Една голяма мрежа от устройства
 - Пример:
   - Ако ние разкачим нашия рутер и го свържем с телефона и лаптопа ни, това е някаква (мини) мрежа от 2 устройства.
   - Ако аз пусна приложение на някакъв порт на лаптопа ми, ще мога да го достъпя на телефона.
   - Ако след това свържем рутера с интернет, то това ще бъде свързване на нашата (мини) мрежа с всички останали мини мрежа, в една голяма мрежа.
    
 - Заражда се като научноизследователска дейност през 1969.

 - Начините, по които се свързваме са чрез:
   - Оптични кабели
   - Медни кабели
   - Телефонни клетки
   - Сателити

- Команди за всички индивидуални мрежови интерфейси на нашата машина
  - Mac/Linux:
  ```
    ifconfig
  ```

  - Windows:
  ```
    ipconfig /all
  ```

  - Физически интерфейси: en0, en1, en2, en3, en4, en5, en6
  - Виртуални интерфейси: lo0, bridge0, utun0, utun1, utun2, utun3, awdl0

2.Request/Response - Client/Server

- Ние искаме някакъв ресурс и ако имаме достъп го взимаме
- Клиента е всяко приложение, което може да достъпи сървър
- Сървъра е машината, която може да предоставя ресурси
```
  curl https://softuni.bg/
```

3.Network Protocol

  - Стандарт, чрез който могат да комуникират 2 устройства
  - Правилата, които трябва да бъдат изпълнени, така че съвъра да може да разбере какво иска клиента, и когато върне резултат клиента да може да го разбере.
  - Често използвани протоколи:
    - HTTP:
      - Използван за зареждане на уеб страници, всяка заявка и отговор са независими.
    - TCP:
      - Гарантира, че данните се предават надеждно и в правилния ред, осигурява връзка преди предаване.
    - FTP:
      - Протокол за прехвърляне на файлове, работи в клиент-сървър модел и поддържа различни режими на трансфер.
      - Често се използва за теглене на резервно копие на база данни, главно поради големия обем на данните.
    - SSH:
      - Осигурява сигурен отдалечен достъп до мрежови устройства, криптирайки комуникацията.
    - SMTP:
      - Използваме, за да изпращаме имейли към имейл провайдъри.
    - IP:
      - Протокол за адресиране и маршрутизация на данни в мрежи, който осигурява изпращането и получаването на пакети между устройства.
 
 4.Пакети
 
   - Когато сървъра и клиента си обменят данни, те ги обменят на пакети
   - Ако имаме твърде голям обем от данни те ще бъдат разделени на малки части (пакети).
   - Клиента ще раздроби данните на пакети, когато ги подава на сървъра. Той от своя страна ще ги сглоби и обратното.
   - Протокола е начина, по който, сървъра и клиента разбират как да обработват пакетите.

5.IP адрес

  - Уникален идентификатор в локалната мрежа
  - В една мрежа всички IP-та трябва да са уникални
  - Поради тази причина свързвайки се с с друга мрежа, можем да имаме друго IP в нея.
  - Ако ние сме свързали няколко устройства в една мрежа, те могат да излизат под едно IP за външия свят, но вътре в самата мрежа те имат различни IP адреси
  - [What is my IP?](https://whatismyipaddress.com/)

6.IPv4 vs IPv6

  - v4 позволява създаването на 4.3 милиарда уникални адреса
    - 32-битови адреси
    - Пример:
      - **192.168.14.20**
      - **192.168** е мрежова част
      - **14** е подмрежа (нашата мрежа)
      - **20** е нашето устройство в мрежата
  - v6 позволява създаването на 3.4×10^38 уникални адреса
    - 128-битови адреси

7.DNS - Domain Name System

  - Грижи се да можем да достъпваме сайтове през домейн(име), а не през IP
  - IP-то се сменя, затова не можем да караме потребителте да го помнят

8.HTTP

  - Винаги получаваме резултат
  - Протокола на интернет
  - HTTP1/HTTP2 използват TCP/IP под себе си. HTTP3 използва QUIC протокол.
  - HTTP verb:
    - CREATE
    - POST
    - PUT
    - DELETE
    - ...
  - [Status Code](https://http.cat/)

9.URL (Uniform Resource Locator)
  
  - Подобно на адресите в реалния свят имаме: държава, град, квартал...
  - [http://localhost:8080/demo/html?id=26&lang=en#lecture](http://localhost:8080/demo/html?id=26&lang=en#lecture)
  - http - протокол
  - localhost - host, domain
  - 8080 - порт
  - /demo/html - път
  - ?id=26&lang=en - query string
  - #lecture - fragment
  - [https://softuni.bg:443](https://softuni.bg:443) - можем да си спестим порта, защото https се заржда на 443 по подразбиране.
  - Можем да имаме url-и на кирилица

10.MIME (Multi-purpose Internet Mail Extensions)

  - Обяснява типа на данните, които се изпращат и получават

---

**02.Django Introduction**

1.Framework - Работна рамка

  - Следваме определени правила и структури.
  - Получаваме готови функции

2.MVT Pattern

  - **Model View Template**

3.Структура на Django проект

  - manage.py - entry point-a за работа с Django, с него изпълняваме command-line операции
  - projectFolder
    - settings.py - съдържа настроките на приложението
    - urls.py - място където дефинираме url-и, които да са достъпни от потребителя
    - asgi.py - setup за асинхронни заявки
    - wsgi.py - setup за синхронни заявки  
 - djangoApp - всеки app се грижи за отделна част от нашия проект

4.Creation of a django app
  - Move app to project directory (Optional)
  - Create ```urls.py``` file
  - Register the djagoApp in ```settings.py```
  - Register the urls in the project
  - ```   python manage.py runserver```

5.Databases

  - За Postgres инсталираме psycopg2
  - Конфигурираме в ```setting.py```
  - Създаваме база
  - Създаваме модели в ```models.py```
  - ```makemigrations```
  - ```migrate```

6.Views

  - Съдържат главната бизнес логика
  - Function Based View (FBV)
  - Трябват ни:
    - Функция, която има един или повече параметри и връща отрговор
      
     ```
     def index(request):
           return HttpResponse("Hello world")

     ```
    
    ```
      HttpResponse("Hello world", headers={
       "Content-Type": "application/json",
    })

7.urls

  - Създаваме си променлива с име ```urlpatterns``` в app/urls.py
  - В нея задаваме на какъв път, какво view да се изпълни
    ```
       from .views import index

       urlpatterns = (
          path('home/', index),
       )

 - Добавяме си app/urls в project/urls.py
   ```
       urlpatterns = (  
       path('admin/', admin.site.urls),
       path('', include('project_name.app_name.urls')),  
    )

8.Admin Panel

  - Django пакет
  - Започнат като third-party пакет и в последствие добавен като официален пакет
  - /admin/ - за да достъпим админ панела
  - ```createsuperuser```
  - admin.py - регистрираме моделите, които искаме да могат да се манипулират в админа

9.Django Template Language (DTL)

  - Като динамичен HTML
  - Имаме цикли, ифове
  - Можем да рендерираме наши стойности
  - ```{{ }}``` - интерполация
  - ```{% %}``` - template tags

---

## 03. Urls and Views

1.Какво са url-ите в Django?

  - Всеки url преставлява път, на който зареждаме дадено view
  - Django ги проверява последователно за съвпадение
    ```
      urlpatterns = [
        path('index/', index_view),
        path('index/', index_view_2)  # никога няма да видим index_view_2
      ]
  - В основните urls на проекта ни, трябва да включим тези от всяко наше приложение
  - Можем да сложим общ prefix, който да седи пред всеки url на даден app
    ```
     urlpatterns = [
       path('admin/', admin.site.urls),
       path('departments/', include('departments.urls')),
     ]
  - include може да приема списък от paths

2.Динамични url-и

  - Понякога искаме в url-a да има динамична стойност (променяща се, примерно id)
    ```
        path('index/<int:pk> ', index_view),
  - Типове динамични url-и
    - str
    - int
    - slug - string, който не може да има интервали и non-Ascii символи
    - path - "/some/path" - не бихме имали съвпадение в str, защото Django вижда това като отделни пътища
    - uuid
 - re_path
   - Винаги пишем в raw стринг(стринг, който няма escapes)
   - В django 2 всеки път е бил с регулярни изрази
     ```
         re_path(r'^article/(?P<year>[0-9]{4})/', view)
         # matches year and saves it in a variable year

3.Views

  - Function Based Views
    - Приемат http заявка и връщат http отговор(или негов наследник)
    - Освен заявката, могат да получават и други параметри заложени в url-a

4.Response types

  - HttpResponse
    - Обект, който се грижи за това да се сериализира нашият отговор (да се разбие на пакети и тн.)
    - Можем да му подаваме content (съдържание)
    - Можем да му подадем status_code
        ```
           return HttpResponse(content="Hi my name is", status=201)
        
 - JsonResponse
   ```
      content = json.dumps({
         "name": "Dido",
         "age": 20
    })
    
    return HttpResponse(content=content, content_type="application/json")
    # or
    return JsonResponse(content,)

5.Django Shortcuts

  - **render**
    - Рендерира контекст в html template
      ```
         return render(request, 'core/index.html', context)  # context is optional

  - **redirect**
    - Пренасочва ни към друг url
    - Може да бъде permanent
      - Когато искаме винаги от тази страница да се пренасочва към друга
  ```
   redirect('https://softuni.bg')  # използваме абсолютен url. защото редиректваме към друго приложение
   redirect('my_view_name', pk=10)  # използваме име на view-то, за по-добра абстракция
  ```

 - **resolve_url**
   - Използва url resolver-a на django, за да намери url отговарящ на view или model (ако в модела има get_absolute_url)
 - get_object_or_404()
 - get_list_or_404()
```
article =  get_object_or_404(Article, pk=article_id)
```
- **reverse**
  - Получава име на url, търси в регистрираните имена и връща url-а с това име
- **reverse_lazy**
  - Използва се за конфигурация
  - Зарежда url-а, когато той съществува
```
   # settings.py
   LOGIN_URL = reverse('index') # throws an error
   LOGIN_URL = reverse_lazy('index') # throws an error
```

6.Django Errors

  - raise Http404
  - return HttpResponseNotFound
  - Постигат един и същ резултат
  - Можем да персонализираме 404 страницата като направум темплейт с име ```404.html```

---

## 04.Template Basics

1.Django Template Language(DTL)

  - Използваме, за да рендерираме информацията от view-тата.
  - Позволява ни да пишем html, който в зависимост от данните да бъде различен.
  - Единствените езици, които Django поддържа out of the box DTL и Jinja2.
  - Има други алтернативи като ```Jinja2```
  - Mожем да рендредираме в html, txt, xml и тн.
  - С него правим Sever Side Rendering(SSR).
  - 
  - Настройките по подразбиране за DTL можем да намерим в ```settings.py```

    ```
       TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [BASE_DIR / 'templates']
              ,
              'APP_DIRS': True,
              'OPTIONS': {
                  'context_processors': [
                      'django.template.context_processors.debug',
                      'django.template.context_processors.request',
                      'django.contrib.auth.context_processors.auth',
                      'django.contrib.messages.context_processors.messages',
                  ],
              },
          },
      ]
    ```

2.Променливи

  - Попълваме от контекста в ```{{ }}```
  - Имената на променливите трябва да бъдат snake_case само букви и цифри
  - Достъпване на методи, пропъртита и индекси става чрез .
  - {{ my_list.1 }}, {{ person.full_name }}, {{ my_object.items }}

```
  context = {
    "person": {
        "name": "Dido",
        "age": 20,
    },
    "person2": Person(name="Ivan", age=21),
}
```

3.Филтри

  - Използваме, за да преобразуваме нашите данни в темплейта.
  - Използваме със символа ```|```
  - Някои филтри имат параметри като тях подаваме с ```:```
  - Някои built-in филтри
    - truncatechars:number - маха последните number chars и ги заменя с ...
    - truncatewords:number
    - join:seprarator - същото като ''.join(separator) в Python.
    - date:format - форматира датата по желан от нас начин.
    - default:value - какво да се покаже при falsy стойност.
    - add:value - добавя към съществуваща стойност.
    - capfirst - прави първата буква главна.
  - Линк към всички филтри в Django -> [Django Tmplate Filters](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/)

4.Тагове

  - Цикли, проверки и други built-in действия.
  - Таговете, които рендерират html имат затварящи тагове, защото html не зачита whitespace.
  - url tag - позволява ни да не използваме hardcoded urls
  - csrf_token - генерира произволен стринг на бак енд-а, рендерира го във фронт-енд-а и го сравнява, когато направим заявка, също запазва cookie.
```
1.Условни оператори (if, elif, else):

{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% elif user.is_staff %}
    <p>Welcome, staff member!</p>
{% else %}
    <p>Welcome, guest! Please log in.</p>
{% endif %}

Това е коректен пример за условни проверки в Django шаблони. Проверките се извършват в съответствие с логическите условия за обекта user.

2.Проверка за празен URL:

{% if url %}
    <a href="{{ url }}">Visit this link</a>
{% else %}
    <p>No URL provided.</p>
{% endif %}

Тук се проверява дали променливата url съдържа стойност и се създава линк към нея. Ако не е предоставен URL, се показва съобщение.

3.Пример с cycle:

<ul>
    {% for item in items %}
        <li class="{% cycle 'row1' 'row2' %}">{{ item }}</li>
    {% endfor %}
</ul>

Функцията cycle се използва за редуване на CSS класове (в случая 'row1' и 'row2') при всяка итерация на елементите в списъка items. Това е удобен начин за създаване на редуващи се стилове.

4.Пример с lorem:

<p>{% lorem 3 p %}</p>

Този шаблонен таг генерира три абзаца с фиктивен текст ("Lorem ipsum"). Може да се използва за запълване на място по време на разработка.
```

5.Static Files

  - Ресурси, които се зареждат за всеки потребител.
  - Снимки, видеа, икони.
  - SetUp
```
   STATIC_URL = "static/"  # BASE URL - място от където достъпваме статичните ресурси
   STATICFILESDIRS = (
        BASE_DIR / 'staticfiles',  # create a folder staticfiles, usually on the level of manage. py
   )  # The place on the filesystem where staticfiles are
```
  - https://localhost:8000/static/file.css - достъпваме файл
  - {% static 'PATH/TO/FILE' %} - static тага, заменя STATIC_URL, по този начин, ако той бъде сменен, няма да се налага да го променяме навсякъде.
  - В началото на темплейта добавяме ```{% load static %}```, което зарежда статичните файлове.
  - При деплоймънт, django не предоставя статичните файлове, защото пускаме приложението си с gunicorn, който също не се грижи за статичните файлове.
  - Тогава ни трябва още една настройка.
```   STATIC_ROOT = BASE_DIR / 'staticfiles_compiled'```
  - Изпълняваме командата ```collectstatic```, която взима статичните файлове от всички наши и чужди приложения и ги слага на STATIC_ROOT пътя.

---
    
