import requests
from pprint import pprint
phone = ('15554421975','13256020950','13792324602')
for ph in phone:
    print("手机号码:{}".format(ph))
    res=requests.get('http://apis.juhe.cn/mobile/get?phone='+ph+'&key=e299a08a701b3bb09a4b8fca9be29564')
    pprint(res.json(),width=30)