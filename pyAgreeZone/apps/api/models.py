from django.db import models


class Department(models.Model):
    STATUS_VALID = 1
    STATUS_DELETE = 9
    name = models.CharField(verbose_name='部门名', max_length=11)
    status_choices = (
        (STATUS_VALID, '正常'),
        (STATUS_DELETE, '删除')
    )
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=status_choices, default=1)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    telephone = models.CharField(verbose_name='手机号', max_length=11)
    nickname = models.CharField(verbose_name='昵称', max_length=64)
    avatar = models.CharField(verbose_name='头像', max_length=64, null=True)
    token = models.CharField(verbose_name='用户Token', max_length=64)
    fans_count = models.PositiveIntegerField(verbose_name='粉丝个数', default=0)
    follow = models.ManyToManyField(verbose_name='关注', to='self', blank=True)
    session_key = models.CharField(verbose_name='微信会话秘钥', max_length=32)
    openid = models.CharField(verbose_name='微信用户唯一标识', max_length=32)

    depart = models.OneToOneField(verbose_name='部门', to='Department', null=True, blank=True)

    status_choices = (
        (1, '正常'),
        (2, '不正常')
    )
    status = models.PositiveSmallIntegerField(verbose_name='用户状态', choices=status_choices, default=1)

    def __str__(self):
        return self.nickname


class Topic(models.Model):
    STATUS_VALID = 1
    STATUS_INVALID = 2
    STATUS_DELETE = 9
    """
    话题
    """
    title = models.CharField(verbose_name='话题', max_length=32)
    count = models.PositiveIntegerField(verbose_name='关注度', default=0)
    status_choices = (
        (STATUS_VALID, '正常'),
        (STATUS_INVALID, '失效')
    )
    status = models.PositiveSmallIntegerField(verbose_name='话题状态', choices=status_choices, default=1)


class AgreePoint(models.Model):
    """
    赞点
    """
    cover = models.CharField(verbose_name='封面', max_length=128)
    content = models.CharField(verbose_name='内容', max_length=255)
    topic = models.ForeignKey(verbose_name='话题', to='Topic', null=True, blank=True)
    address = models.CharField(verbose_name='位置', max_length=128, null=True, blank=True)

    user = models.ForeignKey(verbose_name='发布者', to='UserInfo', related_name='agreePoint')

    favor_count = models.PositiveIntegerField(verbose_name='赞数', default=0)
    viewer_count = models.PositiveIntegerField(verbose_name='浏览数', default=0)
    comment_count = models.PositiveIntegerField(verbose_name='评论数', default=0)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)


class ViewerRecord(models.Model):
    """
    浏览器记录
    """
    agreePoint = models.ForeignKey(verbose_name='赞点', to='AgreePoint')
    user = models.ForeignKey(verbose_name='用户', to='UserInfo')


class AgreePointFavorRecord(models.Model):
    """
    赞点记录表
    """
    agreePoint = models.ForeignKey(verbose_name='赞点', to='AgreePoint')
    user = models.ForeignKey(verbose_name='点赞用户', to='UserInfo')


class CommentRecord(models.Model):
    """
    评论记录表
    """
    agreePoint = models.ForeignKey(verbose_name='赞点', to='AgreePoint')
    content = models.CharField(verbose_name='评论内容', max_length=255)
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo')
    create_date = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)

    reply = models.ForeignKey(verbose_name='回复', to='self', null=True, blank=True)
    depth = models.PositiveIntegerField(verbose_name='评论层级', default=1)

    favor_count = models.PositiveIntegerField(verbose_name='赞数', default=0)

    # 以后方便通过跟评论找到其所有的子孙评论
    root = models.ForeignKey(verbose_name='根评论', to='self', null=True, blank=True, related_name='descendant')


class CommentFavorRecord(models.Model):
    """
    评论赞记录
    """
    comment = models.ForeignKey(verbose_name='赞点', to='CommentRecord')
    user = models.ForeignKey(verbose_name='点赞用户', to='UserInfo')


class AgreePointDetail(models.Model):
    """
    赞点详细
    """
    key = models.CharField(verbose_name='腾讯对象存储中的文件名', max_length=128, help_text="用于以后在腾讯对象存储中删除")
    cos_path = models.CharField(verbose_name='腾讯对象存储中图片路径', max_length=128)
    agreePoint = models.ForeignKey(verbose_name='赞点', to='AgreePoint')


class AgreeMessage(models.Model):
    """
    赞同通知Message
    """
    STATUS_NOT_START = 1
    STATUS_START = 2
    STATUS_END = 3

    title = models.CharField(verbose_name='标题', max_length=32)
    status_choices = (
        (STATUS_NOT_START, '未开始'),
        (STATUS_START, '进行中'),
        (STATUS_END, '已结束')
    )
    content = models.CharField(verbose_name='内容', max_length=512)
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=status_choices, default=1)
    cover = models.FileField(verbose_name='封面', max_length=128)
    video = models.CharField(verbose_name='预览视频', max_length=128, null=True, blank=True)
    start_time = models.DateTimeField(verbose_name='通知开始时间')
    end_time = models.DateTimeField(verbose_name='通知结束时间')
    look_count = models.PositiveIntegerField(verbose_name='围观次数', default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '活动系列'

    def __str__(self):
        return self.title


class AgreeMessageTask(models.Model):
    """ 定时任务 """
    agreeMessage = models.OneToOneField(verbose_name='通知', to='AgreeMessage')
    task = models.CharField(verbose_name='Celery通知任务ID', max_length=64)
    end_task = models.CharField(verbose_name='Celery通知结束任务ID', max_length=64)


class AgreeBook(models.Model):
    title = models.CharField(verbose_name='书名', max_length=32)
    cover = models.CharField(verbose_name='封面', max_length=128)
    read_count = models.PositiveIntegerField(verbose_name='浏览数', default=0)
    author = models.CharField(verbose_name='作者名', max_length=32)
    url = models.CharField(verbose_name='下载链接', max_length=128)