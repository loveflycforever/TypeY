import datetime
import os
import certifi
import urllib3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# 写入文件
def write_file(file_path, text_content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(datetime.datetime.now().strftime('<!-- [store time] %Y-%m-%d %H:%M:%S.%f -->\n'))
        f.write(text_content)


# 读出文件
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    return file_content


# 检查文件
def check_file(file_path, file_size=0):
    return os.path.exists(file_path) and os.path.isfile(file_path) and os.path.getsize(file_path) / 1024 > file_size


# 组装文件名
def __make_up__(directory, name=None):
    if name:
        path = '%s%s.html' % (directory, name)
    else:
        path = '%s%s.html' % (directory, datetime.datetime.now().strftime('%Y-%m-%d-%H'))
    return path


# 浏览器打开地址
def browser_html(html_uri, storage_directory=None, file_name=None):
    if storage_directory and file_name:
        file_path = __make_up__(storage_directory, file_name)
        if check_file(file_path):
            store_html = read_file(file_path)
        else:
            store_html = __browser__(html_uri)
            write_file(file_path, store_html)
    else:
        store_html = __browser__(html_uri)
    return store_html


# 模拟浏览器访问
def __browser__(uri):
    options = Options()
    options.set_headless()
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.get(uri)
    html_content = browser.page_source
    browser.quit()
    return html_content


# 请求打开地址
def request_html(html_uri, need_https=True, storage_directory=None, file_name=None):
    if storage_directory and file_name:
        file_path = __make_up__(storage_directory, file_name)

        if check_file(file_path):
            store_html = read_file(file_path)
        else:
            store_html = __request__(html_uri, need_https)
            write_file(file_path, store_html)
    else:
        store_html = __request__(html_uri, need_https)
    return store_html


# 请求地址访问
def __request__(uri, need_https=True):
    if need_https:
        html_http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where())
    else:
        html_http = urllib3.PoolManager()
    html_response = html_http.request('GET', uri)
    html_content = html_response.data.decode()
    return html_content

