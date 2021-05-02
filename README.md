# Django ------------------------------

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

# Vue -------------------------------------------

### 1. 기본 세팅
+ npm upgrade @vue/cli --global
+ vue create frontend
+ npm run serve
+ vue add vuetify
+ 로직의 흐름 : main.js -> App.vue -> .components/HelloWorld.vue

### 2. Vue와 Django의 연동

#### 2-1. vue-config.js 수정(Webpack 설정 항목 3개 추가)
```
  outputDir: 'dist',  (webpack 결과물이 놓이는 위치 지정)
  publicPath: '/',    (webpack 결과물에 대한 root dir 지정)
  assetsDir: 'static', (static 파일이 들어갈 위치 지정)
```
+ 이어서 npm run build (dist 폴더가 생성되었다.)

#### 2-2. Webpack을 이용해서 멀티 페이지 만들기 (여기서는 3개)
+ vue-config.js에 pages라는 설정항목 추가
```
pages: {

    home: {
      template: 'public/index.html',    [주석] 최종 결과물 파일을 만들 때 참조하는 템플잇
      entry: 'src/pages/main_home.js',  [주석] webpack 빌드 작업의 시작 포인트
      filename: 'home.html',            [주석] 최종 결과물 파일의 이름
      title: 'VueDjangoPhoto/home.html', [주석] 퍼블릭 아래 index.html 안에 title 안에 들어가는 내용 (htmlwebpackplugin 문법)
      minify: false,                    [주석] 최종 html 파일을 보기 쉽게 하기 위한 설정
    },

    post_list: {
      template: 'public/index.html',
      entry: 'src/pages/main_post_list.js',
      filename: 'post_list.html',
      title: 'VueDjangoPhoto/post_list.html',
      minify: false,
    }, 

    post_detail:{
      template: 'public/index.html',
      entry: 'src/pages/main_post_detail.js',
      filename: 'post_detail.html',
      title: 'VueDjangoPhoto/post_detail.html',
      minify: false,
    },
```
+ 상기 entry 포인트에 맞게 pages 폴더 생성, main.js 및 App.vue 파일 이동 및 이름 변경(main_home.js, AppHome.vue 등)하고 각 파일의 내용도 맞게 수정 (특히 파일의 위치가 한단계 더 내려갔으므로 점 하나씩 추가 ../plugins/vuefify;, ../components/HelloWorld.vue
+ 수정 완료후 빌드 npm run build

#### 2-3. Webpack devServer 설정
 + vue-config.js에 devServer 설정 추가  (루트 url에 대해서 home.html을 찾아가도록)
```
 devServer: {
    index: 'home.html',
  },
```

#### 2-4 vue 폴더 django에 자동 복사 연결 (filemanger-webpack-plugin-fixed)
+ 플러그인 설치 : npm i filemanager-webpack-plugin-fixed -D  (설치하면 보안 취약 경고.. npm audit fix 실행.. 그래도 해결 안됨)
+ vue-config.js 맨 위에 플러그인 임포트 : const FileManagerPlugin = require('filemanager-webpack-plugin-fixed');
+ vue-config.js 맨 아래에 아래 코드 추가
```
configureWebpack: {
    plugins: [
      new FileManagerPlugin({
        onStart: {                 [주석] 빌드 하기전에 ~ 해라.. 여기서는 기존 파일 삭제
          delete: [
            '../backend/static/**/',                [주석] ** 해당 폴더 및 그 예하 폴더까지 모두 
            '../backend/templates/**/',
          ],
        },

        onEnd: {                  [주석] 빌드 작업이 끝난 후에 ~ 해라.. 여기서는 기존 파일 복사 이관
          copy: [
            { source: 'dist/static', destination: '../backend/static/' },
            { source: 'dist/favicon.ico', destination: '../backend/static/img/' },  [주석] 퍼블릭 밑의 index.html 열어서 favicon 위치 수정 (여기서는 "/static/img/favicon.ico")
            { source: 'dist/home.html', destination: '../backend/templates/' },
            { source: 'dist/post*.html', destination: '../backend/templates/blog/' },
          ],
        }
      }),
    ]
  },
```





















