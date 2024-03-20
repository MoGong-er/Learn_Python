list1 = ['a','b','c','d']  #通过赋值直接创建列表
list2 = list(range(1,20))  #通过list()函数将range()函数转换为列表
list3 = []  #创建空列表
list_number = [4,6,3,5,1,2,7,0,8,9]
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
#print(list_poetry)

print(str(list1.count('a')))  #count()函数可以获取到指定元素在列表中出现的次数
print(str(list1.index('a')))  #index()函数可以获取到指定元素首次出现的下标
print(sum(list2))  #sum()函数可以计算列表元素和

list_number.sort(reverse=True)  #sort()函数可以对列表元素进行排序
print(list_number)

print(sorted(list_number,reverse=False))  #sorted()函数可以排序列表，且不改变原列表顺序
print(list_number)

list_list = [int(x**5) for x in list_number] #构建列表推导式
print(list_list)

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

list_list_list = [fact(i) for i in list_number]
print(list_list_list)

list_list_list = [(map(fact,list_number))]
print(list_list_list)

print(list2)