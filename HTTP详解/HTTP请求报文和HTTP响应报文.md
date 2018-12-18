### 请求报文和响应报文的组成

#### 请求行

包括用于请求的方法，请求URI和HTTP版本

```http
GET /HTTP/1.1
Host:
User-Agent:
Accept:
Accept-language:
Accept-encoding:
Connnection:
Cache-control:
## 除第一行外是各种首部字段
```



#### 状态行

包含表明响应结果的状态码，原因短语和HTTP版本

```http
HTTP/1.1 200 OK
Date:
Server:
Last-Modified:
Content-length:
Connection:
Content-type:
# 除第一行外是各种首部字段
```



#### 首部字段

包含表示请求和响应的各种条件和属性的各类首部。一般包含四种首部：通用首部，请求首部，响应首部和实体首部。

#### 其它

可能包含HTTP的RFC里未定义的首部（Cookie）等。