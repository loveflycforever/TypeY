# TypeY

## 应用 Django

### 步骤

##### 安装

`pip install django`

##### 创建项目

`django-admin.py startproject TypeY`

##### 创建应用

`cd TypeY`

`python manage.py startapp amara`

##### 配置应用

`vim TypeY/setting.py`

```angular2html
INSTALLED_APPS = [
    ...
    'amara',
]
```

##### 建立模型

`vim amara/models.py`

```angular2html
class Collection(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    protocol = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    builder = models.CharField(max_length=100)
```

##### 建立数据表

`python manage.py makemigrations`

将在相应app下建立 migrations 目录，并记录下所有的关于 models 的改动

`python manage.py migrate`
此时才会真正作用到数据库，产生对应的表数据

##### 创建管理员

`python manage.py createsuperuser`

账号 root 密码 abc123456

##### 管理后台模型

`vim amara/admin.py`

```angular2html
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'protocol', 'language', 'platform', 'keeper', 'created_at',)


admin.site.register(Collection, CollectionAdmin)
```

##### 运行测试服务器

`python manage.py runserver 8081`

默认端口8080，访问 http://localhost:8081/admin 

##### 配置请求映射

`vim amara/urls.py`
```angular2html
def oo(request):
    return HttpResponse(dumps(dict(path=request.path_info,
                                   ip=request.META['REMOTE_ADDR'],
                                   time=time.localtime(time.time()))),
                        content_type="application/json")
```

`vim TypeY/urls`

```angular2html
urlpatterns = [
    ...
    path('amara/', include('amara.urls')),
]
```

访问 http://localhost:8081/amara/oo

#### 测试
`python manage.py test amara.tests`


### 错误

1 RuntimeError: You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL w
hile maintaining POST data. Change your form to point to localhost:8081/amara/collection/ (note the trailing slash), or set APPEND_SLASH=False in your
 Django settings.
 
2 TypeError: 'xxx' object is not subscriptable 

3 TypeError: Object of type 'xxx' is not JSON serializable
```angular2html
json.dumps(obj), default=lambda obj: obj.__dict__)
```
4 TypeError: 'mappingproxy' object is not callable
```angular2html
lambda obj: obj.__dict__
```

5 Forbidden (CSRF cookie not set.): xxx
```angular2html
MIDDLEWARE = [
    ...
    # 'django.middleware.csrf.CsrfViewMiddleware',
    ...
]
```
