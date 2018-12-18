1. What is Django framework ?
    * django是一个高级Web开发框架。时间长，大而全，自带ORM，社区活跃，文档齐全，大量的第三方组件。

2. Why most of them suggesting Django is good for web developement?(explain the main features)
    * 功能完善，要素齐全，该有的，可以没有的都有，自带大量的工具和框架，无需自定义、组合、增删、修改。
    * 晚上的文档，经过十多年的发展，django拥有广泛的实践案例和完善的在线文档。
    * 强大的数据库访问组件，Django的Model层自带ORM数据库组件，使得开发者无需学习其他数据库访问技术。
    * 灵活的URL映射，Django使用正则表达式管理URL映射，灵活性高。
    * 丰富的Template模版语言。
    * 自带后台管理系统admin。
    * 完整的错误信息提示。

3. What is MVC/MVT architecture ?
    * MVC：Model、View、Controller。Model层负责封装对数据库的访问，对数据库中的数据进行增删改查。View用于封装结果，生成页面展示的HTML内容。Controller用于接受请求，处理业务逻辑，与Model和View交互，返回结果。
    * MVT： Model、View、Template。Model层与MVC中M功能相同，负责和数据库交互，进行数据处理。View层与MVC中的C功能相同，接受请求，进行业务处理。Template层与MVC中的V层功能相同，负责封装构造要返回的HTMl。

4. What arechitecture is following Django ? (explain with MVT)
    * Django遵循的MVC的设计模式。
    * 客户端发送请求交给View层进行处理，View层需要调用数据的时候会调用Model层，然后Model层去数据库拿数据并返回给Model层。然后再返回View层，然后View层进行一些处理，处理的结果需要用到Template层呈现，然后又回到了View层，View层将一个列表对象返回给客户端。
    * 注意：客户端和服务端之间的HTTP请求需要实现WSGI协议。

5. What are the features available in Django web framework ?

6. Please explain the entire arechitecture of django based project?[start2end]

7. What is URL ?

8. Why django is scalable ?

9. How can you set up the database in Django?

10. What is ORM ? How SQL is differ from this same ?

11. What is Middleware ? what is Important ? How to write Custom middlewares in Django?
     * middleware是修改Django request或response对象的钩子。
     * 什么时候使用middleware？如果你想修改请求，或者被传送到view中的http request对象，或者你想修改view返回的http response对象，这些都可以通过中间件来实现。
     * Django提供了一些默认的中间件。
     * middleware的顺序非常重要。
     * 一个middleware只需要继承object类。
     * 一个middleware可以实现一些方法并且不需要实现所有的方法。
     * 一个middleware可以实现process_request但是不可以实现process_response和process_view方法。
     * 一个middleware可以实现process_response，但是不需要实现process_request方法。

12. Tell about Builtin Middlewares ? (Session,Auth,Csrf Import)

13. What is role of ALLOWED_HOSTs in Django ?

14. What is CSRF ? How it's Important in django based application?

15. What is Decorator ? How to Write Custom Decorator ? what are the builtin Decorators in Django?

16. How the Templeting system is working in django ?

17. How can you set up static files in Django ?
     * 确保django.contrib.staticfiles已经添加在INSTALL_APPS中。

     * 在settings.py中进行配置`STATIC_URL='static'`

     * 在模版文件中使用：

       ```HTML
       {% load static %}
       <img src='{% static "my_app/example.jpg" %}' alt="My Image">
       ```

     * 在我们的项目中创建一个名为static的文件夹，并将资源文件保存到对应文件夹。

     * 我们还可以使用下面这种方式来实现：

       ```python
       STATICFILES_DIRS = [
           os.path.join(BASE_DIR, "static"),
           '/var/www/static/',
       ]
       ```

     * 在实际开发部署时，我们可以使用下面的方式来存储静态资源文件：

       ```python
       #Set the STATIC_ROOT setting to the directory from which you’d like to serve these files, for example:
       
       STATIC_ROOT = "/var/www/example.com/static/"
       #Run the collectstatic management command:
       
       $ python manage.py collectstatic
       #This will copy all files from your static folders into the STATIC_ROOT directory.
       
       #Use a web server of your choice to serve the files. Deploying static files covers some common deployment strategies for static files.
       # 大多数Django应用使用一个单独的服务器来处理静态资源，例如使用nginx或者apache这类web服务器来专门处理静态资源。
       # 还有一种方式来处理静态资源文件， 那就是CDN或者云加速服务来处理静态资源。使用这种方式可以让我们忽略提供静态文件的问题，并且可以提高我们网页的加载速度。使用这种方式，和上述的基本工作流程类似，除了不用使用rsync将静态文件上传到服务器，这里是将静态文件传输到云服务器或者CDN。
       ```

       

18. what are the signals? what are the important parameter ?how to use?

19. How to query as GROUP BY in django?

20. How Django complex query will be return (Django Aggregation)?

21. How to fetch limited data from Django models like SQL Limit ?

22. What's the difference between select_related and prefetch_related?

23. Please study abouts Querysets and parameters [https://docs.djangoproject.com/en/1.11/ref/models/querysets/]

24. What is Template Tags ? How to write custom template tags ? what are the built in template tags?

25. How to inherit the A template in B template ?( template inheritance )

26. Tell about few packages which you used in your Django career?

27. Difference between Function Based views and Class based views ? which one you preffer? why?

28. Difference between Form and Model Form ? Can we add custom styles in forms fields ?

29. User authentication Django ? where you can find the bultin User(importing) ?

30. What is Model, views ?

31. What is __init __ method?

32. What is Message ? How its working ? why we call django is message framework ?

33. What does of Django field class types do?

34. Have you used Django a content management system (CMS) ?

35. How to Handle Load Management in Django ?

36. Is Django supporting Session? How do we set a varible in session ? How its working ?

37. How to improve the performance of the django application ?

38. What is Memcache ? what is redis server ?

39. Why logging is important in django application ? in which area it will important ?

40. What is Scheduling ? which packages you are using for this same ?

41. What is caching ?

42. In which django version you are using for developement ?

43. Have you heard about the South? what it will do ?

44. How do we wrtite the test cases ?

45. How do we can write the RESTfull API's?

46. REST API package ?( django-tastypy and DRF ) , please study the diff,adv,disdv ?

47. When we submit a form with out CSRF token the server will throw 403 error message, but when we are posting request from (drf or tastypy) 
     it got accepted with out any error, Why? How?

48. What is Unicode ?

49. Internationalization and localization ?

50. Which all are the Common Web application tools provided by django ?

51. What is Model Manager ? how its important ?

52. How do we add extra model field in django models?

53. What is meta class method ?

     metaclass（元类），它是类的类（怎么理解？？）。就像类定义了类的实例的行为和属性一样。元类定义了类的行为方式，类是元类的实例。

     在理解metaclass之前，你需要理解python中的类。在大多数python语言中，类是描述如何生成对象的代码片段。python中的类也是如此，在python中，类也是对象。只要使用了class关键字，python都会为其创建一个object。

54. Some times while running your project you will get error like " the port is already in use " how will you resolve the issue ? [Port Killing]

55. List out the inheritance styles in Django ?

56. What is diff between Nosql and Sql databases ? please answer with example( hint: mysql and mongo db)

57. Which ORM is using for the mongodb database integration in Django? How ? advantage ?

58. Where we are using RDBMS and Nosql databases ?

59. Differance between Oauth and Oauth2 ?

60. Study about the how the authentication working in django?

61. How do we write custom authentication backend with Django ?

62. What is token authentication ?

63. What is authentication and authorization ?

64. How to handle the high traffic in django based application ?

65. What are bultin management commands? How do we write custom management commands?

66. How you debug the application? [pdb im using]

67. Have you tried django-channels, sockets ?

68. How to implement the social media authentication in django based application ?

69. What is Hashing ? difference between hashing and encryption ?

70. What is diff List,Dictionary and Tuple ?(Please asure your answer (list[],dict{}-mut,tuple-()-imut))

71. Built in data types in Python ? give some example ?

72. what all the Advanced features added or removed from the latest version of python?

73. Memory management in Python ?

74. Is it Python Call by reference or Call by value ?

75. Do you know the difference between range and xrange?

76. What is generators ?

77. How good are you in deployment ? Are you comfortable with Linux server?

78. Have you heard about AWS , GAE for deployment ?

79. How to deploy a django project ?

80. Which web server you used for project deployment ? (Nginx or Apche) ? ( note: please look on uwsgi and gunicorn )

81. How good are you in GAE hosting ? How to host a django project in GAE ?

82. How good are you in Git commands ( please sure about the merge commands,how to resolve whilte conflit happen )

83. Study about the git commands (reset, rebase, revert)?

84. How good are you in website design ( please study basic stuffs about bootstrap,Html5,Css,Jquery)

85. Did you know about Angular js ? How its integrate with django project ?

86. Please study some stuffs regarding data mining and data visulaization ?

87. Study about Scipy and Numpy ,NLTK ?

88. Have you tried any Automation with python ? like publlish the application with server , testing, and etc?

89. Django has been updated plesae read the documents django 1.11 version ?

90. whats use of the apps.py ?

91. whats __pycache__ ? what is .pyc files will do?

     当我们运行python程序时，解释器首先会将python文件编译为字节码，并将其存储在`__pycache__`文件夹中，在该文件夹中，你会发现一堆名称和.py文件相同的，但后缀是`.pyc`和`.pyo`的文件，它们分别是程序文件的字节码编译和优化的字节码编译版本。

92. what does `if __name__ == '__main__' do ?`

     当python解释器读取源文件时，它会执行其中的所有代码。在执行代码之前，它将定义一些特殊变量。例如：如果python解析器将该模块作为主程序执行时，它会设置特殊的`__name__`变量为`__main__`，如果这个模块时从其他地方导入进来的，那么将`__name__`的变量设置为该模块的名称。

     ```python
     # Threading example
     import time, thread
     
     def myfunction(string, sleeptime, lock, *args):
         while True:
             lock.acquire()
             time.sleep(sleeptime)
             lock.release()
             time.sleep(sleeptime)
     
     if __name__ == "__main__":
         lock = thread.allocate_lock()
         thread.start_new_thread(myfunction, ("Thread #: 1", 2, lock))
         thread.start_new_thread(myfunction, ("Thread #: 2", 2, lock))
         
     """
     在执行python threading_example.py之后，当设置完特殊变量之后，它会执行import语句并加载这些模块，然后执行def块，创建一个函数并创建一个名为myfunction的变量，该变量指向函数对象。然后将读取if语句并看到__name__ == '__main__'，因此它将会执行该块。
     这样做的原因是有时候我们会编写一个py文件来直接执行它，或者它也可以被导入在另一个模块中使用。通过执行主检查，该文件会在该模块作为程序运行时自动执行该代码，而在有人只想导入模块并自行调用函数时不会执行该代码。
     """
     ```

       

93. what do you understand by django?

94. 


