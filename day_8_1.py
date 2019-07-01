import re
import os
import time

# (venv) hudeMacBook-Pro:paramiko chenhu$ lsof -i tcp:80
# COMMAND   PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
# Python  47244 chenhu    4u  IPv4 0x795b17a59fd27b47      0t0  TCP *:http (LISTEN)


while True:
     time.sleep(1)
     route_n_result = os.popen('lsof -i tcp:80').read()
     if re.findall('.*\s(TCP)\s(\*:http).*',route_n_result):
         print('HTTP(TCP/80)服务已被打开！')
         break

     else:
         print('等待一秒开始监控！')

