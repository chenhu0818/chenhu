import re
import os
import time

from ssh_linux import ssh

while True:
    time.sleep(2)
    netstat = os.popen('netstat -rn').read()
    for gateway in netstat.split('\n')[2:-1]:
        re_result = re.findall('.*\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+UG?',gateway)
        break
    break

if __name__ == '__main__':
    print(ssh('192.168.3.201', 'root', 'chinagis02', cmd='pwd'))
    print('网关为:')
    print(re_result[0])