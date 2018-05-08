from django.db import models
from django.db.models import ForeignKey
from django.db.models import TextField, BigIntegerField, DateTimeField, BooleanField, CharField


class InfoDataVip(models.Model):
    vipType = BigIntegerField()
    dueRemark = TextField()
    accessStatus = BigIntegerField()
    vipStatus = BigIntegerField()
    vipStatusWarn = TextField()

    local_recorded_at = DateTimeField(auto_now_add=True)


class InfoDataOfficialVerify(models.Model):
    type = BigIntegerField()
    desc = TextField()

    local_recorded_at = DateTimeField(auto_now_add=True)


class InfoDataNameplate(models.Model):
    nid = BigIntegerField()
    name = TextField()
    image = TextField()
    image_small = TextField()
    level = TextField()
    condition = TextField()

    local_recorded_at = DateTimeField(auto_now_add=True)


class InfoDataPendant(models.Model):
    pid = BigIntegerField()
    name = TextField()
    image = TextField()
    expire = BigIntegerField()

    local_recorded_at = DateTimeField(auto_now_add=True)


class InfoDataLevelInfo(models.Model):
    current_level = BigIntegerField()
    current_min = BigIntegerField()
    current_exp = BigIntegerField()
    next_exp = BigIntegerField()

    local_recorded_at = DateTimeField(auto_now_add=True)


class InfoData(models.Model):
    mid = TextField()
    name = TextField()
    approve = BooleanField()
    sex = TextField()
    rank = TextField()
    face = TextField()
    DisplayRank = TextField()
    regtime = BigIntegerField()
    spacesta = BigIntegerField()
    birthday = TextField()
    place = TextField()
    description = TextField()
    article = BigIntegerField()
    sign = TextField()
    level_info = ForeignKey(InfoDataLevelInfo, on_delete=models.DO_NOTHING)
    pendant = ForeignKey(InfoDataPendant, on_delete=models.DO_NOTHING)
    nameplate = ForeignKey(InfoDataNameplate, on_delete=models.DO_NOTHING)
    official_verify = ForeignKey(InfoDataOfficialVerify, on_delete=models.DO_NOTHING)
    vip = ForeignKey(InfoDataVip, on_delete=models.DO_NOTHING)
    toutu = TextField()
    toutuId = BigIntegerField()
    theme = TextField()
    theme_preview = TextField()
    coins = BigIntegerField()
    im9_sign = TextField()
    playNum = BigIntegerField()
    fans_badge = BooleanField()

    local_recorded_at = DateTimeField(auto_now_add=True)


class Info(models.Model):
    status = BooleanField()
    data = ForeignKey(InfoData, on_delete=models.DO_NOTHING)

    local_recorded_at = DateTimeField(auto_now_add=True)


class Upo(models.Model):
    mid = CharField(primary_key=True, max_length=30)
    info = ForeignKey(Info, on_delete=models.DO_NOTHING)

    submitter = TextField()
    deleted = BooleanField()

    local_updated_at = DateTimeField(auto_now_add=True)
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
