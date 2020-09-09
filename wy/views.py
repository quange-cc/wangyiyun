import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from wy import models


# Create your views here.

def index(request):
    return render(request, 'index.html')


def comment_list(request):
    # 随机获取20条记录获取数据表数据
    dates = models.database.objects.order_by('?')[:30]

    # 获取数据数量
    data = dates.count()
    json_list = []
    for i in dates:
        json_dict = {
            'id': i.id,
            'song_name': i.song_name,
            'song_id': i.song_id,
            'comment': i.comment,
            'comment_date': i.comment_date,
            'user_name': i.user_name,
            'user_id': i.user_id,
            'head_link': i.head_link,
            'likedCount': i.likedCount,
            'singer_name': i.singer_name
        }

        json_list.append(json_dict)
    pageIndex = request.GET.get('page')
    pageSize = request.GET.get('limit')

    pages = Paginator(json_list, pageSize)
    contacts = pages.page(pageIndex)

    res = []
    for i in contacts:
        res.append(i)

    Result = {"code": 0, "msg": "", "count": data, "data": res}

    return HttpResponse(json.dumps(Result), content_type="application/json")

