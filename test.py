def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip,1
    else:
        return ip,0


if __name__ == '__main__':
    result = qytang_ping('137.78.5.254')
    if result[1]:
        print(result[0], '通!')
    else:
        print(result[0], '不通!')