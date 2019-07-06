from ping import ping
from ssh_linux import ssh
import re
import pprint


def qytang_get_if(*ips, username='chenhu', password='chinsgis02'):
    device_if_dict = {}
    for ip in ips:
        if ping(ip):
           if_dict = {}
           result = ssh(ip, username, password)
           result_if = re.findall('(\w+|\w+/\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+', result)
           for i in range(len(result_if)):
               result_if[i][0]= result_if[i][1]
           device_if_dict.update({ip: if_dict})
        else:
            return device_if_dict.update({ip:{}})
    return device_if_dict

if __name__ == '__main__':
    pprint.pprint(qytang_get_if('10.1.1.1', username='chenhu', password='chinsgis02'),indent=4)

