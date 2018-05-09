aList = [1, 2, 3, 4, 5]
bList = [1, 3, 5, 6, 7, 8]

print(aList) # 输出完整列表
print(aList[0]) # 输出列表的第一个元素
print(aList[1:3]) # 输出列表第2、3个元素.切片操作是包含起始下标的元素但不包含结束下标的元素。返回一个新的list
print(aList[2:]) # 获取从第3个元素开始的list中的所有元素,返回一个新的list
print(aList[-1]) # 获取list最后一个元素
print(aList[-2]) # 获取list的倒数第二个元素
print(aList[-3:]) # 获取后三个元素
print(aList + bList) # 合并列表
print(aList * 3) # 重复3次

"""
添加或删除元素
"""
aList.append(100)
print(aList)

del aList[3]
print(aList)

"""
遍历列表
"""
for x in aList:
    print(x)


# 查找元素是否在列表中
print(3 in aList)

# extend 在列表末尾追加元素
aList.extend(bList)
print(aList)

# pop移除元素
aList.pop(2)
print(aList)


############ 元组 #############
aTuple = (1, 2, 3, 4, 5)
bTuple = ('huang', 7, 5)
print(aTuple)

print(aTuple[1]) # 获取元组第二个元素

print(aTuple[2:]) # 获取元组第三个开始的所有元素

print(aTuple[-2]) # 获取元组倒数第二个元素

print(aTuple[-3:]) # 获取元组后三个元素

print(aTuple+bTuple) # 合并元组

print(aTuple*2) # 重复2次

"""
元组内置函数
"""
print(max(aTuple)) # 元组中元素最大值
print(min(aTuple)) # 元组中元素最小值
print(tuple(['a', 'b', 'c'])) # 列表转换为元组


########### 字典 ################

aDict = {'name':'huangxiang', 'password':'123456'}
bDict = {'sex':'male'}

print(aDict) # 输出完整字典
aDict['name'] = 'hujinli' # 修改字典value
print(aDict)
aDict['email'] = '875255458@qq.com' # 添加字典元素
print(aDict)
print(aDict['name']) # 根据key取value
print(aDict.values()) # 获取所有的values

del aDict['name'] # 删除字典元素
print(aDict)

#aDict.clear() # 清空字典元素
#print(aDict)


"""
内置函数
"""
print(len(aDict))
print(str(aDict))
print(type(aDict))
