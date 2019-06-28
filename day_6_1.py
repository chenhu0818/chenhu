import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

for x in asa_conn.split('\n'):
    re_result = re.findall('\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{2,5}).*\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{2,5})',asa_conn)
    re_result1 = re.findall('bytes\s(\d+).*\w+\s+(UIO){1,2}',asa_conn)


asa_dict = {a:b for (a,b) in zip(re_result,re_result1)}

src = 'src'
src_ip = 'src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags = 'flags'

format_str = '{0:^10}:{1:^20}|{2:^10}:{3:^20} | {4:^10}:{5:^20} | {6:^10}:{7:^20}'
format_str1 = '{0:^10}:{1:^20}|{2:^10}:{3:^20}'

print('格式化打印输出\n')

for key,value in asa_dict.items():
    print(format_str.format(src,key[0],src_ip,key[1],dst,key[2],dst_ip,key[3]))
    print(format_str1.format(bytes_name, value[0], flags, value[1]))
    print('=' * 200)







# print('打印分析后的字典\n')
# print(asa_dict)
# print('-'*100)
#
# for key,value in asa_dict.items():
#     print(key,'\n',value,'\n','='*100)
#








# asa_infoamation_key = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5}).*\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5})',asa_infoamation)
# asa_infoamation_key2 = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5}).*\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5})',asa_infoamation)
# asa_infoamation_value = re.findall('bytes\s(\d{1,10}).*\s+(UIO)?',asa_infoamation)
# asa_infoamation_value2 = re.findall('bytes\s(\d{1,10}).*\s+(UIO)?',asa_infoamation)
