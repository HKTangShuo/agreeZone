# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2021-10-01 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='收货人姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='联系电话')),
                ('detail', models.CharField(max_length=255, verbose_name='收货地址')),
            ],
        ),
        migrations.CreateModel(
            name='AgreePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.CharField(max_length=128, verbose_name='封面')),
                ('content', models.CharField(max_length=255, verbose_name='内容')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='位置')),
                ('favor_count', models.PositiveIntegerField(default=0, verbose_name='赞数')),
                ('viewer_count', models.PositiveIntegerField(default=0, verbose_name='浏览数')),
                ('comment_count', models.PositiveIntegerField(default=0, verbose_name='评论数')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='AgreePointDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='用于以后在腾讯对象存储中删除', max_length=128, verbose_name='腾讯对象存储中的文件名')),
                ('cos_path', models.CharField(max_length=128, verbose_name='腾讯对象存储中图片路径')),
                ('agreePoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AgreePoint', verbose_name='赞点')),
            ],
        ),
        migrations.CreateModel(
            name='AgreePointFavorRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreePoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AgreePoint', verbose_name='赞点')),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '未开拍'), (2, '预展中'), (3, '拍卖中'), (4, '已结束')], default=1, verbose_name='状态')),
                ('cover', models.FileField(max_length=128, upload_to='', verbose_name='封面')),
                ('video', models.CharField(blank=True, max_length=128, null=True, verbose_name='预览视频')),
                ('preview_start_time', models.DateTimeField(verbose_name='预展开始时间')),
                ('preview_end_time', models.DateTimeField(verbose_name='预展结束时间')),
                ('auction_start_time', models.DateTimeField(verbose_name='拍卖开始时间')),
                ('auction_end_time', models.DateTimeField(verbose_name='拍卖结束时间')),
                ('deposit', models.PositiveIntegerField(default=1000, verbose_name='全场保证金')),
                ('total_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='成交额')),
                ('goods_count', models.PositiveIntegerField(default=0, verbose_name='拍品数量')),
                ('bid_count', models.PositiveIntegerField(default=0, verbose_name='出价次数')),
                ('look_count', models.PositiveIntegerField(default=0, verbose_name='围观次数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '拍卖系列',
            },
        ),
        migrations.CreateModel(
            name='AuctionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=12, verbose_name='图录号')),
                ('title', models.CharField(max_length=32, verbose_name='拍品名称')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '未开拍'), (2, '预展中'), (3, '拍卖中'), (4, '成交'), (5, '流拍'), (6, '逾期未支付')], default=1, verbose_name='状态')),
                ('cover', models.FileField(max_length=128, upload_to='', verbose_name='拍品封面')),
                ('start_price', models.PositiveIntegerField(verbose_name='起拍价')),
                ('deal_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='成交价')),
                ('reserve_price', models.PositiveIntegerField(verbose_name='参考底价')),
                ('highest_price', models.PositiveIntegerField(verbose_name='参考高价')),
                ('video', models.CharField(blank=True, max_length=128, null=True, verbose_name='预览视频')),
                ('deposit', models.PositiveIntegerField(default=100, verbose_name='单品保证金')),
                ('unit', models.PositiveIntegerField(default=100, verbose_name='加价幅度')),
                ('bid_count', models.PositiveIntegerField(default=0, verbose_name='出价次数')),
                ('look_count', models.PositiveIntegerField(default=0, verbose_name='围观次数')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Auction', verbose_name='拍卖')),
            ],
            options={
                'verbose_name_plural': '拍品',
            },
        ),
        migrations.CreateModel(
            name='AuctionItemDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=16, verbose_name='项')),
                ('value', models.CharField(max_length=32, verbose_name='值')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AuctionItem', verbose_name='拍品')),
            ],
            options={
                'verbose_name_plural': '拍品规格',
            },
        ),
        migrations.CreateModel(
            name='AuctionItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(max_length=64, upload_to='', verbose_name='详细图')),
                ('carousel', models.BooleanField(default=False, verbose_name='是否在轮播中显示')),
                ('order', models.FloatField(default=1, verbose_name='排序')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AuctionItem', verbose_name='拍品')),
            ],
            options={
                'verbose_name_plural': '拍品详细图',
            },
        ),
        migrations.CreateModel(
            name='AuctionTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview_task', models.CharField(max_length=64, verbose_name='Celery预展任务ID')),
                ('auction_task', models.CharField(max_length=64, verbose_name='Celery拍卖任务ID')),
                ('auction_end_task', models.CharField(max_length=64, verbose_name='Celery拍卖结束任务ID')),
                ('auction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Auction', verbose_name='专场')),
            ],
        ),
        migrations.CreateModel(
            name='BidRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '竞价'), (2, '成交'), (3, '逾期未付款')], default=1, verbose_name='状态')),
                ('price', models.PositiveIntegerField(verbose_name='出价')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AuctionItem', verbose_name='拍品')),
            ],
        ),
        migrations.CreateModel(
            name='BrowseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AuctionItem', verbose_name='拍品')),
            ],
        ),
        migrations.CreateModel(
            name='CommentFavorRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CommentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='评论内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('depth', models.PositiveIntegerField(default=1, verbose_name='评论层级')),
                ('favor_count', models.PositiveIntegerField(default=0, verbose_name='赞数')),
                ('agreePoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AgreePoint', verbose_name='赞点')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CommentRecord', verbose_name='回复')),
                ('root', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='descendant', to='api.CommentRecord', verbose_name='根评论')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(1, '未开始'), (2, '领取中'), (3, '已结束')], default=1, verbose_name='状态')),
                ('title', models.CharField(max_length=32, verbose_name='优惠券名称')),
                ('money', models.PositiveIntegerField(default=200, verbose_name='抵扣金额')),
                ('count', models.PositiveIntegerField(default=100, verbose_name='创建数量')),
                ('apply_count', models.PositiveIntegerField(default=0, verbose_name='已申请数量')),
                ('apply_start_date', models.DateTimeField(verbose_name='开始领取时间')),
                ('apply_stop_date', models.DateTimeField(verbose_name='领取结束时间')),
                ('apply_start_task_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='celery任务ID')),
                ('apply_stop_task_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='celery任务ID')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Auction', verbose_name='专场')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='部门名')),
            ],
        ),
        migrations.CreateModel(
            name='DepositDeduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='金额')),
                ('deduct_type', models.SmallIntegerField(choices=[(1, '逾期扣款'), (2, '支付抵扣')], default=1, verbose_name='扣款类型')),
            ],
        ),
        migrations.CreateModel(
            name='DepositRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '未支付'), (2, '支付成功')], default=1, verbose_name='状态')),
                ('uid', models.CharField(max_length=64, verbose_name='流水号')),
                ('deposit_type', models.SmallIntegerField(choices=[(1, '单品保证金'), (2, '全场保证金')], verbose_name='保证金类型')),
                ('pay_type', models.SmallIntegerField(choices=[(1, '微信'), (2, '余额')], verbose_name='支付方式')),
                ('amount', models.PositiveIntegerField(verbose_name='金额')),
                ('balance', models.PositiveIntegerField(verbose_name='余额')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Auction', verbose_name='拍卖')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.AuctionItem', verbose_name='拍品')),
            ],
        ),
        migrations.CreateModel(
            name='DepositRefundRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=64, verbose_name='流水号')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '待退款'), (2, '退款成功')], verbose_name='状态')),
                ('amount', models.PositiveIntegerField(verbose_name='退款金额')),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DepositRecord', verbose_name='保证金')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '未支付'), (2, '待收货'), (3, '已完成'), (4, '逾期未支付'), (5, '支付中')], verbose_name='状态')),
                ('uid', models.CharField(max_length=64, verbose_name='流水号')),
                ('price', models.PositiveIntegerField(verbose_name='出价')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('twenty_four_task_id', models.CharField(blank=True, max_length=32, null=True, verbose_name='24小时后定时任务')),
                ('pay_type', models.SmallIntegerField(blank=True, choices=[(1, '微信'), (2, '余额')], null=True, verbose_name='支付方式')),
                ('real_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='实际支付金额')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Address', verbose_name='收获地址')),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DepositRecord', verbose_name='保证金')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AuctionItem', verbose_name='拍品')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='话题')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='关注度')),
            ],
        ),
        migrations.CreateModel(
            name='UserCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(1, '未使用'), (2, '已使用'), (3, '已过期')], default=1, verbose_name='状态')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Coupon', verbose_name='优惠券')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Order', verbose_name='订单')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=11, verbose_name='手机号')),
                ('nickname', models.CharField(max_length=64, verbose_name='昵称')),
                ('avatar', models.CharField(max_length=64, null=True, verbose_name='头像')),
                ('token', models.CharField(max_length=64, verbose_name='用户Token')),
                ('fans_count', models.PositiveIntegerField(default=0, verbose_name='粉丝个数')),
                ('balance', models.PositiveIntegerField(default=1000, verbose_name='账户余额')),
                ('session_key', models.CharField(max_length=32, verbose_name='微信会话秘钥')),
                ('openid', models.CharField(max_length=32, verbose_name='微信用户唯一标识')),
                ('depart', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Department', verbose_name='部门')),
                ('follow', models.ManyToManyField(blank=True, related_name='_userinfo_follow_+', to='api.UserInfo', verbose_name='关注')),
            ],
        ),
        migrations.CreateModel(
            name='ViewerRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreePoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AgreePoint', verbose_name='赞点')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='用户')),
            ],
        ),
        migrations.AddField(
            model_name='usercoupon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='depositrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='depositdeduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order', verbose_name='订单'),
        ),
        migrations.AddField(
            model_name='commentrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='评论者'),
        ),
        migrations.AddField(
            model_name='commentfavorrecord',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CommentRecord', verbose_name='赞点'),
        ),
        migrations.AddField(
            model_name='commentfavorrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='点赞用户'),
        ),
        migrations.AddField(
            model_name='browserecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='bidrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='出价人'),
        ),
        migrations.AddField(
            model_name='agreepointfavorrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='点赞用户'),
        ),
        migrations.AddField(
            model_name='agreepoint',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Topic', verbose_name='话题'),
        ),
        migrations.AddField(
            model_name='agreepoint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agreePoint', to='api.UserInfo', verbose_name='发布者'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='用户'),
        ),
    ]