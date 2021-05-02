from django.views.generic import ListView, DetailView

from blog.models import Post


class PostLV(ListView):
    model = Post
    # template_name = 'blog/post_list.html' # (이 폴더 파일 이름이랑 동일하므로 생략가능)


class POSTDV(DetailView):
    model = Post
