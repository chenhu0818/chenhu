import re #导入RE模块

ifconfig_result = 'ifconfig en0\nen0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500\nether dc:a9:04:81:2c:58\ninet6 fe80::84a:c028:21ad:2f2%en0 prefixlen 64 secured scopeid 0x8\ninet 192.168.3.20 netmask 0xffffff00 broadcast 192.168.3.255\nnd6 options=201<PERFORMNUD,DAD>\nmedia: autoselect\nstatus: active'


list_ifconfig_result = ifconfig_result.split('\n') #以换行符分隔字符串ifconfig_result中的内容，并返回一个列表。

#print(list_ifconfig_result)

for x in list_ifconfig_result: #遍历列表list_ifconfig_result，将每一行的内容赋值给x
    for y in x.split():        #以空白为分隔符遍历x，返回一个列表，列表中的元素是以空格为分隔的内容，将结果赋值给y
        if re.match('.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*',y): #使用re对y进行遍历，内容为所有ip地址格式的元素
            print(y)  #如果匹配上打印y


