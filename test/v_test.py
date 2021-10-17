import requests




headers = {
    'Host':'cdn-01.wangaokai.com',
    'Accept-Encoding':'identity',
    'X-Playback-Session-Id':'068A7FE7-886A-4963-9405-81D3560CEE9B',
    'Accept':'*/*',
    'User-Agent':'AppleCoreMedia/1.0.0.19A346 (iPhone; U; CPU OS 15_0 like Mac OS X; zh_cn)',
    'Accept-Language':'zh-CN,zh-Hans;q=0.9',
    'Referer':'http://www.qq.com',
    'Connection':'keep-alive'
}

_v:   20190806
sign: 1634416998-96f8b2f201ad016a451edddd842e6fd2-0-145ba436fbe3275869c8cbe9412d78a0



requests.get('https://cdn-01.wangaokai.com',headers=headers)
print(request.status)


headers = {
    'Host':'ocsp.usertrust.com',
    'X-Apple-Request-UUID':'E7D3ECD6-9BF7-44AC-9D42-98589B59E96D',
    'Proxy-Connection':'keep-alive',
    'Accept':'*/*',
    'User-Agent':'com.apple.trustd/2.1',
    'Accept-Language':'en-US,en;q=0.9',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive'
}

requests.get('http://ocsp.usertrust.com/MFYwVKADAgEAME0wSzBJMAkGBSsOAwIaBQAEFM0w0kw0OoKrHwVwFYrXoQd2KZLpBBRTeb9aqitKz1SA4dibwJ3ysgNmywIQfVtRJrR2uhHbdBYLvFMNpw%3D%3D',headers=headers)
