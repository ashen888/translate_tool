这是我个人学习django的一些项目和笔记
两个目录分别是两个项目
django知识里是学习django的笔记 从零开发

首先 要安装django
pip install django==1.81 
pip全自动安装 ==后面更上版本
如果要安装多个版本 就都装进虚拟环境中

1 现在来开始django项目
CommandLine上敲
django-admin startproject 你的项目名称
里面有一些文件
manage.py 一个命令号工具 可以多种方式跟django项目交互
有一个和你创建项目时名字一模一样的目录 里面有
__init__.py 空文件 告诉python这个目录应该被看作成一个python包
setting   项目的配置文件
urls   项目的URL声明 也是主路由
wsgi 项目与WSGI兼容的web服务器入口 wsgi是一个协议

2 配置数据库
django默认使用sqllit3数据库
在settings中 通过DATABASES选项进行数据库配置
配置mysql 在init里加两行代码
然后再setting中配置mysql的信息

3 创建应用 再一个项目可以创建多个应用 每个应用进行一种业务处理
python manage.py startapp 你的应用名称
app 目录说明
admin 站点配置
models  模型
views   视图
激活应用 才能够使用应用 在setting中将app加入到NSTALLED_APPS选项中

4定义模型 models
有一个数据表 就对应有一个模型
在models文件中定义模型 与数据库进行交互
models写好后 在数据库中生成数据表
生成迁移文件(生成sql语句) 
执行 python manage.py makemigratios
在migrations目录下生成了一个迁移文件 此时数据库中还没有生成数据表
2 执行迁移 输入数据迁移的指令  
执行python manage.py migrate
如有迁移没成功 在后面加入app名 表强行迁移

测试数据库操作  通过进入 python shell 执行python manage.py shell
查询所有数据    类名加上影藏属性objects的all()方法 可以查看所有 比如 Grade.objects.all()
添加数据  本质就是创建一个模型类的对象实例
然后用类的实例对象来操作字段 就可以增删改查了 这里面底层就是ORM 操作数据库变成了操作对象
查询单个的信息 Grade.objects.get(pk=1) 第一个对象
删除数据有物理删除和逻辑删除 物理删除就数据库里真的删了 对象名.delete()
字段是外键 就给他赋值一个对

关联对象
对象名.关联的类名的小写_set.all() 比如 grade1.students()_set.all()
需求 创建曾志伟
 s3 = grade1.students_set.create(name='曾志伟',gender=True,age=60,introduce='煎饼侠 你就是煎饼侠！')
 这样创建一个1班里的学生 学生信息如上 不用save直接保存进数据库了

开始启动服务器
python manage.py runserver ip:port
ip可以不写 默认本机ip 端口默认是8000
这是一个纯python写的轻量级web服务器 仅仅在开发测试中使用
Admin站点管理
1 内容发布
    负责添加 修改 删除内容
2 公告访问
配置Admin应用
在setting文件中的INSTALLED_APPS中添加'django.contrib.admin' 默认添加好了
创建管理员用户 python manage.py createsuperuser
默认页面是英文的页面 在setting里改语言为中文 就能汉化了

管理数据表
修改app应用目录里的admin文件 导入一下我的模型里的类就行了
自定义管理页面
identified 确认
issue 问题
属性说明 关于列表页属性 和添加 修改页属性
关联对象 需求 在一个班级里加入两名学生
布尔值显示问题
执行动作问题
以后使用装饰器来完成注册 不会用admin.site.register来注册了

视图的基本使用
对web请求进行回应 视图就是一个python函数 在views
先在项目view_django目录下的urls文件 创建路由 然后写对应处理事务的视图函数

模板的基本使用
模板是HTML页面 可以根据视图中传递过滤的数据进行填充
创建模板目录 创建templates目录 在review_django项目目录下创建
配置模板路径 setting文件
模板语法  {{输出量 可以是变量,也可以是实例对象的属性}}
这个是{%执行代码%}
定义视图 然后再配置urls路由
三部  先写模板HTML 再写视图函数 最后配置urls路由

django知识目录中有详细介绍 可以根据代码和讲解一起看








