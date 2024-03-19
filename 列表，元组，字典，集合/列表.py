list1 = ['a','b','c','d']  #通过赋值直接创建列表
list2 = list(range(1,20))  #通过list()函数将range()函数转换为列表
list3 = []  #创建空列表
list_poetry = ['人生自古谁无死','留取丹心照汗青']

for item in list1:
    #print(item)
    pass

for index,item in enumerate(list_poetry):  #enumerate()函数可以同时输出索引和元素
    #print(index,item,end='')
    pass

list1.append('e')  #append()函数可以向列表的末端添加一个元素
#print(len(list1),list1)  #len()函数可以获取序列的长度

list4 = ['f','g','h']
list1.extend(list4)  #extend()函数可以将一个列表中的所有值追加到原列表中
#print(max(list1),min(list1),list1)  #max()函数可以获取到序列中的最大值，min()函数可以获取最小值

list_poetry[1] = '早死晚死都得死'   #通过索引重新赋值即可修改列表中的元素
for i in list_poetry:
    #print(i)
    pass

del list_poetry[1] #del()函数可以根据索引值删除列表内元素
#print(list_poetry)

list_poetry.remove('人生自古谁无死')  #remove()方法可以根据元素移除元素
print(list_poetry)

