## django基础

### 整体结构

### Model层

### View层

### Form层

### Template层


## django进阶

* 如何排查Django项目的性能问题？

* 如何部署Django项目，以及不同的部署方式之间的差别？
* 部署时如何处理项目中的静态文件？
* 如何实现自定义的登录认证逻辑？
* 如何理解Django中的Model，Form，ModelForm和Field、Widgets之间的关系
* Paginator的原理是什么，如何自己实现分页逻辑？
* Model中的Field的作用是什么？
* 什么是SQL注入，ORM又是如何解决这个问题的？
* CSRF全称是什么？Django又是如何解决这个问题的？
* XSS攻击是指什么，在开发时如何避免这个攻击？
* Signal的作用以及实现逻辑？
* DATABASE配置的CONN_MAX_AGE参数的作用，以及使用场景？
* CONN_MAX_AGE的实现逻辑是什么？
* 用Django内置的User模型创建用户时是否可以直接：User(username='the5fire', password='the5fire').save() ?
* 上面的创建方式有什么问题？应该如何处理用户密码？
* 使用Django-rest-framework如何实现用户认证登录逻辑？
* Session模块在Django中的作用是什么？
* 如何自定义Django中的权限粒度，实现自己的权限逻辑？
* 如何捕获线上系统的异常？
* 如何分析某个接口相应时间过长的问题，假设响应时间为2s，一次请求涉及到数据库和缓存查询。


## 部署相关

* 如何来自动化部署项目到生产环境，具体流程？
* 介绍下常用的自动化部署工具？
* 用到哪些监控工具，作用是什么？使用中有什么不足之处？
* Supervisor的作用是什么？为何使用它？
* Gunicorn的作用是什么？为何使用它？
* 如何对系统进行压力测试？以及流量预估？
* Nginx的作用是什么？能否独立配置？有没有优化经验？
* 发版逻辑是什么，如何保证新版本发生异常时能快速回滚？





