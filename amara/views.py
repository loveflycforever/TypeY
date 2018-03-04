import json
import time
from enum import Enum, unique

from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


@unique
class ResultTags(Enum):
    NORMAL_RESPONSE = dict(status=1000, message='normal response')
    PARAMETER_ERROR = dict(status=1000, message='parameter error')


class ResultBuilder:
    def __init__(self, tag, data=None):
        self.status = tag.value['status']
        self.message = tag.value['message']
        if data:
            self.data = data


class ResultBuilderEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        return json.JSONEncoder.default(self, obj)


def requestInfo(request):
    return HttpResponse(json.dumps(dict(path=request.path_info,
                                        ip=request.META['REMOTE_ADDR'],
                                        time=time.localtime(time.time()))),
                        content_type="application/json")


def dealCollections(request):
    if not POST(request):
        return HttpResponse(json.dumps(ResultBuilder(ResultTags.PARAMETER_ERROR),
                                       default=lambda obj: obj.__dict__),
                            content_type="application/json")
    try:
        uri = request.POST['uri']
    except MultiValueDictKeyError:
        return HttpResponse(json.dumps(ResultBuilder(ResultTags.PARAMETER_ERROR),
                                       default=lambda obj: obj.__dict__),
                            content_type="application/json")

    try:
        analyze_uri = analyzeUri(uri)
    except RuntimeError:
        return HttpResponse(json.dumps(ResultBuilder(ResultTags.PARAMETER_ERROR),
                                       default=lambda obj: obj.__dict__),
                            content_type="application/json")
    return HttpResponse(json.dumps(ResultBuilder(ResultTags.NORMAL_RESPONSE), default=lambda obj: obj.__dict__),
                        content_type="application/json")


def GET(request):
    return request.method == 'GET'


def POST(request):
    return request.method == 'POST'


def analyzeUri(uri):

    correspondence = {'osc': 'analyzeOSChina',
                      'xxx': 'analyzeXXX', }

    tag = None
    if 'http://www.oschina.net' in uri:
        tag = 'osc'
    elif 'xxx' in uri:
        tag = 'xxx'
    handler = correspondence.get(tag)
    if not handler:
        raise RuntimeError('Not A Scoped URI')

    return eval(handler)(uri)


def analyzeOSChina(uri):
    print(uri, 'oa')
    if 'http://www.oschina.net' not in uri:
        raise RuntimeError('Not A OSChina URI')

    return


def analyzeXXX(uri):
    print(uri, 'xxx')
    if 'xxx' not in uri:
        raise RuntimeError('Not A XXX URI')

    return
