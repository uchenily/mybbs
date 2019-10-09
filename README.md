# mybbs
mybbs是一个简单的前后端分离项目, 包含前端,后端两部分. 前端使用vuejs实现, 后端使用python3实现.

### mybbs-backend项目

#### 项目说明

该项目是mybbs的后端项目, 采用python开发, 提供RESTful API服务. 

项目中使用了轻量级的RESTful开发框架`pecan`, 数据库orm框架采用的是`sqlalchemy`.

pecan本身是兼容python2和python3的, 但是由于python2即将不再维护, 项目中使用了python3特有的语法, 如果需要在python2下运行可能需要做部分更改.

#### 快速开始

为了快速搭建一个干净的python环境, 推荐使用python3中的venv模块创建一个python虚拟环境.

```bash
# 创建虚拟环境
python3 -m venv virtualenv
# 激活虚拟环境
. virtualenv/bin/activate

# 退出虚拟环境
# deactivate
```

克隆本项目到本地, 进入到mybbs-backend目录下, 安装(或者调试)项目

```bash
cd mybbs-backend

# 安装
# python setup.py install

# 开发调试
python setup.py develop
```

**推荐步骤**, 安装watchdog, 对于开发pecan应用十分有用, 可以实现代码热加载. 

```bash
pip install watchdog
```

启动项目

```bash
pecan serve config.py

# 如果安装了watchdog, 更改代码后自动加载, 不需重启服务
pecan serve config.py --reload
```





#### API调用

mybbs-backend默认使用sqlite3的内存数据库模式('`sqlite://`'), 将数据存储在内存而非文件中, 这样做的好处是在调试时更加方便, 如果需要清空数据库或者更改表结构, 只需要重启web服务即可.

该项目中只提供了RESTful风格的接口, 进行调试需要使用类似`curl`,`postman`等RESTful API调试工具. 

下面的例子中使用`curl`进行模拟请求.

**用户**

创建一个用户

POST /v1/users
```bash
curl -X POST http://localhost:8888/v1/users \
-H "Content-Type: application/json" \
-d \
'{
    "user": {
        "username": "test1", 
        "password": "password"
    }
}'
```

获取用户信息

GET /v1/users/{username}

```bash
curl http://localhost:8888/v1/users/test1
```

获取用户列表

GET /v1/users

```bash
curl http://localhost:8888/v1/users
```

更新用户信息

PUT /v1/users

```bash
curl -X PUT http://localhost:8888/v1/users \
-H "Content-Type: application/json" \
-d \
'{
    "user": {
        "username": "another",
        "password": "another"
    }
}'
```



**帖子分类**

创建一个分类

POST /v1/categories

```bash
curl -XPOST http://localhost:8888/v1/categories \
-H "Content-Type: application/json" \
-d \
'{
    "category": {
        "name": "test-category",
        "description": "this is test description"
    }
}'
```

获取分类信息

GET /v1/categories

```bash
curl http://localhost:8888/v1/categories
```



**帖子**

创建一个帖子

POST /v1/topics

```bash
curl -XPOST http://localhost:8888/v1/topics \
-H "Content-Type: application/json" \
-d \
'{
    "topic": {
        "title": "test-topic1",
        "author_id": 1,
        "content": "this is test content1",
        "category_id": 1
    }
}'
```

获取帖子列表

GET /v1/topics

```bash
curl http://localhost:8888/v1/topics
```


**回复**         
                                              
创建一个回复
                                              
POST /v1/replies
                                              
```bash                               
curl -XPOST http://localhost:8888/v1/replies \
-H "Content-Type: application/json" \
-d \
'{
    "reply": {
        "user_id": 1,
        "content": "this is test content1"
    }
}'
```                                           
                                              
获取回复列表
                                              
GET /v1/replies
                                              
```bash                                
curl http://localhost:8888/v1/replies
```                                           


### mybbs-frontend项目

#### 项目说明

该项目是mybbs项目的前端部分, 使用vuejs2.x开发, 使用了vue-router做路由, 使用了vuex管理组件状态, 使用了axios库来发送请求. 为了简洁, 没有使用其他任何依赖.

项目依赖于node环境, 需要预先安装. 另外, 项目使用yarn作为node包管理工具, 也需要进行安装.



#### 快速开始

克隆本项目到本地, 进入到mybbs-frontend目录下.

```bash
cd mybbs-frontend
```

安装依赖

```bash
yarn install
```

> 自行更改下载源以提高下载速度.

启动项目

```bash
yarn run dev

# 默认访问地址
# 用户
# http://localhost:8080
# 管理员
# http://localhost:8080/#/admin
```


