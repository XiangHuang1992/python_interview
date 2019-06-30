## Redis基础数据结构

### redis基础数据结构

redis有物种基础数据结构：string(字符串)、list(列表)、set(集合)、hash(哈希)、zset(有序集合).



### string(字符串)

**Redis所有的数据结构都是以唯一的key字符串作为名称，然后通过这个唯一的key来获取相应的value数据，不同的数据结构的差异就在于value的结构不一样**。

* 字符串结构使用广泛。例如：缓存用户信息。将用户信息结构体使用JSON序列化成字符串，将序列化后的字符串塞进Redis缓存。
* Redis的字符串是动态字符串，是可修改的字符串。内部实现类似于Java的ArrayList，采用预分配冗余空间的方式来减少内存的频繁分配。

```shell
127.0.0.1:6379> set name huangxiang
OK
127.0.0.1:6379> get name
"huangxiang"
127.0.0.1:6379> EXISTS name
(integer) 1
127.0.0.1:6379> del name
(integer) 1
127.0.0.1:6379> get name
(nil)
# 批量键值对
127.0.0.1:6379> set name1 huangxiang
OK
127.0.0.1:6379> set name2 hujinli
OK
127.0.0.1:6379> MGET name1 name2
1) "huangxiang"
2) "hujinli"
127.0.0.1:6379> MSET name1 boy name2 girl name3 unknown
OK
127.0.0.1:6379> MGET name1 name2 name3
1) "boy"
2) "girl"
3) "unknown"
# 过期和set命令扩展
127.0.0.1:6379> set name huangxiang
OK
127.0.0.1:6379> get name
"huangxiang"
127.0.0.1:6379> EXPIRE name 5 # 设置5s后过期
(integer) 1
127.0.0.1:6379> get name
(nil)
127.0.0.1:6379> SETEX name 5 huangxiang # setex相当于set + expire
OK
127.0.0.1:6379> get name
(nil)
# 如果value的值是一个整数，还可以进行自增操作
127.0.0.1:6379> set age 30
OK
127.0.0.1:6379> INCR age
(integer) 31
127.0.0.1:6379> INCRBY age 5
(integer) 36
127.0.0.1:6379> INCRBY age -5
(integer) 31
```

### list(列表)

**Redis的列表相当于Java中的LinkedList，注意是链表而不是数组。这意味着它插入和删除的速度是非常快的。时间复杂度位O(1)，但是索引定位速度很慢，时间复杂度位O(n)。**

* 当列表弹出来最后一个元素之后，该数据结构被自动删除，内存被回收。
* Redis的列表结构常用来做异步队列使用。将需延后处理的任务结构体序列化成字符串塞进Redis的列表，另一个线程从这个列表中轮询数据进行处理。

```shell
# rpush lpop 右边进左边出：队列
127.0.0.1:6379> RPUSH books python java golang
(integer) 3
127.0.0.1:6379> LLEN books
(integer) 3
127.0.0.1:6379> LPOP books
"python"
127.0.0.1:6379> LPOP books
"java"
127.0.0.1:6379> LPOP books
"golang"
127.0.0.1:6379> LPOP books
(nil)
# rpush rpop 右边进右边出：栈
127.0.0.1:6379> RPUSH books python java golang
(integer) 3
127.0.0.1:6379> RPOP books
"golang"
127.0.0.1:6379> RPOP books
"java"
127.0.0.1:6379> RPOP books
"python"
127.0.0.1:6379> RPOP books
(nil)
# 
```

### hash(字典)

Redis的字典相当于Java里的HashMap，是无序字典。内部结构也与java的hashmap类似。同样的数组+链表二维结构。

不同之处时Redis的字典只能是字符串，还有rehash的方式不一样。java采用一次性rehash，Redis采取的是渐进式rehash。

### set



## 分布式锁



