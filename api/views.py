from django.db.models import Count
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from taggit.models import Tag

from blog.models import Post
from api.views_util import obj_to_post, prev_next_post, make_tag_cloud


class ApiPostLV(BaseListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        postlist = [obj_to_post(obj) for obj in qs]
        return JsonResponse(data=postlist, safe=False, status=200)

class ApiPostDV(BaseDetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']   # 테이블로부터 꺼내온 레코드 하나
        post = obj_to_post(obj)
        post['prev'], post['next'] = prev_next_post(obj)
        return JsonResponse(data=post, safe=True, status=200)

class ApiTagCloudLV(BaseListView):
    #model = Tag                # Tag 테이블을 불러오는 세가지 방법.. 여기서는 두번째 방법 사용
    queryset = Tag.objects.annotate(count=Count('post'))
    #def get_queryset(self):
    #    return Tag.objects.all()

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        # postlist = [obj_to_post(obj) for obj in qs]

        # tagList = []  ## 별도 함수로 작성
        # for obj in qs:
        #     tagList.append({
        #         'name': obj.name,
        #         # 'count': obj.name,
        #         # 'weight': obj.name,
        #     })
        tagList = make_tag_cloud(qs)
        return JsonResponse(data=tagList, safe=False, status=200)