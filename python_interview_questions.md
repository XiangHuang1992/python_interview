

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [-](#-)

<!-- markdown-toc end -->


### Basic Python Interview Question

1. What are the supported data types in Python?
> * Numbers
> * String
> * List
> * Tuple
>> Dictionary

2. What is the difference between list and tuples?
| List                                 | Tuple                                                        |
|--------------------------------------|--------------------------------------------------------------|
| List are mutable. they can be edited | Tuples are immutable. tuples are lists which can't be edited |
| List are slower than tuples          | Tuples are faster than list                                  |
| Syntax: list_1 = [10, 'abc', 20]     | Syntax: tup_1 = (10, 'abc', 20)                              |

3. how is memory managed in Python?

> * Python memory is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have an access to this private heap and interpreter takes care of this Python private heap.

> * The allocation of Python heap space for Python objects is done by Python memory manager. The core API gives access to some tools for the programmer to code.

> * Python also have an inbuilt garbage collector, which recycle all the unused memory and frees the memory and makes it available to the heap space. 

4. Explain Inheritance in Python with an example.

Inheritance allows One class to gain all the members(say attributes and methods) of another class. Inheritance provides code reusability, makes it easier to create and maintain an application. The class from which we are inheriting is called super-class and the class that is inherited is called a derived / child class.

> * Single Inheritance – where a derived class acquires the members of a single super class.
> * Multi-level inheritance – a derived class d1 in inherited from base class base1, and d2 is inherited from base2.
> * Hierarchical inheritance – from one base class you can inherit any number of child classes
> * Multiple inheritance – a derived class is inherited from more than one base class.

5. Whenever Python exits, why isn’t all the memory de-allocated?

> * Whenever Python exits, especially those Python modules which are having circular references to other objects or the objects that are referenced from the global namespaces are not always de-allocated or freed.
> * It is impossible to de-allocate those portions of memory that are reserved by the C library.
> * On exit, because of having its own efficient clean up mechanism, Python would try to de-allocate/destroy every other object.

6. What is dictionary in Python?

> * The built-in datatypes in Python is called dictionary. It defines one-to-one relationship between keys and values. Dictionaries contain pair of keys and their corresponding values. Dictionaries are indexed by keys.

'''python
dict_1 = {'country': 'china', 'code': '+86'}
print(dict[country])
'''

7. Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.

8. Write a sorting algorithm for a numerical dataset in Python.

9. How will you reverse a list?

10. How will you remove last object from a list?

11. What are negative indexes and why are they used?

12. Explain split(), sub(), subn() methods of “re” module in Python.

13. What is the difference between range & xrange?

14. What is pickling and unpickling?

15. What is map function in Python?

16. How to get indices of N maximum values in a NumPy array?

17. What is a Python module?

18. Name the File-related modules in Python?

19. Explain the use of with statement?

20. Explain all the file processing modes supported by Python?

21. How many kinds of sequences are supported by Python? What are they?

22. How do you perform pattern matching in Python? Explain

23. How to display the contents of text file in reverse order?

24. What is the difference between NumPy and SciPy?

25. Is Python object oriented? what is object oriented programming?

26. Does Python supports interfaces like in Java? Discuss.

27. What are Accessors, mutators, @property?

28. Differentiate between append() and extend() methods.?

29. Name few methods that are used to implement Functionally Oriented Programming in Python?

30. what are the key feathures of Python? 

31. How is memory managed in Python?

> * memory management in python is managed by python private heap space. all python objects and data structures are located in a private heap. the programmer does not have access to this private heap. python interpreter takes care of this instead. python的内存管理由Python私有堆内存管理。所有Python对象和数据结构都位于私有堆中。由Python解释器负责处理这个问题。

> * this alloction of heap space for python objects is done by python's memory manager. this core API gives access to some tools for programmer to code。Python对象的堆内存分配由Python的内存管理器完成。核心API提供了一些程序员编写代码的工具。

> * Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made avaliable to the heap space. Python还有一个内置的垃圾收集器，它可以回收所有未使用的内存，并使其可用于堆内存。

32. Explain Inheritance in Python with an example.

Inheritance allows One class gain all the members(say attributes and methods) of another class. Inheritance provides code reusability, makes it easier to create and maintain an application. the class from which we are inheriting is called super-class and the class that is inherited is called a derived/child class. 继承允许一个类获得另一个类的所有成员，继承可以提高代码可重用性，让我们创建和维护程序变得更简单。我们继承的类称为超类，继承的类称为子类或者派生类。

> * Single Inheritance - where a derived class acquires the members of a single super class. 单一继承-派生类获取单个超类的成员。

> * Multi-level inheritance - a derived class d1 in inherited form base class base1, and d2 are inherited form base2. 多级继承-从基类base1继承的派生类d1，d2从basse2继承。

> * Hierarchical inheritance - from one base class you can inherit any number of child class. 多层继承-从一个基类可以继承任意数量的子类。

> * Multiple inheritance - a derived class is inherited from more than one base class. 多重继承-派生类从多个基类继承。

33. 
