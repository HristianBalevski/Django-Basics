[Click here for more infromation about the course](https://softuni.bg/trainings/4713/django-basics-september-2024)

![Django Basics](https://github.com/user-attachments/assets/5be0e970-454b-4619-85a4-cdc4df63cbbd)

## 01.Internet and HTTP

 **1.Какво е интернет**
 
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

**2.Request/Response - Client/Server**

- Ние искаме някакъв ресурс и ако имаме достъп го взимаме
- Клиента е всяко приложение, което може да достъпи сървър
- Сървъра е машината, която може да предоставя ресурси
```
  curl https://softuni.bg/
```

**3.Network Protocol**

  - Стандарт, чрез който могат да комуникират 2 устройства
  - Правилата, които трябва да бъдат изпълнени, така че сървъра да може да разбере какво иска клиента, и когато върне резултат клиента да може да го разбере.
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
 
 **4.Пакети**
 
   - Когато сървъра и клиента си обменят данни, те ги обменят на пакети
   - Ако имаме твърде голям обем от данни те ще бъдат разделени на малки части (пакети).
   - Клиента ще раздроби данните на пакети, когато ги подава на сървъра. Той от своя страна ще ги сглоби и обратното.
   - Протокола е начина, по който, сървъра и клиента разбират как да обработват пакетите.

**5.IP адрес**

  - Уникален идентификатор в локалната мрежа
  - В една мрежа всички IP-та трябва да са уникални
  - Поради тази причина свързвайки се с с друга мрежа, можем да имаме друго IP в нея.
  - Ако ние сме свързали няколко устройства в една мрежа, те могат да излизат под едно IP за външия свят, но вътре в самата мрежа те имат различни IP адреси
  - [What is my IP?](https://whatismyipaddress.com/)

**6.IPv4 vs IPv6**

  - v4 позволява създаването на 4.3 милиарда уникални адреса
    - 32-битови адреси
    - Пример:
      - **192.168.14.20**
      - **192.168** е мрежова част
      - **14** е подмрежа (нашата мрежа)
      - **20** е нашето устройство в мрежата
  - v6 позволява създаването на 3.4×10^38 уникални адреса
    - 128-битови адреси

**7.DNS - Domain Name System**

  - Грижи се да можем да достъпваме сайтове през домейн(име), а не през IP
  - IP-то се сменя, затова не можем да караме потребителте да го помнят

**8.HTTP**

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

**9.URL (Uniform Resource Locator)**
  
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

**10.MIME (Multi-purpose Internet Mail Extensions)**

  - Обяснява типа на данните, които се изпращат и получават

---

## 02.Django Introduction

**1.Framework - Работна рамка**

  - Следваме определени правила и структури.
  - Получаваме готови функции

**2.MVT Pattern**

  - **Model View Template**

**3.Структура на Django проект**

  - manage.py - entry point-a за работа с Django, с него изпълняваме command-line операции
  - projectFolder
    - settings.py - съдържа настроките на приложението
    - urls.py - място където дефинираме url-и, които да са достъпни от потребителя
    - asgi.py - setup за асинхронни заявки
    - wsgi.py - setup за синхронни заявки  
 - djangoApp - всеки app се грижи за отделна част от нашия проект

**4.Creation of a django app**

  - Move app to project directory (Optional)
  - Create ```urls.py``` file
  - Register the djagoApp in ```settings.py```
  - Register the urls in the project
  - ```   python manage.py runserver```

**5.Databases**

  - За Postgres инсталираме psycopg2
  - Конфигурираме в ```setting.py```
  - Създаваме база
  - Създаваме модели в ```models.py```
  - ```makemigrations```
  - ```migrate```

**6.Views**

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

**7.urls**

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

**8.Admin Panel**

  - Django пакет
  - Започнат като third-party пакет и в последствие добавен като официален пакет
  - /admin/ - за да достъпим админ панела
  - ```createsuperuser```
  - admin.py - регистрираме моделите, които искаме да могат да се манипулират в админа

**9.Django Template Language (DTL)**

  - Като динамичен HTML
  - Имаме цикли, ифове
  - Можем да рендерираме наши стойности
  - ```{{ }}``` - интерполация
  - ```{% %}``` - template tags

---

## 03. Urls and Views

**1.Какво са url-ите в Django?**

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

**2.Динамични url-и**

  - Понякога искаме в url-a да има динамична стойност (променяща се, примерно id)
    ```
        path('index/<int:pk> ', index_view),
  - Типове динамични url-и
    - str
    - int
    - slug - string, който не може да има интервали и non-Ascii символи
    - path - "/some/path" - не бихме имали съвпадение в str, защото Django вижда това като отделни пътища
    - [UUID (Universally Unique Identifier)](https://www.uuidgenerator.net/) е 128-битов уникален идентификатор, използван за обозначаване на обекти по уникален начин в рамките на дадена система.
 - re_path
   - Винаги пишем в raw стринг(стринг, който няма escapes)
   - В django 2 всеки път е бил с регулярни изрази
     ```
         re_path(r'^article/(?P<year>[0-9]{4})/', view)
         # matches year and saves it in a variable year

**3.Views**

  - Function Based Views
    - Приемат http заявка и връщат http отговор(или негов наследник)
    - Освен заявката, могат да получават и други параметри заложени в url-a

**4.Response types**

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
   ```

**5.Django Shortcuts**

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

**6.Django Errors**

  - raise Http404
  - return HttpResponseNotFound
  - Постигат един и същ резултат
  - Можем да персонализираме 404 страницата като направим темплейт с име ```404.html```

**7.Creating Slug**

Добавянето на ```slug``` в проектите е добра практика, особено ако имаме модели с полета като ```name```, които трябва да се използват в URL адреси. Slug полетата са по-четливи за потребителя и по-оптимизирани за SEO, отколкото използването на идентификатори (IDs) в URL.
  
- **Използване на SlugField**: По-добре е да използвамe ```SlugField``` вместо ```CharField```, който е специално създаден за такива случаи. Той автоматично ограничава символите до валидни URL символи.
- **Автоматично генериране на уникални "slugs"**: Ако има два записа с еднакво име, те ще получат един и същ slug, което ще наруши уникалността. Добре е да се добави логига за униканлни slugs.
  ```
  from django.db import models
  from django.utils.text import slugify


  class Department(models.Model):
    name = models.CharField(
        max_length=100,
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Department.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"ID: {self.pk}, Name: {self.name}"
  ```
  Този метод е добра и надеждна практика за генериране на уникални slugs, но не е единственото решение.

**Възможни подобрения на slug логиката**

**1.Използване на библиотеки като** ```django-autoslug``` **или** ```django-extensions```: Тези библиотеки автоматизират много от процесите, свързани с slug-овете, и добавят функции за автоматично генериране и обновяване.

**2.Сложни структури на данни**: Ако имаме по-сложна структура на модела (например когато slug-овете зависят от друг модел, като категория или потребител), може да трябва да адаптираме логиката, за да осигурим уникалност на slug-овете в рамките на дадена връзка.

**3.SEO подобрения**: Можем да добавим и логика за ограничаване на дължината на slug-овете или да изключваме определени символи, които не са подходящи за URL, ако искаме да направим още по-оптимизирани URL адреси за SEO.

**ВАЖНО Е ДА ЗАПОМНИМ**

- **Slug не винаги е необходим**: Не във всеки модел slug е задължителен. Полезен е за модели, които се показват в URL адреси (например публикации в блогове, категории, продукти).
- **Уникалност и оптимизация**: Винаги трябва да следим за уникалност на slug-овете и да избягваме проблеми с дублиране.

---

## 04.Template Basics

**1.Django Template Language(DTL)**

  - Използваме, за да рендерираме информацията от view-тата.
  - Позволява ни да пишем html, който в зависимост от данните да бъде различен.
  - Единствените езици, които Django поддържа out of the box DTL и Jinja2.
  - Има други алтернативи като ```Jinja2```
  - Mожем да рендредираме в html, txt, xml и тн.
  - С него правим Server Side Rendering(SSR).
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

**2.Променливи**

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

**3.Филтри**

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

**4.Тагове**

  - Цикли, проверки и други built-in действия.
  - Таговете, които рендерират html имат затварящи тагове, защото html не зачита whitespace.
  - url tag - позволява ни да не използваме hardcoded urls
  - csrf_token - генерира произволен стринг на бак енд-а, рендерира го във фронт-енд-а и го сравнява, когато направим заявка, също запазва cookie.
```
4.1.Условни оператори (if, elif, else):

{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% elif user.is_staff %}
    <p>Welcome, staff member!</p>
{% else %}
    <p>Welcome, guest! Please log in.</p>
{% endif %}

Това е коректен пример за условни проверки в Django шаблони.
Проверките се извършват в съответствие с логическите условия за обекта user.

4.2.Проверка за празен URL:

{% if url %}
    <a href="{{ url }}">Visit this link</a>
{% else %}
    <p>No URL provided.</p>
{% endif %}

Тук се проверява дали променливата url съдържа стойност и се създава линк към нея.
Ако не е предоставен URL, се показва съобщение.

4.3.Пример с cycle:

<ul>
    {% for item in items %}
        <li class="{% cycle 'row1' 'row2' %}">{{ item }}</li>
    {% endfor %}
</ul>

Функцията cycle се използва за редуване на CSS класове (в случая 'row1' и 'row2') при всяка итерация на елементите в списъка items.
Това е удобен начин за създаване на редуващи се стилове.

4.4.Пример с lorem:

<p>{% lorem 3 p %}</p>

Този шаблонен таг генерира три абзаца с фиктивен текст ("Lorem ipsum").
Може да се използва за запълване на място по време на разработка.
```

**5.Static Files**

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
    
## 05.Forms Basics

**1.Какво са формите**

  - Уеб формата е страница, която позволява на потребителите да въвеждат данни, които след това се изпращат на сървъра за обработка.
  - В HTML, формите се намират вътре във ```<form>``` таг и използват методи като GET и POST за изпращане на данни.

**2.Форми в Django**

  - Django предлага библиотека за работа с форми чрез Python код. Това улеснява създаването и управлението на форми.
  - Полетата във формите на Django съответстват на HTML <input> елементи. Например, за да създадеш поле за име:
  - Създаваме ги във ```forms.py```
    
    ```from django import forms
       class EmployeeForm(forms.Form):
            first_name = forms.CharField(
            max_length=35,
            required=True,
       )
   - В темплейта
     ```
         <form action="{% url 'index' %}" method="post" >
            {{ employee_form }}
            {% csrf_token %}
            <button>Send</button>
         </form>
     
   - Във view-то
     ```   def index(request):
              if request.method == "GET":
                 context = {
                    "employee_form": EmployeeForm,
                 }
        
                 return render(request, "web/index.html", context)
              else:
                 print(request.POST)  # get the data but without any validation
                 form = EmployeeForm(request.POST)
        
                 if form.is_valid(): # starts validation process returns boolean
                    print(form.cleaned_data["first_name"])
                    return redirect('index')
                 else:
                    context = {
                       "employee_form": form,  # подаваме формата с грешките в нея
                    }
        
                    return render(reques t, "web/index.html", context)

**3.Django Form Class**

   -  Този клас има няколко важни функции:
       - Определя какви полета ще има формата.
       - Валидира данните, които потребителят въвежда.
       - Определя външния вид и поведението на формата.

   **Как се обработват формите в Django?**

   Когато потребителят изпрати данни, Django ги проверява дали са валидни. Ако са, продължаваш с обработката на данните.
   
   Примерен код за обработка на форма:

   ```def add_new_name(request):
        if request.method == "POST":
            form = NameForm(request.POST)
            if form.is_valid():
                # тук обработваш данните
                pass
        else:
            form = NameForm()
    
        return render(request, 'index.html', {'form': form})
   ```
Това означава, че ако заявката е POST (когато потребителят е натиснал "Изпрати"), се създава форма с въведените данни, проверява се тяхната валидност, и ако всичко е наред, се обработват данните.

**Полета във формите**

Ключовата част при създаването на форма е да се дефинират правилно полетата, например:

  - ```CharField``` – за текстови полета.
  - ```BooleanField``` – за чекбоксове.
  - ```ChoiceField``` – за избор от няколко опции (напр. радиобутони или падащо меню).

Към всяко поле можеш да добавиш допълнителни аргументи като:

  - ```label``` – за задаване на име на полето, което ще се вижда от потребителите.
  - ```required``` – дали полето е задължително.
  - ```help_text``` – малък текст, който пояснява какво трябва да въведе потребителят.
  
**4.Django Widgets**

В Django, widgets са елементи, които контролират как изглежда и се държи едно поле във формата.

Например:

- ```TextInput``` – стандартно текстово поле.
- ```Textarea``` – по-голямо текстово поле.
- ```EmailInput``` – поле за имейл адреси.
- За всяко поле на форма може да бъде зададен специфичен widget:
  
   ```comment = forms.CharField(widget=forms.Textarea)```

**5.Django ModelForm Class**

- Когато формата ти съответства на модел (например при регистрация на потребител), можеш да използваш ModelForm, за да избегнеш дублиране на дефиниции.
- Това автоматично генерира форма, базирана на модела:

  ```
  from django import forms
  from .models import Name

  class NameForm(forms.ModelForm):
     class Meta:
        model = Name
        fields = '__all__'
  ```

- В ModelForm има вътрешен клас ```Meta```, който задава опциите за поведението на формата (например кои полета от модела да се включат или изключат).

  ```
    class Meta:
      model = Name
      fields = ['first_name', 'last_name']
  ```

Формите в Django са полезен инструмент, който позволява на потребителите да взаимодействат с приложението. Те предоставят богата функционалност, която прави процеса на събиране и валидиране на данни много по-удобен.

---

## 06.Templates Advanced

**1.Template Inheritance**

Наследяването на шаблони в Django позволява създаването на основен шаблон (например ```base.html```), който може да съдържа общи елементи като заглавие, меню и футър. След това, други шаблони могат да наследяват този основен шаблон и да добавят свои специфични части.

**Пример:**
```
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}
        <p>Това е основното съдържание по подразбиране.</p>
    {% endblock %}
</body>
</html>
 ```
```
<!-- child.html -->
{% extends "base.html" %}

{% block title %}Начална Страница{% endblock %}

{% block content %}
    <h1>Добре дошли!</h1>
    <p>Това е специфичното съдържание за началната страница.</p>
{% endblock %}
```
Template Snippets

Можем да включваме части от други шаблони с ```{% include %}```. Това е полезно за многократно използване на елементи като менюта или футъри.

**Пример:**
```
<!-- nav-bar.html -->
<nav>
    <ul>
        <li><a href="/">Начало</a></li>
        <li><a href="/about">За нас</a></li>
    </ul>
</nav>
```
```<!-- main.html -->
{% extends "base.html" %}

{% block content %}
    {% include "nav-bar.html" %}
    <p>Добре дошли на главната страница!</p>
{% endblock %}
```
**2.Custom Tags**

Django позволява създаването на персонализирани тагове за сложна логика в шаблоните.
Използват се два основни метода:

  - **simple_tag**: Връща стринг.
  - **inclusion_tag**: Връща html стринг базаиран на темплейт.

**Пример за simple_tag:**

```
  # templatetags/my_tag.py
  from django import template
  
  register = template.Library()
  
  @register.simple_tag
  def greeting(name):
      return f"Здравей, {name}!"
```

В шаблона:
```
{% load my_tag %}
<p>{% greeting "Иван" %}</p>
```

**Пример за inclusion_tag:**

```
# my_tags.py
from django import template
from your_app.models import Article

register = template.Library()

@register.inclusion_tag('latest_articles.html')
def show_latest_articles(count=5):
  latest_articles = Article.objects.order_by('-published_date')[:count]
  return {'latest_articles': latest_articles}

```

- Тук, ```show_latest_articles``` е функцията, която ще бъде използвана в шаблона като таг.
- Тя извлича последните 5 статии (или броя, който е указан) от модела ```Article```.
- Рендерира шаблона ```latest_articles.html``` и му предава контекст с ключ ```latest_articles```.

В шаблона:
```
<!-- latest_articles.html -->
<ul>
    {% for article in latest_articles %}
        <li>
            <a href="{{ article.get_absolute_url }}">{{ article.title }}</a>
            <small>({{ article.published_date }})</small>
        </li>
    {% empty %}
        <li>Няма налични статии.</li>
    {% endfor %}
</ul>
```
**3.Custom Filters**

Можем да създаваме потребителски филтри, които да обработват данни в шаблоните.

**Пример:**
```
# templatetags/my_filter.py
from django import template

register = template.Library()

@register.filter
def odd(value):
    return value % 2 != 0
```

В шаблона:
```
{% load my_filter %}
{% if 3|odd %}
    <p>Числото 3 е нечетно!</p>
{% endif %}
```

**4.Bootstrap**

За създаване на лесни за използване и responsive интерфейси, Django шаблоните могат да се комбинират с **Bootstrap**. Това включва използването на предварително дефинирани CSS класове.

**Пример за Bootstrap меню:**
```
<nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Лого</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="/">Начало</a></li>
                <li class="nav-item"><a class="nav-link" href="/about">За нас</a></li>
            </ul>
        </div>
    </div>
</nav>
```

**Заключение**

  - **Template Inheritance** позволява повторно използване на общи елементи.
  - **Template Snippets** улеснява включването на многократни компоненти.
  - **Custom Tags and Filters** осигуряват гъвкавост при работа с шаблони.
  - **[Bootstrap](https://getbootstrap.com/)** е мощен инструмент за създаване на красиви и responsive уеб страници.

---
## 07.Forms Advanced

**1.Валидиране на форми в Django**

- **Django Validators** - Валидаторът е функция или клас, който проверява дали дадена стойност отговаря на определени критерии. Ако стойността е валидна, не се връща нищо, иначе се вдига грешка ```ValidationError```.
  
   Пример:
   ```
   from django.core.exceptions import ValidationError
   
   def validate_value(value):
       if value < 0:
           raise ValidationError("Value cannot be negative")
   ```
- **Повторна употреба на валидатори**: Валидаторите могат да бъдат прилагани както върху модели, така и върху форми и ```ModelForms```.
- **Формати за валидиране на форми**: Валидирането на форми се извършва по време на процеса на почистване на данните. Всяко поле на формата има специфична логика за валидиране. Можем да добавим допълнителни валидатори към полетата на формата:
    ```
    class NameForm(forms.Form):
        name = forms.CharField(
            validators=[validator_one, validator_two]
        )
    ```
- **ModelForm Validation**: Валидацията може да се извършва както на ниво модел, така и на ниво форма.
  ```
  class Person(models.Model):
    first_name = models.CharField(max_length=30, validators=[validate_value])
  ```
- **Съобщения за грешка**: Можем да персонализираме съобщенията за грешки както във формите, така и в моделите.
  
  Error messages in Form:
   ```
   class NameForm(forms.Form):
   name = forms.CharField(
       error_messages={
           'required': 'Please enter your name'
       }
   )
   ```
   Error messages in Model:
  ```
  class UserName(models.Model):
     username = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
           "unique": "The name is already taken."
        })
  ```
  Error Messages in ModelForms:
  ```
  class NameModelForm(forms.ModelForm):
    class Meta:
      ...
      error_messages = {
        'name': {
        'max_length': "The name is too long."
      }
    }
  ```
**2.Form Class Methods**

- ```__init__(self, *args, **kwargs)```: Този метод се използва за инициализация на формата и може да бъде презаписан за допълнителна настройка.
  ```
  class NameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
  ```
- ```clean(self)```: Метод за цялостно валидиране на формата.
  
  ```
  def clean(self):
    cleaned_data = super().clean()
    if cleaned_data.get('first_name') == cleaned_data.get('last_name'):
        raise ValidationError("First and last name cannot be the same.")
    return cleaned_data
  ```
- ```clean_<fieldname>(self)```: Метод за валидиране на специфично поле.
  
  ```
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if not email.endswith('@example.com'):
        raise ValidationError("Email must be from '@example.com'")
    return email
  ```
- ```is_valid(self)```: Проверява дали формата е валидна и връща ```True```, ако е.
- ```save(self, commit=True)```: Запазва данните във формата, ако тя е ```ModelForm```.
  
  ```
  form = MyModelForm(request.POST)
  if form.is_valid():
      form.save()
  ```
**3.Formsets**

- Django предоставя клас **Formset** за работа с множество форми на една страница. Това позволява едновременно управление и обработка на няколко форми.
  ```
  from django.forms import modelformset_factory
  PersonFormSet = modelformset_factory(Person, fields=('name', 'email'), extra=2)
  ```
- Използване във ```views.py```:

  ```
  def manage_people(request):
    if request.method == 'POST':
        formset = PersonFormSet(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = PersonFormSet()
    return render(request, 'manage_people.html', {'formset': formset})
  ```
**4.Styling Forms**

- **Стилизиране на форми**: Django предлага различни методи за представяне на форми - като параграфи, таблици, списъци и др.
  ```
  <form method="post">
    {{ form.as_p }}
    <input type="submit" value="Submit">
  </form>
  ```
- **Bootstrap и Crispy Forms**: Използването на ```crispy_forms``` за добавяне на ```Bootstrap``` стилизиране.
  ```
  $ pip install crispy-bootstrap5
  ```
  Конфигурация в ```settings.py```:

  ```
  INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap5",
    ...
  )
  
  CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
  
  CRISPY_TEMPLATE_PACK = "bootstrap5"
  ```
  Примерен код:

  ```
  from crispy_forms.helper import FormHelper

  class ExampleForm(forms.Form):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.form_class = 'form-horizontal'
  ```
**5.Working with Media Files**

- **Медийни файлове**: Включват снимки, аудио, видео и други документи. Django предлага начини за обработка на тези файлове, включително работа с изображения чрез библиотеката Pillow.
- **Инсталиране на Pillow**:

  ```pip install pillow```
- **Създаване на поле за изображения в модел**:

  ```
  class Person(models.Model):
    image = models.ImageField(upload_to='images/')
  ```
- **Конфигурация на медийната папка в** ```settings.py```:

  ```
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```
- **Пример за показване на изображение в шаблон**:

  ```
  <img src="{{ person.image.url }}" alt="Person Image">
  ```
