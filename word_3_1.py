import re

mac_address = '166  54a2.74f7.0326  DYNAMIC Gi1/0/11'

mac_information = re.match('(\d+)\s+(\w+\.\w+\.\w+)\s+(\w+)\s+(\w.*)',mac_address).groups()

print('='*100)
print('VLAN ID     : {0:<20}'.format(mac_information[0]))
print('MAC         : {0:<20}'.format(mac_information[1]))
print('Type        : {0:<20}'.format(mac_information[2]))
print('Interface   : {0:<20}'.format(mac_information[3]))

