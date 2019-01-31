from django.shortcuts import render
# shortcut 是快捷方式
# Create your views here.
from django.http import HttpResponse

# 实参是浏览器给服务器发来的请求 形参用request来代替
def index(request):
    # 服务器给浏览器返回数据 这个是返回的response body
    return HttpResponse('ashen is a good man')

def withargs(request,user,password):
    return HttpResponse('阿神的账号是%s,\n密码是%s,\n迪恩爱抚登陆！' % (user,password))

from .models import Grade,Students
def grade(request):
    # 去模型Models里取数据  这个得到的是一个列表
    grade_list = Grade.obj.all()
    #将数据传递给模板  模板在渲染页面 将渲染好的页面返回浏览器
    # 第一个requests 第二个是模板的路径 第三个是字典 这个value就是模板里哪个grade
    return render(request,'my_app/grade.html',{'grade':grade_list})

def students(request):
    students_list = Students.obj.all()[0:5]  #这个相当于limit 限制取5条数据
    # 因为setting里配置的路径已经是review/django/templates了
    return render(request,'my_app/students.html',{'students':students_list})

def select_stu(request,num):
    # 这个是得到一个班级对象
    grade = Grade.obj.get(pk=num)
    # 得到这个班级的所有学生对象列表
    student_list = grade.students_set.all()
    return render(request,'my_app/students.html',{'students':student_list})

def add_students(request):
    # 主键id=1的对象给grade 也就是阿神学院1班
    grade = Grade.obj.get(pk=3)
    stu = Students.createStudents('周星驰',26,True,'如果你没有机会爱一个人 那就去爱一件事',grade)
    stu.save()
    return HttpResponse('添加学生信息成功!')

def get_attr(request):
    print('==='*45)
    print('path:',request.path)
    print('method:',request.method)
    print('encoding:',request.encoding)
    print('GET:',request.GET)
    print('POS:)',request.POST)
    print('FILES:',request.FILES)
    print('COOKIES:',request.COOKIES)
    print('session:',request.session)
    return HttpResponse('attr')

def get_abc(request):
    print('==='*45)
    # ?a=1&b=2&c=3
    a = request.GET.get('a')
    b = request.GET.get['b']  #这样写  get键 获得值 这个获得单个值 多个就报错
    c = request.GET.get('c')
    return HttpResponse(a + '  ' +b + '  ' +c)

def get_list(request):
    print('==='*45)
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')  #?a=1&a=2&c=3  这样的a有两个值 用get会报错
    return HttpResponse(a1 + '  ' +a2 + '  ' +c)

def register(request):
    print('==='*45)
    return render(request,'my_app/register.html')

def receipt(request):
    print('==='*45)
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    pwd = request.POST.get('pwd')
    hobby = request.POST.getlist('hobby')
    print(name,gender,age,pwd,hobby)
    result = ''
    for k,v in request.POST.items():
        result += k + '==>>' + v + ','

    return HttpResponse('登陆成功! 我已记录你的信息！{0}'.format(result))

def response(request):
    print('==='*45)
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res

def cookie_test(request):
    res = HttpResponse()
    # res.write('<h1>')
    cookie = res.set_cookie('good',value='Good')
    print(cookie)
    return res

def show_cookie(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write('<h1>'+cookie['good']+'</h1>')
    return res

# 服务器端重定向
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def Redirect1(request):
    # return HttpResponseRedirect('Redirect2')
    return redirect('Redirect2')

def Redirect2(request):
    return HttpResponse('哈哈哈哈哈哈哈哈哈哈哈 没想到你找到我啦')

from django.http import JsonResponse
def is_ajax(request):
    if request.is_ajax():
        a = JsonResponse({})
    pass

def indexz(request):
    # 取session   如果没取到 就用后面哪个默认值
    username = request.session.get('name',"游客")
    return render(request,'my_app/index.html',{'username':username})

def login(request):
    return render(request,'my_app/login.html')

def show_indexz(request):
    # 存session key和value
    print('===========================================================')
    username = request.POST.get('username')
    request.session['name'] = username
    # 设置 session保存的时间
    request.session.set_expiry(10)
    # 取这个键值 里的value值
    password = request.POST.get('password')
    request.session['password'] = password
    return redirect('/my_app/indexz')

from django.contrib.auth import logout
def quit_func(request):
    # 清除session
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect('/my_app/indexz')

def temp(request):
    students = Students.obj.all()
    print(students)
    return render(request,'my_app/temp.html',{'student':students,'num':0})

def good(request,id):
    return render(request,'my_app/反向解析.html',{"num":id})

def main_page(request):
    return render(request,'my_app/main.html')

def detail(request):
    return render(request,'my_app/detail.html')

def postfile(request):
    return render(request,'my_app/postfile.html')

def csrf(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    return render(request,'my_app/csrf.html',{"username":username,"pwd":pwd})

# verify验证 code 代码  验证码视图
def verifycode(request):
    # 引入绘图模块
    from PIL import Image,ImageDraw,ImageFont
    # 引入随机函数模块
    import random
    # 定义变量 用于画面的背景色 宽 高 一个元祖里放者rgb 三色的值
    background_color = (random.randrange(20,100),random.randrange(20,100),random.randrange(20,100))
    width = 100
    height = 50
    # 创建画面对象  画布
    im = Image.new('RGB',(width,height),background_color)

    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point函数绘制散点图
    for i in range(0,100):
        xy = [(random.randrange(0,width),random.randrange(0,height))]
        # 实心的点 这是颜色填充
        fill = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        draw.point(xy,fill=fill)
    # 定义验证码的备选值
    verify_value = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0,4):
        rand_str += verify_value[random.randrange(0,len(verify_value))]
    # 构造字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\msyh',40)
    #构造字体颜色
    font_color1 = (255,random.randrange(0,255),random.randrange(0,255))
    font_color2 = (255,random.randrange(0,255),random.randrange(0,255))
    font_color3 = (255,random.randrange(0,255),random.randrange(0,255))
    font_color4 = (255,random.randrange(0,255),random.randrange(0,255))
    # 绘制4个字
    draw.text((5,2),rand_str[0],font=font,fill=font_color1)
    draw.text((25,2),rand_str[1],font=font,fill=font_color2)
    draw.text((50,2),rand_str[2],font=font,fill=font_color3)
    draw.text((75,2),rand_str[3],font=font,fill=font_color4)
    # 释放画笔
    del draw

    # 存入session 用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内容文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中  文件类型为png
    im.save(buf,'png')
    #将内存中的图片数据返回给客户端 MIME类型为图片Png
    return HttpResponse(buf.getvalue(),'image/png')

def dengluqq(request):
    # 从session里拿值 默认给True  没有这个变量就不拿
    f = request.session.get('flag',True)
    if f == False:
        a = '<h1>验证码输入错误 请重新输入!</h1>'
    else:
        a = '<h1>欢迎来到黑客帝国 ubuntu admin</h1>'
    request.session.clear()
    return render(request,'my_app/验证码.html',{"flag":a})

def check(request):
    # 得到表单传来的 用户输入的验证码值
    host = request.POST.get('verify').upper()
    # 得到session里存的这个验证码里的值
    sess = request.session['verifycode'].upper()
    if host == sess:
        return redirect('/my_app/grade/')
    else:
        request.session['flag'] = False
        return redirect('/my_app/dengluqq/')

def upfile(request):
    return render(request,'my_app/upfile.html')

import os
from django.conf import settings

def savefile(request):
    if request.method == 'POST':
        # 拿出这个文件 这个是文件描述符
        f = request.FILES['file']
        # 文件在服务器端的路径
        filePath = os.path.join(settings.MEDIA_ROOT,f.name)
        with open(filePath,'wb') as fp:
            # 以文件流的形式 一段段的接收 写入
            for info in f.chunks():
                fp.write(info)
        return HttpResponse('文件上传成功!')
    else:
        return HttpResponse('文件上传失败')

from django.core.paginator import Paginator
def students_page(request,page_num):
    # 所有学生的列表
    all_list = Students.obj.all()

    # 一个列表 一个整数 表示一页显示6个对象 返回分页对象
    paginator = Paginator(all_list,2)
    # 分页对象的page方法 参数传页码
    page = paginator.page(page_num)
    return render(request,'my_app/student_page.html',{'students':page})

def ajax(request):
    return render(request,'my_app/ajax.html')

def stuinfo(request):
    stu_list = Students.obj.all()
    l = list()
    for stu in stu_list:
        l.append([stu.name,stu.age,stu.introduce])
    return JsonResponse({'data':l})

def edit(request):
    return render(request,'my_app/富文本.html')

import time
def celery(request):
    print('aaa')
    time.sleep(5)
    print('bbb')
    return render(request,'my_app/celery.html')
