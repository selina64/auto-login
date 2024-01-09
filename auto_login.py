import time
from Crypto.Cipher import ARC4
import urllib.parse

import requests
session = requests.Session()
session.trust_env = False

# 填写自己的用户名和密码，填完之后可以进入 http://1.1.1.3 断掉校园网，然后运行此python文件测试。
username = '221010xx'
passwd = 'xxxxxx'

def onPwdLogin():
    # 检查密码是否有效

    # 生成随机密钥
    rckey = (str(int(time.time()*1e3)))

    print(rckey)

    # 加密密码
    rc4_cipher = ARC4.new(rckey.encode('utf-8'))
    pwd = rc4_cipher.encrypt(passwd.encode('utf-8')).hex()
    print(pwd)

    # 构造请求参数
    params = {
        "opr": "pwdLogin",
        "userName": username,
        "pwd": pwd,
        "auth_tag": rckey,
        "rememberPwd": "0"
    }
    print(params)

    return params

url = "http://1.1.1.3/ac_portal/login.php"
header = {
    "Host": "1.1.1.3",
    "Origin": "http://1.1.1.3",
    "Referer":
    "http://1.1.1.3/ac_portal/20230318032256/pc.html?template=20230318032256&tabs=pwd-sms&vlanid=0&_ID_=0&switch_url=&url=http://edge-http.microsoft.com/captiveportal/generate_204&controller_type=&mac=3c-54-47-89-e6-06",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48",
    'X-Requested-With': 'XMLHttpRequest'

}
data = onPwdLogin()
x = session.post(url, headers=header, data=data)

print(x.content)