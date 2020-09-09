from selenium import webdriver
from bs4 import BeautifulSoup
from wy import models
from django.db.models import Q
import json
import requests
import time
import threading


def singer_name_id(start_id, end_id):
    driver = webdriver.Chrome()
    # 初始歌曲主页

    # 主循环开始
    while start_id <= end_id:

        # 歌手歌曲页面链接
        url = 'https://music.163.com/artist?id=' + str(start_id)

        driver.get(url)
        time.sleep(2)
        # 切换成iframe
        driver.switch_to.frame("g_iframe")
        # 休息
        time.sleep(2)
        # 获取源码
        page_src = driver.page_source

        # 筛选数据
        soup = BeautifulSoup(page_src, 'lxml')
        items = soup.find_all('span', 'txt')

        # 判断歌曲列表是否为空
        if len(items) > 0:

            # 获取歌手
            singer_name = soup.find(attrs={"name": "keywords"})['content']

            # 循环取歌曲名称和歌曲id
            for item in items:
                song_name = item.b['title']
                song_id = item.a['href'].replace('/song?id=', '')

                # 传入歌曲id，判断数据库中是否存在
                if id_repeat(songID=song_id) == 0:
                    print('歌曲' + song_name + 'id:' + song_id + '比对未抓取，正在抓取....')
                    # 获取到的歌曲id，传给函数
                    wy_user_api(songName=song_name, songID=song_id, singer_name=singer_name)
                else:
                    print('歌曲' + song_name + 'id:' + song_id + '已抓取过数据！')

        # 休息
        time.sleep(2)
        start_id += 1

    # 关闭浏览器
    driver.close()


# 传入歌曲名称，歌曲id，获取精彩评论以及评论人的信息，写入数据库中
def wy_user_api(songName, songID, singer_name):
    # 评论API，传入歌曲id，返回json
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + songID
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.125 Safari/537.36',
        'content-type': 'application/json'
    }
    # 获取网页源码
    r = requests.get(url=url, headers=header).text
    res = json.loads(r)
    # 精彩评论数量
    hotComments_count = len(res['hotComments'])

    # 判断，如果评论数量大于 0 的时候 执行
    if hotComments_count > 0:
        # 遍历精彩评论
        for i in res['hotComments']:
            # 获取评论内容
            content = i['content']
            # 获取点赞数量
            likedCount = i['likedCount']
            # 获取时间
            time_stamp = i['time']
            # 把13位时间戳转换为10位时间戳
            time_stamp = int(time_stamp * (10 ** (10 - len(str(time_stamp)))))
            # 把时间戳转换为时间
            comment_time = time.strftime('%Y-%m-%d', time.localtime(time_stamp))
            # 获取用户名称
            nickname = i['user']['nickname']
            # 获取用户id
            userId = i['user']['userId']
            # 获取用户头像链接
            avatarUrl = i['user']['avatarUrl'] + '?param=30y30'

            # 把数据写入数据库中
            database = models.database.objects.create(song_name=songName, singer_name=singer_name, song_id=songID,
                                                      comment=content, comment_date=comment_time, user_name=nickname,
                                                      user_id=userId, likedCount=likedCount, head_link=avatarUrl)

            print(database, type(database))
            print('已写入数据库中！')
    else:
        print('没有精彩评论！')


# 传入歌曲id，数据库检索是否存在，存在返回1，不存在返回0
def id_repeat(songID):
    # Q查询songid的表项数值列表
    res = models.database.objects.filter(Q(song_id__contains=songID))
    # 查询到的数量
    discount = res.count()

    if discount == 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    t1 = threading.Thread(target=singer_name_id, args=[18001, 18002])
    t1.start()


