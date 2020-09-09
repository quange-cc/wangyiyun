from django.contrib import admin

# Register your models here.
from .models import database


@admin.register(database)
class Data_Admin(admin.ModelAdmin):
    # 列表想要显示的字段
    list_display = ('id', 'song_name', 'song_id', 'comment', 'comment_date', 'user_name', 'user_id')

    # 后台数据列表排序方式
    ordering = ('id',)

    # 设置点击哪些字段，进入编辑界面
    list_display_links = ('song_name',)
