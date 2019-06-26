#列表L2为L1从小到大的排序，从L1/L2中提取第一个对象，并打印

l1 = [4, 5, 7, 1, 3, 9, 0]
l2 = l1[:]

l2.sort()

for i in range(len(l1)):
    print(l1[i], l2[i])

