import os
import re

ifconfig_result = os.popen('ifconfig ' + 'en0').read()

#使用正则表达式找到IP、掩码、广播和MAC地址

#掩码显示netmask 0xffffff00，实际为255.255.255.0
ipv4_address = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
netmask = re.findall('(0[x]f{1,6}\d{2})',ifconfig_result)[0]
boradcast = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.[255]{3})',ifconfig_result)[0]
mac_address = re.findall('\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}',ifconfig_result)[0]

#打印结果
print('='*100)
print('ipv4_add    :%-10s'%ipv4_address)
print('netmask     :%-10s'%netmask)
print('boradcast   :%-10s'%boradcast)
print('mac_add     :%-10s'%mac_address)


#产生网关的IP地址

#trace = os.popen('traceroute ' + '163.com').read()

#读取文件失败，只能显示以下两行
#traceroute: Warning: 163.com has multiple addresses; using 123.58.180.8
#traceroute to 163.com (123.58.180.8), 64 hops max, 52 byte packets


# #获取不到trace信息，假设文件内容为：
text = 'traceroute to 163.com (221.130.210.74), 64 hops max, 52 byte packets' \
         '1  192.168.3.1 (192.168.3.1)  5.029 ms  4.663 ms  3.324 ms' \
         '2  221.218.112.1 (221.218.112.1)  5.638 ms  6.196 ms  7.193 ms' \
         '3  61.51.246.209 (61.51.246.209)  7.690 ms' \
         '4  124.65.60.25 (124.65.60.25)  5.941 ms'


#匹配traceroute第一跳信息
ipv4_get = re.findall('[1]\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',text)[0]

print('get_way     :%-10s'%ipv4_get)

#ping网关
#ping_result = os.open('ping ' + ipv4_get + ' -c 1').read()

ping_result = 'ping 192.168.3.1' \
              'PING 192.168.3.1 (192.168.3.1): 56 data bytes' \
              '64 bytes from 192.168.3.1: icmp_seq=0 ttl=64 time=3.720 ms'

re_ping_result =re.findall('(64\s+byte.*\s)(ttl=\d{1,3})',ping_result)[0]

#ping信息
print('-'*100)

if re_ping_result:
    print(re_ping_result)
    print('网关可达!')
else:
    print('网关不可达!')