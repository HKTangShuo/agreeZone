# 赞圈小程序 V1.0

## 小程序介绍及功页面概览

### 项目介绍

​	赞圈小程序是一款基于python开发用于公司内部工作生活交流的社交小程序。为公司发布企业通知、同事间工作生活交流提供了一个平台。

目前项目代码已开源至  GitHub 地址： https://github.com/HKTangShuo/agreeZone/ 

​	**解决的痛点：**

​	目前公司所使用的企业微信"同事吧"小程序仅包含发布帖子这一个模块，功能较为单一。赞圈小程序在此基础完善并拓展提供了额外的功能以及额外提供web管理后台

​	由于时间优先目前赞圈小程序 1.0版本主要实现功能如下

1. **小程序端：**

- 用户登录认证

- 通知预览与详情查看
- 赞点列表、赞点详情、赞点点赞与评论、赞点发布
- 赞书列表、赞书详情
- 我的页面查看

​	2.  **web管理端:**

- 登录认证
- 通知维护
- 话题维护
- 部门维护
- 赞书维护
- 用户维护

### 页面预览

- 登录页面

  ![image-20211016154303380](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016154303380.png)

- 通知页面

  ![image-20211016154226734](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016154226734.png)

  

  ![image-20211016155217147](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016155217147.png)

- 赞点页面

  

  ![image-20211016154931454](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016154931454.png)

  

  ![image-20211016155017118](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016155017118.png)

  

- 发布赞点页面

  ![image-20211016154418529](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016154418529.png)

  ![image-20211016154904662](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016154904662.png)

  

- 赞书页面

  ![image-20211016155254084](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016155254084.png)

- 我的页面

  ![image-20211016155303470](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016155303470.png)

- web管理平台

  ![image-20211016155317217](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016155317217.png)

  ![image-20211016231844029](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016231844029.png)

## 技术说明以及项目部署

### 技术说明

项目主要使用python语言编写、使用到的技术主要包括：

- Django、DjangoRestFrameWork 
- Celery开启定时任务实现对通知的开始时间、结束时间进行任务监听，处理通知状态
- nginx反向代理
- 腾讯云对象存储、腾讯云短信

- 存储层使用Sqlite3、redis

其主要流程图如下：

![image-20211016175305562](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016175305562.png)





### 项目部署与目录结构(！必读！)

1. 目录结构说明

   ![image-20211016224412429](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016224412429.png)

   - minAgreeZone 为微信小程序代码
   - pyAgreeZone 为微信小程序后端和管理端后端代码 
     - apps/web 为管理端后台代码  
     - apps/api为微信小程序后台代码

2. 项目部署

   目前项目后端（pyAgreeZone) 已部署到 106.75.109.111 服务器，微信小程序须在config/api.js中配置即可以直接连接该地址 `const rootUrl = 'http://106.75.109.111/api'`

   ![image-20211016224955572](C:\Users\flm\AppData\Roaming\Typora\typora-user-images\image-20211016224955572.png)

   也可在本地开启服务(请先确保本地已安装python3.6、redis数据库) ，后台启动方式如下

   `cd pyAgreeZone`

   `pip3 install -r requiements.txt` 安装项目依赖

   `python manage.py makemigrations` 生成数据库脚本

   `python manage.py migrate` 执行数据库脚本

   `celery worker -A pyAgreeZone -l info -P eventlet` (开启celery定时任务 ，linux不加 -P eventlet)

   `python manage.py runserver` （开启服务）

   访问 http://127.0.0.1:8000/login/

   用户名 admin
   
   密码 123456

## 待完成V2.0

- 赞书下载与阅读

- 我的页面 

  - 签到功能
  - 消息中心
  - 收藏
  - 意见反馈
  - 好友动态、关注数、赞数等

- 部门认证

  ......

## 联系我

若有问题请联系唐硕 

邮箱：tangshuo@agree.com.cn

微信：pctans

