list1 = [1,2,3,4,5,6,7,8,9]
tuple1 = (1,2,3,4)

set1 = {1,2,3,4,5,6}  #直接赋值创建集合
set2 = set(list1)     #用set()函数将可迭代对象转换为集合

set1.add(10)     #add()方法添加元素
set1.pop()       #pop()方法随机删除一个元素
set1.remove(10)  #remove()方法删除一个指定元素  
set1.clear()     #clear()清空集合
