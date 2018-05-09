### list

**list可以通过以下几种方法创建：**

* 使用`[]`创建一个空的list
* 使用`[]`创建一个list：[a, b, c]
* 使用内建构造函数：list()或者list(iterable)
* 使用： x for x in iterable



### Python中的list、dict、tuple差异化理解

```python
aDict = {'a':1, 'b':2, 'c':3}
aList = [1, 2, 3, 4, 5]
aTuple = (1,2,3,4,5)
```

#### 字典（dict）

* dict是python内置数据类型，定义了键值间的一一对应关系。
* 每个元素都是key-value对，整个元素集合使用大括号括起来。
* 可以通过key获取value，但不能通过value获取key。
* key不能相同，key相同时，value会被覆盖。
* key大小写敏感，value支持任意数据类型。
* del可以通过key删除字典中特定元素。
* claer可以清空字典中所有元素。空的大括号表示没有元素的字典。



#### 列表（list）

* list中的元素是可变的。
* list是使用中括号括起来的有序元素集合。
* list列表索引从0开始。
* 负数索引表示从list的尾部开始向前存取元素。list[-1]表示取最后一个元素。list[-n]可以理解为list[len(list)-n]
* list[m:n]是list中的切片操作。表示list中m<=k<n的子集。
* list[:]返回与list中元素相同的一个新list
* list中元素可以相同。
* list可以通过+连接两个列表。



#### 元组（Tuple）

* Tuple元组是不可变的list，不能改变元组中的元素值。
* 创建Tuple的形式和list相同，区别在于把`[]`变成`()`
* Tuple元组中没有append、extend、remove、pop、index等方法，可以使用in判断元素是否存在。
* 空元组也可以使用`()`表示。但只有一个元素的元组为了避免歧义应该使用`(n,)`表示。python可能会误解为加了括号的数字n
* 列表和元组的相互转化：`aTuple=tuple(alist) alist=list(atuple)`
* 无关闭分隔符，任何以逗号分隔的无符号对象都认为是元组，如 x,y=1,2
* Tuple好处，速度比list块，代码安全。