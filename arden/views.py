from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from arden.beans.UpoItem import UpoItem
from arden.forms import UpoForm
from arden.models import Info, Upo
from common.BilibiliUtils import getInfoAt

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
    return render(request, 'declare.html', {'form': form, 'label': label})


def listUpo(request):
    waiting = Upo.objects \
        .filter(condition=Upo.PENDING) \
        .order_by('-local_created_at')
    # 使用or条件查询
    queuing = Upo.objects \
        .filter(Q(condition=Upo.APPROVED) | Q(condition=Upo.FAILED)) \
        .order_by('-local_created_at')

    adverting = Upo.objects \
        .filter(Q(condition=Upo.SUCCEEDED) | Q(condition=Upo.PUBLISHED)) \
        .order_by('-local_created_at')

    recycling = Upo.objects \
        .filter(Q(condition=Upo.REJECTED) | Q(condition=Upo.REMOVED)) \
        .order_by('-local_created_at')

    data = {'waiting': ('待处理', waiting),
            'queuing': ('排队中', queuing),
            'adverting': ('公布栏', adverting),
            'recycling': ('回收站', recycling)}
    return render(request, 'list_upo.html', {'data': data})
    # result = {'status': 1000, 'message': 'OK', 'data': data}
    # return jsonResponse(result)


def approve(request):
    mid = getPostParameter(request, 'mid')
    Upo.objects.filter(mid=mid).update(condition=Upo.APPROVED)
    result = {'status': 1000, 'message': 'OK', 'data': 'you are approved'}
    return jsonResponse(result)


def reject(request):
    mid = getPostParameter(request, 'mid')
    Upo.objects.filter(mid=mid).update(condition=Upo.REJECTED)
    result = {'status': 1000, 'message': 'OK', 'data': 'you are rejected'}
    return jsonResponse(result)


def collect(request):
    upo_mid = getPostParameter(request, 'mid')
    upo_data = getInfoAt(upo_mid)
    upo_info = extractFrom(upo_data)
    upo_info.save()
    Upo.objects.filter(mid=upo_info.mid).update(info=upo_info, condition=Upo.SUCCEEDED)
    result = {'status': 1000, 'message': 'OK', 'data': '已交由处理，请稍后。'}
    return jsonResponse(result)


def extractFrom(upo_data):
    json_object = json.loads(upo_data)

    extracted = Info()
    extracted.status = json_object['status']
    extracted.mid = json_object['data']['mid']
    extracted.name = json_object['data']['name']
    extracted.sex = json_object['data']['sex']
    extracted.rank = json_object['data']['rank']
    extracted.face = json_object['data']['face']
    extracted.regtime = json_object['data']['regtime']
    extracted.spacesta = json_object['data']['spacesta']
    extracted.birthday = json_object['data']['birthday']
    extracted.sign = json_object['data']['sign']
    extracted.toutu = json_object['data']['toutu']
    extracted.toutuId = json_object['data']['toutuId']
    extracted.theme = json_object['data']['theme']
    extracted.theme_preview = json_object['data']['theme_preview']
    extracted.coins = json_object['data']['coins']
    extracted.im9_sign = json_object['data']['im9_sign']
    extracted.fans_badge = json_object['data']['fans_badge']
    extracted.level_info_current_level = json_object['data']['level_info']['current_level']
    extracted.official_verify_type = json_object['data']['official_verify']['type']
    extracted.official_verify_desc = json_object['data']['official_verify']['desc']
    extracted.official_verify_suffix = json_object['data']['official_verify']['suffix']
    extracted.vip_vipType = json_object['data']['vip']['vipType']
    extracted.vip_vipStatus = json_object['data']['vip']['vipStatus']
    return extracted


def remove(request):
    mid = getPostParameter(request, 'mid')
    Upo.objects.filter(mid=mid).update(condition=Upo.REMOVED)
    result = {'status': 1000, 'message': 'OK', 'data': 'you are removed'}
    return jsonResponse(result)


def show(request):
    published = Upo.objects.filter(condition=Upo.PUBLISHED).order_by('-local_created_at')
    # print(str(Upo.objects.filter(condition=Upo.PUBLISHED).order_by('-local_created_at').query))
    data = []
    for item in published:
        info = item.info
        print(info.name)
        upo_item = UpoItem(info.mid, info.name, info.sex, info.face, info.regtime, info.birthday, info.sign,
                           info.level_info_current_level)
        data.append(upo_item)
    result = {'status': 1000, 'message': 'OK', 'data': data}
    return jsonResponse(result)


def mapz(request, name=None):
    if name:
        name += '.html'
        return render(request, name)
    return render(request, 'declare.html')


def getPostParameter(request, key):
    return request.POST.get(key)


def jsonResponse(data):
    return HttpResponse(json.dumps(data, default=lambda obj: obj.__dict__), content_type="application/json")
