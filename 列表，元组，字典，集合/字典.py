list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']

dict1 = {'666':2,(2.3):[1,'字典']}  #赋值直接创建字典，字典的键是唯一且不可变的，故列表不能是键
dictionary = {'键':'值'}

dict_none = {}  #空字典
dict_none_2 = dict()  #dict()方法创建字典

dict_name = dict(zip(list1,list2))   #zip()方法创建字典，列表list1为键，列表list2为值
print(dict_name)

print(dict_name[4] if 4 in dict_name else 'None')  #用if in获取指定值是否存在于字典

print(dict_name.get(5,666))  #用get()方法获取指定键的值, 当指定键不存在，返回第二个参数

print(dict_name.items())  #用items()方法遍历字典并返回元组

for items in dict_name.items():  #for循环遍历字典
    print(items)                 #返回值是元组

dict_name[5] = 'f'  #dict[key]=value来添加元素
del dict_name[1]
print(dict_name)