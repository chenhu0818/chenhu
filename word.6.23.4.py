#23日作业第4题代码：补齐被删除的代码-新解法

####为了一行能显示代码，修改了变量的名称
department1 = 'Security'
department2 = 'Python'
depart1 = 'cq_bomb'
depart2 = 'qinke'
cost = 456789.123456
cost1 = 1234.3456

line1 = 'Department1  name:{0:<10}   Menager:{1:<10}   COURES FEES:{2:<10.2f}  Ten END!'.format(department1, depart1, float(cost))
line2 = 'Department2  name:{0:<10}   Menager:{1:<10}   COURES FEES:{2:<10.2f}  Ten END!'.format(department2, depart2, float(cost1))

lenght = len(line1)
print('='*lenght)
print(line1)
print(line2)
print('='*lenght)