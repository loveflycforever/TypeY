from common import HttpUtils

URLS = {'GetInfo': 'https://space.bilibili.com/ajax/member/GetInfo'}


def getInfoAt(mid):
    return HttpUtils.POST(URLS.get('GetInfo'), {'mid': mid}, {'Referer': 'https://space.bilibili.com/%s/' % mid})


# print(getInfoAt(5510828))
