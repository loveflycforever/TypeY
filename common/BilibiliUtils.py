from common import HttpUtils

URLS = {'GetInfo': 'https://space.bilibili.com/ajax/member/GetInfo'}


def getInfo(mid):
    return HttpUtils.POST(URLS.get('GetInfo'), {'mid': mid})

print(getInfo(5510828))
