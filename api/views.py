from django.http import JsonResponse
from django.views.generic.list import BaseListView

from blog.models import Post
from api.views_util import obj_to_post


class ApiPostLV(BaseListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        postlist = [obj_to_post(obj) for obj in qs]
        return JsonResponse(data=postlist, safe=False, status=200)