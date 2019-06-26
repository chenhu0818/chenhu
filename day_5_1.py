import os
import re

route_n_result = os.popen('netstat -r').read()

ipv4_get = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+((UG)?)',route_n_result)[0]

if ipv4_get:
    print('网关为：'+ipv4_get[0])
else:
    print('信息获取失败')