import certifi
import urllib3


# POST请求
def GET(url, fields=None, headers=None, ssl=True):
    return __REQUEST__('GET', url, fields, headers, ssl)


# GET请求
def POST(url, fields=None, headers=None, ssl=True):
    return __REQUEST__('POST', url, fields, headers, ssl)


# REQUEST请求
def __REQUEST__(method, url, fields, headers, ssl):
    if ssl:
        _connection = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where())
    else:
        _connection = urllib3.PoolManager()
    _body = _connection.request(method, url, fields, headers)
    return _body.data.decode()
