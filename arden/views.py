from django.http import HttpResponseRedirect
from django.shortcuts import render

from arden.forms import UpoForm
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


def collectUpoInfo(request):
    upoMid = request['mid']

    upoData = getInfo(upoMid)

    jsonObject = json.loads(upoData)

    info_status = jsonObject['status']

    mid = jsonObject['data']['mid']
    name = jsonObject['data']['name']
    sex = jsonObject['data']['sex']
    rank = jsonObject['data']['rank']
    face = jsonObject['data']['face']
    regtime = jsonObject['data']['regtime']
    spacesta = jsonObject['data']['spacesta']
    birthday = jsonObject['data']['birthday']
    sign = jsonObject['data']['sign']
    toutu = jsonObject['data']['toutu']
    toutuId = jsonObject['data']['toutuId']
    theme = jsonObject['data']['theme']
    theme_preview = jsonObject['data']['theme_preview']
    coins = jsonObject['data']['coins']
    im9_sign = jsonObject['data']['im9_sign']
    fans_badge = jsonObject['data']['fans_badge']

    level_info_current_level = jsonObject['data']['level_info']['current_level']

    official_verify_type = jsonObject['data']['official_verify']['type']
    official_verify_desc = jsonObject['data']['official_verify']['desc']
    official_verify_suffix = jsonObject['data']['official_verify']['suffix']

    vip_vipType = jsonObject['data']['vip']['vipType']
    vip_vipStatus = jsonObject['data']['vip']['vipStatus']
    
    Info.objects.create(info_status = info_status,
                        mid = mid,
                        name = name,
                        sex = sex,
                        rank = rank,
                        face = face,
                        regtime = regtime,
                        spacesta = spacesta,
                        birthday = birthday,
                        sign = sign,
                        toutu = toutu,
                        toutuId = toutuId,
                        theme = theme,
                        theme_preview = theme_preview,
                        coins = coins,
                        im9_sign = im9_sign,
                        fans_badge = fans_badge,
                        level_info_current_level = level_info_current_level,
                        official_verify_type = official_verify_type,
                        official_verify_desc = official_verify_desc,
                        official_verify_suffix = official_verify_suffix,
                        vip_vipType = vip_vipType,
                        vip_vipStatus = vip_vipStatus)