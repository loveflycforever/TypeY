from django.http import HttpResponse
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
            new_upo.save()
            label = '提交成功，继续？'
        else:
            for error in form.errors:
                print(error.message)
            label = '信息有误'
    return render(request, 'append_upo.html', {'form': form, 'label': label})


def listUpo(request):
    waiting = Upo.objects\
        .filter(condition=Upo.PENDING)\
        .order_by('-local_created_at')

    queuing = Upo.objects\
        .filter(condition=Upo.APPROVED)\
        .filter(condition=Upo.FAILED)\
        .order_by('-local_created_at')

    adverting = Upo.objects\
        .filter(condition=Upo.SUCCEEDED)\
        .filter(condition=Upo.PUBLISHED)\
        .order_by('-local_created_at')

    recycling = Upo.objects\
        .filter(condition=Upo.REJECTED)\
        .filter(condition=Upo.REMOVED)\
        .order_by('-local_created_at')
    return render(request, 'list_upo.html', {'data': {'waiting': ('待处理', waiting),
                                                      'queuing': ('排队中', queuing),
                                                      'adverting': ('公布栏', adverting),
                                                      'recycling': ('回收站', recycling)}})


def approve(request):
    result = {'status': 1000, 'message': 'OK', 'data': 'you are approved'}
    return HttpResponse(json.dumps(result), content_type="application/json")


def reject(request):
    result = {'status': 1000, 'message': 'OK', 'data': 'you are rejected'}
    return HttpResponse(json.dumps(result), content_type="application/json")


def collect(request):
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

    info = Info.objects.create(info_status=info_status,
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

    print(info.id)
    Upo.objects.filter(mid=mid).update(info=info)
    result = {'status': 1000, 'message': 'OK', 'data': 'you are loaded'}
    return HttpResponse(json.dumps(result), content_type="application/json")


def remove(request):
    result = {'status': 1000, 'message': 'OK', 'data': 'you are removed'}
    return HttpResponse(json.dumps(result), content_type="application/json")

