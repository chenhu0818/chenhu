import re

asa_show = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

network_information = re.match("(\w+)\s+(\w+)\s+(\d+\.\d+\.\d+\.\d+.\d+)\s+(\w+)\s+(\d+\.\d+\.\d+\.\d+.\d+)"
                               ".\s+(\w+)\s+(\d.\d+.\d+).\s+(\w+)\s+(\d+).\s+(\w+)\s+(\w+)",asa_show).groups()
time = str(network_information[6])

print('='*100)
print('{0:<30}:{1:<30}'.format('protocol',network_information[0]))
print('{0:<30}:{1:<30}'.format(network_information[1],network_information[2]))
print('{0:<30}:{1:<30}'.format(network_information[3],network_information[4]))
print('{0:<30}:{1:<2}小时 {2:<3}分钟 {3:<3}秒'.format(network_information[5],time[0],time[2:4],time[5:7]))
print('{0:<30}:{1:<30}'.format(network_information[7],network_information[8]))
print('{0:<30}:{1:<30}'.format(network_information[9],network_information[10]))
