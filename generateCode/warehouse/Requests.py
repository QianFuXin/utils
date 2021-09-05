def getPost():
    info = '''
    # 超文本传输的几种协议（Hyper Text Transfer Protocol，HTTP）
response = requests.get('https://api.github.com/events')
response = requests.post('http://httpbin.org/post', data={'key': 'value'})
response = requests.put('http://httpbin.org/put', data={'key': 'value'})
response = requests.delete('http://httpbin.org/delete')
response = requests.head('http://httpbin.org/get')
response = requests.options('http://httpbin.org/get')

# url附加参数
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get("http://httpbin.org/get", params=payload)
# 结果:http://httpbin.org/get?key2=value2&key1=value1
# url附加参数2
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
response = requests.get('http://httpbin.org/get', params=payload)
# 结果:http://httpbin.org/get?key1=value1&key2=value2&key2=value3

# 文本内容
response.text
# 设置编码
response.encoding = "utf-8"
# 字节内容
response.content

# 下载一张图片
from PIL import Image
from io import BytesIO

# 获取字节内容,写入Image对象
i = Image.open(BytesIO(response.content))

# json对象
response.json()

# 原始响应内容,未加工
response = requests.get('https://api.github.com/events', stream=True)
response.raw
# 读取十个字节
response.raw.read(10)
# 文本流保存到文件
with open("文件名", 'wb') as fd:
    for chunk in response.iter_content(100):
        fd.write(chunk)

# 请求头
"""
如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。
而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
如果被重定向到别的主机，授权 header 就会被删除。
代理授权 header 会被 URL 中提供的代理身份覆盖掉。
在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。
"""
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)

# post 表单
payload = {'key1': 'value1', 'key2': 'value2'}

response = requests.post("http://httpbin.org/post", data=payload)
print(response.text)
"""
结果
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
"""
# post 表单2
payload = (('key1', 'value1'), ('key1', 'value2'))
response = requests.post('http://httpbin.org/post', data=payload)
print(response.text)
"""
{
  ...
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}
"""
# post 非表单
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

response = requests.post(url, json=payload)

# post 上传文件
url = 'http://httpbin.org/post'
# 设置文件名 文件类型 请求头
files = {'file': ('report.xls', open('文件名', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
response = requests.post(url, files=files)
response.text
"""
结果
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
"""
# post 上传文件2(把字符串当作文件传进去)
url = 'http://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

response = requests.post(url, files=files)
response.text
"""
结果
{
  ...
  "files": {
    "file": "some,data,to,send\\nanother,row,to,send\\n"
  },
  ...
}
"""
# 响应码(200为正常)
response.status_code
# 查看响应码是否正常
response.status_code == requests.codes.ok
# 如果响应码正确就继续执行,否则抛出异常
response.raise_for_status()

# 响应头
response.headers
"""
{
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
}
"""
# 访问响应头(名字忽略大小写)
response.headers['Content-Type']

# 响应cookie
url = 'http://example.com/some/cookie/setting/url'
response = requests.get(url)
# 访问cookie
response.cookies
response.cookies['example_cookie_name']

# 请求cookie
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

response = requests.get(url, cookies=cookies)
response.text
'{"cookies": {"cookies_are": "working"}}'

# 重定向和请求历史
response = requests.get('http://github.com')
response.url
'https://github.com/'
response.history
# [<Response [301]>]
# 禁用重定向
response = requests.get('http://github.com', allow_redirects=False)

# head重定向
response = requests.head('http://github.com', allow_redirects=True)
response.url
'https://github.com/'
response.history
# [<Response [301]>]

# 设置超时  设定最大等待时间(减少死等待)
requests.get('http://github.com', timeout=0.001)
    '''
