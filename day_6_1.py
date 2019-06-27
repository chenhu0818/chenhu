import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

for x in asa_conn.split('\n'):
    re_result = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5}).*\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5})',asa_conn)
    re_result1 = re.findall('bytes\s(\d{1,10}).*\s+(UIO)?',asa_conn)

asa_dict = {a:b for (a,b) in zip(re_result,re_result1)}

print(asa_dict)

src = 'src'
src_ip = 'src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags = 'flags'
format_str1 =
format_str2 =






# asa_infoamation_key = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5}).*\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5})',asa_infoamation)
# asa_infoamation_key2 = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5}).*\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5})',asa_infoamation)
# asa_infoamation_value = re.findall('bytes\s(\d{1,10}).*\s+(UIO)?',asa_infoamation)
# asa_infoamation_value2 = re.findall('bytes\s(\d{1,10}).*\s+(UIO)?',asa_infoamation)
