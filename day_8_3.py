import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR) # 关闭不必要的报错

from kamene.all import *

def ping(ip_add):
    ping_pkt = IP(dst=ip_add) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip_add, True
    else:
        return ip_add, False

if __name__ == '__main__':
    result = ping('192.168.3.1')
    if result:
        print(f'{result[0]} 通！')
    else:
        print(f'{result[0]} 不通！')


