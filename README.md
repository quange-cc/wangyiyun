网易云热评墙：每一段评论后都有一段故事
=====

### 初学python，用来学习django，练习的项目（抓取精彩评论，前端展示）

### 首页预览图
![](https://github.com/free-quan/wangyiyun/blob/master/static/images/index.png)

### 用到的库
* 1.django  (web框架)<br>
* 2.requests  <br>
* 3.bs4<br>
* 4.lxml<br/>
* 5.selenium  (自动化测试框架)<br>
* 6.json<br>
### 前端
* Layer 前端ui <br>
* salvattore ：js瀑布流插件<br>
* ajax  <br>


wp_comment.py 为网易云评论抓取，用selenium获取歌手列表页面的歌曲信息，通过歌曲id，get 网易云评论的api（一个老接口尽然存活这么久）<br>
没有开线程抓，怕封。。。晚上放着跑，跑了3天，共抓了641996条评论<br>
![](https://github.com/free-quan/wangyiyun/blob/master/static/images/20200910025542.png)

### 使用
本人抓取的数据库文件，就不上传了<br>
安装项目的必备库<br>
* 生成数据库同步脚本
```
python manage.py makemigrations
```
* 同步数据库
```
python manage.py migrate
```
* 创建超级管理员
```
python manage.py createsuperuser
```
* 启动项目
```
python manage.py runserver 8080
```
