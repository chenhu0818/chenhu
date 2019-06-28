import os
import re

os.chdir('test')
print('文件中包含"qytang"关键字的文件为:')
print('方案一：')

for file_in_dir in os.listdir(os.getcwd()):
    if os.path.isfile(file_in_dir) == True:
        file = open(file_in_dir,'r')
        for x in file:
            if re.match('.*(qytang).*',x):
                print(file_in_dir)
