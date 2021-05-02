# vue_django

### 1. 세팅 명령어
+ django-admin startproject mysite .
+ python manage.py startapp blog
+ python manage.py migrate
+ python manage.py createsuperuser

### 2. settings.py 설정
+ installed app에 앱 추가 : 'blog.apps.BlogConfig'
+ 템플릿 디렉토리 지정 : TEMPLATES의 DIR [] 부분에 os.path.join(BASE_DIR, 'templates') 추가 및 templates 폴더 만들기(import os 추가)
+ time zone 수정 : 'Asia/Seoul'
+ use_tz : False로 수정 (DB에서도 한국시간으로 표기)
+ 프로젝트 스태틱 디렉토리 정보 추가 : STATICFILES_DIR = [os.path.join(BASE_DIR, 'static)]

### 3. Models.py 설정

### 4. admin.py 설정

### 5. 마이그레이션 실행
+ python manage.py makemigrations
+ python manage.py migrate

### 6. urls.py 설정 (mysite 프로젝트, blog 앱 순서로)
 #### 6-1. mysite의 urls.py 설정
+ from . import views 추가
+ urlpatters 리스트 안에 추가
  - path('', views.HomeView.as_view(), name='home'),
  - path('blog/', include('blog.urls')),

 #### 6-2. blog의 urls.py 설정
+ blog에 urls.py 파일 생성 후 경로 입력

### 7. views.py 설정
+ 홈 views.py를 mysite 밑에 생성
+ blog 밑의 views.py 설정

### 8. templates 파일 설정
+ 템플릿 폴더 안에 home.html 파일 생성
+ blog 폴더 안에 templates 폴서 생성하고 다시 그 안에 blog 폴더 생성후  html 파일 두개 생성 (리스트랑 디테일)

### 9. 새로운 User 인증 처리를 위한 앱 등록 설정
+ python manage.py startapp accounts
+ mysite, settings.py에 앱 추가
+ 유저 인증 파일은 settings.py에 등록 : AUTH_USER_MODEL = 'account.User'

### 10. settings.py 분리 (base.py, develop.py, product.py)








