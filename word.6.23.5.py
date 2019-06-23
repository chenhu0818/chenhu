#23日作业第5题代码：匹配IP地址信息

import re

str1 = 'Port-channel|1.89       192.168.189.254     YES    CONFIG   UP'

network_information = re.match('(\w.*)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)\s+(\w+)\s+(\w+)',str1).groups()

print('-'*100)
print('接口     :{0:<10}'.format(network_information[0]))
print('IP地址   :{0:<10}'.format(network_information[1]))
print('状态     :{0:<10}'.format(network_information[4]))



