import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_infoamation = asa_conn.split('\n')
asa_infoamation_line1 = asa_infoamation[0]
asa_infoamation_line2 = asa_infoamation[1]
asa_infoamation_key = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5}).*\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5})',asa_infoamation_line1)
asa_infoamation_key2 = re.findall('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5}).*\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).?(\d{2,5})',asa_infoamation_line2)
asa_infoamation_value = re.findall('bytes\s(\d{1,10}).*\s+(UIO)?',asa_infoamation_line1)
asa_infoamation_value2 = re.findall('bytes\s(\d{1,10}).*\s+(UIO)?',asa_infoamation_line2)

asa_list = [[asa_infoamation_key,asa_infoamation_value],[asa_infoamation_key2,asa_infoamation_value2]]

asa_dict = {}
for x in asa_list:
    asa_dict[x[0]] = x[1]
