from json import dumps

import time
from django.http import HttpResponse


def oo(request):
    return HttpResponse(dumps(dict(path=request.path_info,
                                   ip=request.META['REMOTE_ADDR'],
                                   time=time.localtime(time.time()))),
                        content_type="application/json")
