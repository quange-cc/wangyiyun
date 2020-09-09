from django.db import models


# Create your models here.


# 创建数据表
class database(models.Model):
    song_name = models.CharField('歌曲名', max_length=30)
    singer_name = models.CharField('歌手', max_length=20, default='')
    song_id = models.CharField('歌曲id', max_length=20)
    comment = models.TextField('热评内容')
    comment_date = models.CharField('评论日期', max_length=20)
    user_name = models.CharField('评论者', max_length=20)
    user_id = models.CharField('评论者id', max_length=20)
    likedCount = models.CharField('点赞数量', max_length=20, default='')
    head_link = models.CharField('头像链接', max_length=100, default='')

    class Meta:
        verbose_name = '歌曲热评数据表'
        verbose_name_plural = verbose_name

