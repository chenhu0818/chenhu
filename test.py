import re
sr = ('0:01:09','3435223fdfd')
time = str(sr[0])
time2 = re.sub(':', '小时',time[:2])
time3 = re.sub(':', '分钟',time[:4])
print(time2)


