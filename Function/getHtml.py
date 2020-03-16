import requests
import os
from configparser import ConfigParser


# ========================================================================网页请求
def get_html(url, cookies=None):
    config_file = ''
    if os.path.exists('../config.ini'):
        config_file = '../config.ini'
    elif os.path.exists('config.ini'):
        config_file = 'config.ini'
    config = ConfigParser()
    config.read(config_file, encoding='UTF-8')
    retry_count = 0
    proxy = ''
    timeout = 0
    try:
        proxy = str(config['proxy']['proxy'])
        timeout = int(config['proxy']['timeout'])
        retry_count = int(config['proxy']['retry'])
    except:
        print('[-]Proxy config error! Please check the config.')
    i = 0
    while i < retry_count:
        try:
            if not proxy == '':
                proxies = {"http": "http://" + proxy, "https": "https://" + proxy}
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/60.0.3100.0 Safari/537.36'}
                getweb = requests.get(str(url), headers=headers, timeout=timeout, proxies=proxies, cookies=cookies)
                getweb.encoding = 'utf-8'
                return getweb.text
            else:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/68.0.3440.106 Safari/537.36'}
                getweb = requests.get(str(url), headers=headers, timeout=timeout, cookies=cookies)
                getweb.encoding = 'utf-8'
                return getweb.text
        except:
            i += 1
            print('[-]Connect retry ' + str(i) + '/' + str(retry_count))
    print('[-]Connect Failed! Please check your Proxy or Network!')
    return 'ProxyError'


