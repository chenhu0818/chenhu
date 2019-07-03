
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

# for x in list1:
#     if x in list2:
#         print(x,' in list1 and list2')
#     else:
#         print(x,'only in list1')

def same_object(x, y):
    for a in x:
        if a in y:
            print(a,' in list1 and list2')
        else:
            print(a, 'only in list1')

same_object(list1,list2)
