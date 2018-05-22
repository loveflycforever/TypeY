from django.shortcuts import render

from arden.forms import UpoForm
from arden.models import Info, Upo
from common.BilibiliUtils import getInfo

import json


def appendUpo(request):
    form = UpoForm()
    label = '新的信息'
    if request.method == 'POST':
        form = UpoForm(request.POST)
        if form.is_valid():
            new_upo = form.save(commit=False)
            # check mid is TRUE
            new_upo.save()
            label = '提交成功，继续？'
        else:
            label = '信息有误'
    return render(request, 'append_upo.html', {'form': form, 'label': label})


def listUpo(request):
    pending_upo = Upo.objects.filter(condition=Upo.PENDING).order_by('-local_created_at')
    approved_upo = Upo.objects.filter(condition=Upo.APPROVED).order_by('-local_created_at')
    rejected_upo = Upo.objects.filter(condition=Upo.REJECTED).order_by('-local_created_at')
    published_upo = Upo.objects.filter(condition=Upo.PUBLISHED).order_by('-local_created_at')
    removed_upo = Upo.objects.filter(condition=Upo.REMOVED).order_by('-local_created_at')
    return render(request, 'list_upo.html', {'data': {'pending_upo': ('待处理', pending_upo),
                                                      'approved_upo': ('已核准', approved_upo),
                                                      'rejected_upo': ('已拒绝', rejected_upo),
                                                      'published_upo': ('已发布', published_upo),
                                                      'removed_upo': ('已移除', removed_upo)}})


def collectUpoInfo(request):
    upo_mid = request['mid']

    upo_data = getInfo(upo_mid)

    json_object = json.loads(upo_data)

    info_status = json_object['status']

    mid = json_object['data']['mid']
    name = json_object['data']['name']
    sex = json_object['data']['sex']
    rank = json_object['data']['rank']
    face = json_object['data']['face']
    regtime = json_object['data']['regtime']
    spacesta = json_object['data']['spacesta']
    birthday = json_object['data']['birthday']
    sign = json_object['data']['sign']
    toutu = json_object['data']['toutu']
    toutuId = json_object['data']['toutuId']
    theme = json_object['data']['theme']
    theme_preview = json_object['data']['theme_preview']
    coins = json_object['data']['coins']
    im9_sign = json_object['data']['im9_sign']
    fans_badge = json_object['data']['fans_badge']

    level_info_current_level = json_object['data']['level_info']['current_level']

    official_verify_type = json_object['data']['official_verify']['type']
    official_verify_desc = json_object['data']['official_verify']['desc']
    official_verify_suffix = json_object['data']['official_verify']['suffix']

    vip_vipType = json_object['data']['vip']['vipType']
    vip_vipStatus = json_object['data']['vip']['vipStatus']

    Info.objects.create(info_status=info_status,
                        mid=mid,
                        name=name,
                        sex=sex,
                        rank=rank,
                        face=face,
                        regtime=regtime,
                        spacesta=spacesta,
                        birthday=birthday,
                        sign=sign,
                        toutu=toutu,
                        toutuId=toutuId,
                        theme=theme,
                        theme_preview=theme_preview,
                        coins=coins,
                        im9_sign=im9_sign,
                        fans_badge=fans_badge,
                        level_info_current_level=level_info_current_level,
                        official_verify_type=official_verify_type,
                        official_verify_desc=official_verify_desc,
                        official_verify_suffix=official_verify_suffix,
                        vip_vipType=vip_vipType,
                        vip_vipStatus=vip_vipStatus)
