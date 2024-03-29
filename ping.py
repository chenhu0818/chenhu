import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR) # 关闭不必要的报错

from kamene.all import *

def ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip, 1
    else:
        return ip, 0

if __name__ == '__main__':
    result = ping('192.168.94.96')
    if result[1]:
        print(f'{result[0]} 通！')
    else:
        print(f'{result[0]} 不通！')


