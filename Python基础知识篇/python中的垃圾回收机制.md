### GC

现在的高级编程语言如java，c#都有垃圾回收机制。python也同java一样采用了垃圾回收机制，但不一样的是：**python采用的是`引用计数`为主，`标记-清除`和`分代收集`两种机制为辅的策略。**



#### python的对象分配

当创建对象时，Python立即向操作系统请求内存。（Python实现了一套自己的内存分配系统，在操作系统之上提供了一个抽象层。）

### 引用计数策略

在Python中，每个对象都会保存一个引用计数的值。来追踪到底有多少引用指向了这个对象。多一个引用，值+1，少一个引用，值-1，当值为0时，则释放该对象及回收相关的内存。

pyobject（每个对象都有一个pyobject结构体）  ob_refcnt（引用计数）

#### 缺点

* 需要额外的空间维护计数。不仅如此，每一个简单的操作都可能变成一个复杂的操作。引文python需要增加或减少一个引用计数，还可能需要释放对象。
* 相对比较慢，虽然Python随着程序执行GC很稳健，但这并不意味着快，python不断的更新着引用计数的值，特别是当我们不再使用一个大数据结构的时候，比如一个包含很多元素的列表。python可能一次性释放掉大量对象，这样的话减少引用计数就成了一个复杂的递归问题了。
* 不能解决对象的循环引用问题。（循环引用问题时指比如A、B两个对象相互引用，但没有任何外部对象引用该两个对象。虽然A、B的值都为1，但它们是应该删除的。）一个数据结构引用其自身，也就是说该数据结构是一个循环数据结构，那么某些引用计数肯定是无法清0的。

### 标记清除(Mark-Sweep)

标记清除算法是一种基于追踪回收技术实现的垃圾回收算法。通过对所有存活的对象进行一次全局遍历来确定哪些对象可以回收，遍历从根节点出发，找到所有可达对象，除此之外，不可达对象就是垃圾对象。整个过程分成两段，标记阶段找到所有存活对象，清除阶段清除所有垃圾对象。



#### 缺点

标记清除算法是一种停止启动算法，在垃圾回收器运行过程中，应用程序必须暂时停止，所以对于标记-清除算法，需要研究如何减少它的停顿时间。而分代收集回收机制就是为了减少它的停顿时间。

标记-清除算法在标记阶段需要遍历所有存活的对象，会造成一定的开销。在清除阶段，清除垃圾对象后会造成一定的内存碎片。

### 分代收集：以空间换时间

```c
#define NUM_GENERATIONS 3
#define GEN_HEAD(n) (&generations[n].head)

/* linked lists of container objects */
static struct gc_generation generations[NUM_GENERATIONS] = {
    /* PyGC_Head,                               threshold,      count */
    {{{GEN_HEAD(0), GEN_HEAD(0), 0}},           700,            0},
    {{{GEN_HEAD(1), GEN_HEAD(1), 0}},           10,             0},
    {{{GEN_HEAD(2), GEN_HEAD(2), 0}},           10,             0},
};

......
PyObject *
_PyObject_GC_Malloc(size_t basicsize)
{
    PyObject *op;
    PyGC_Head *g;
    if (basicsize > PY_SSIZE_T_MAX - sizeof(PyGC_Head))
        return PyErr_NoMemory();
    g = (PyGC_Head *)PyObject_MALLOC(
        sizeof(PyGC_Head) + basicsize);
    if (g == NULL)
        return PyErr_NoMemory();
    g->gc.gc_refs = GC_UNTRACKED;
    generations[0].count++; /* number of allocated GC objects */ //增加一个
    if (generations[0].count > generations[0].threshold &&
        enabled && //大于预分配
        generations[0].threshold &&
        !collecting &&
        !PyErr_Occurred()) {
        collecting = 1;
        collect_generations(); // 执行收集
        collecting = 0;
    }
    op = FROM_GC(g);
    return op;
}

collect_generations(void)
{
    int i;
    Py_ssize_t n = 0;

    /* Find the oldest generation (highest numbered) where the count
     * exceeds the threshold.  Objects in the that generation and
     * generations younger than it will be collected. */
    // 从最老的一代开始回收
    for (i = NUM_GENERATIONS-1; i >= 0; i--) {
        if (generations[i].count > generations[i].threshold) { //如果超过了阀值
            /* Avoid quadratic performance degradation in number
               of tracked objects. See comments at the beginning
               of this file, and issue #4074.
            */
            if (i == NUM_GENERATIONS - 1
                && long_lived_pending < long_lived_total / 4)
                continue;
            n = collect(i); // 执行收集
            break;
        }
    }
    return n;
}
```



将系统中所有的内存块根据其存活的时间划分成不同的集合，每一个集合就是一个代。垃圾收集的频率随着代的存活时间的增大而减少。（活得越长的对象，就越不可能是垃圾，就应该去减少收集的频率。

python中的分代收集共有三个代。一个代就是一个链表，所有属于同一代的内存块都放在痛一个链表中。

python使用一种不同的列表来持续追踪活跃的对象。python的内部C代码称之为零代。当你每次创建一个对象或其他什么值当时候，Python会将其加入零代列表。根据活跃时间将某些对象分入一代。三代则是从二代中的活跃对象中选出一部分放入二代。

python在进行垃圾回收时，一定会扫描0代对象，当某一代对象经过垃圾回收依然存活，那么它会归入下一代。当0代对象经过一定次数垃圾回收，则启动0代和1代的扫描清理。当1代也经历了一定次数的垃圾回收之后，那么会启动0，1，2。即对所有对象进行扫描。

启动垃圾回收的阀值为700，10次的0代垃圾回收会配合1次1代的垃圾回收，而10次一代的垃圾回收才会有一次的二代垃圾回收。



