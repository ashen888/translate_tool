# from django.shortcuts import render

# 快捷方式 渲染
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect,HttpRequest
#这个就是一个类 创建这个类的实例 就可以返回结果

# Create your views here.

# 视图函数需要一个参数，类型 是 HttpRequest
# request 代表协议 请求方法 报头 cookie session file 都在这里面
def do_normalmap(request):
    # print("In do_normalmap")
    return HttpResponse("This is normalmap")

def withparam(request,year,month):
    return HttpResponse("This is with params{0},{1}".format(year,month))

def do_app(request):
    return HttpResponse("这是一个子路由 YP大神")

def do_param2(request,pn):
    return HttpResponse("page number is {0}".format(pn))

# 这个name是我们传入的  值是ashen
def exam(request,name):
    return HttpResponse("My name is {0}".format(name))

def myname(request):
    return HttpResponse("Your requested URL is {0}".format(reverse("ask my name")))

def v2_exception(request):
    raise Http404
    # return HttpResponse("Ok")

def v10(request):
    return HttpResponseRedirect(reverse("v11_name"))

def v11(request):
    # reverse()反转 把这个URL的name反转成URL
    return HttpResponseRedirect(reverse("v12_name"))

def v12(request):
    return HttpResponse("小伙子 我想送你一句话\n 做人如果没梦想,那和咸鱼有什么区别")

def req_get(request):
    result = ""
    for k,v in request.GET.items():
        result += k + '-->' + v
        result += ','
        print(k,v)
    # print(request.GET.items())
        return HttpResponse("Get value of Request is {0}".format(result))

def form_get(request):
    #渲染模板并返回
    return render_to_response(request,"for_post.html")

def form_post(request):
    result = ""
    for k, v in request.POST.items():
        result += k + '-->' + v
        result += ','
        # print(k, v)
        return HttpResponse("Get value of POST is {0}".format(result))

def render_test(request):
    #环境变量
    c = dict()
    # render返回的是一个HttpResponse的实例
    # 渲染模板 返回的就是模板 模板里就是网页
    response = render(request,"render.html")
    # response = HttpRequest(request,"render,html")
    return response

def render2_test(request):
    #环境变量
    d = dict()
    d["name"] = "ashenQAQ"
    # 上下文环境 d的值  来替换了模板里面的name这个变量
    response = render(request,"render2.html",context=d)
    return response

def render3_test(request):
    # 得到模板
    from django.template import  loader  #加载程序
    t = loader.get_template("render2.html")
    print(type(t))

    response = t.render({"name":"yipeng"})
    print(type(response))
    return HttpResponse(response)

def get404(request):
    from django.views import defaults
    return defaults.page_not_found(request,template_name="render.html")

def hello(request):
    response = render(request,"HelloOne.html")
    return response

def label(request):
    c = dict()
    c["score"] = [99,87,23,100,83,88]
    response = render(request,"label.html",context=c)
    return response

def ifww(request):
    c = dict()
    c["name"] = "ashen7"
    response = render(request, "ifww.html", context=c)
    return response

def csrf_get(request):
    return render(request,"csrf.html")

def csrf_post(request):
    print(request.POST)
    return render(request,"HelloOne.html")

def tanchishe(request):
    return render(request,'20行贪吃蛇.html')