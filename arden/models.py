from django.db import models
from django.db.models import ForeignKey, IntegerField
from django.db.models import TextField, BigIntegerField, DateTimeField, BooleanField, CharField


class Info(models.Model):
    status = BooleanField(default=False)
    # data
    mid = BigIntegerField(null=True)
    name = TextField(null=True)
    sex = TextField(null=True)
    rank = BigIntegerField(null=True)
    face = TextField(null=True)
    regtime = BigIntegerField(null=True)
    spacesta = BigIntegerField(null=True)
    birthday = TextField(null=True)
    sign = TextField(null=True)
    toutu = TextField(null=True)
    toutuId = BigIntegerField(null=True)
    theme = TextField(null=True)
    theme_preview = TextField(null=True)
    coins = BigIntegerField(null=True)
    im9_sign = TextField(null=True)
    fans_badge = BooleanField(default=False)
    # level_info
    level_info_current_level = BigIntegerField(null=True)
    # official_verify
    official_verify_type = BigIntegerField(null=True)
    official_verify_desc = TextField(null=True)
    official_verify_suffix = TextField(null=True)
    # vip
    vip_vipType = BigIntegerField(null=True)
    vip_vipStatus = BigIntegerField(null=True)

    local_recorded_at = DateTimeField(auto_now_add=True)


class Upo(models.Model):
    PENDING = 0
    APPROVED = 1
    REJECTED = 2
    PUBLISHED = 3
    REMOVED = -1
    CONDITION_CHOICES = ((PENDING, '待处理'),
                         (APPROVED, '已核准'),
                         (REJECTED, '已拒绝'),
                         (PUBLISHED, '已发布'),
                         (REMOVED, '已移除'),)

    mid = CharField(primary_key=True, max_length=30)
    info = ForeignKey(Info, on_delete=models.DO_NOTHING, null=True)

    condition = IntegerField(choices=CONDITION_CHOICES, default=PENDING)
    instruction = TextField(null=True)

    local_updated_at = DateTimeField(auto_now_add=True)
    local_created_at = DateTimeField(auto_now_add=True)


class LogRecord(models.Model):

    content = TextField(null=True)
    submitter = TextField(null=True)

    local_created_at = DateTimeField(auto_now_add=True)


class SubmitVideo(models.Model):
    comment = BigIntegerField()  # 总评论数
    typeid = BigIntegerField()
    play = BigIntegerField()  # 总播放量
    pic = TextField()  # 封面图
    subtitle = TextField()
    description = TextField()  # 简介
    copyright = TextField()
    title = TextField()  # 标题
    review = BigIntegerField()
    author = TextField()  # 作者
    mid = BigIntegerField()  # 作者编号
    created = BigIntegerField()  # 创建时间，秒
    length = TextField()  # 长度
    video_review = BigIntegerField()  # 总弹幕数
    favorites = BigIntegerField()  # 收藏人数
    aid = BigIntegerField()  # 视频编号
    hide_click = BooleanField()

    local_recorded_at = DateTimeField(auto_now_add=True)
