from django.conf.urls import include, url
from django.contrib import admin

from ashen import views as tv
from ashen import ashenApp_urls
# 这个就是django的主路由
urlpatterns = [
    # Examples:
    # url(r'^$', 'ashen7_dj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 视图函数名称只有名称 没有括号没有参数
    # 用re匹配这个URL字符串  从上往下匹配 找到符合这个re请求的字符串URL 就用相应的函数去处理他
    url(r'^admin/', include(admin.site.urls)),

    # 比如约定 凡是由ashen 这个app模块处理的视图的url 都以ashen开头
    # 凡是以ashen开头的字符串URL 直接导入ashen里面的子路由 来处理
    url(r'^ashen/',include(ashenApp_urls)),

    url(r'^web/(?:page=(?P<pn>\d+)/)$',tv.do_param2),
    url(r'^myname/$',tv.exam,{"name":"ashen"}),

    # 这个name 是给这个URL起的一个名字 可以通过这个名字来修改他
    url(r'^yourname/$',tv.myname,name="ask my name"),
    url(r"^v2_exp",tv.v2_exception),

    url(r'^v10',tv.v10),
    url(r'^v11_hello',tv.v11,name="v11_name"),
    url(r'^v12_world',tv.v12,name="v12_name"),

    url(r'^req',tv.req_get),
    url(r'^form_get',tv.form_get),
    url(r'^form_post',tv.form_post),

    url(r'^render/',tv.render_test),
    url(r'^render2',tv.render2_test),
    url(r'^render3',tv.render3_test),
    url(r'^getexp',tv.get404),
    url(r'^hello',tv.hello),
    url(r'^label',tv.label),
    url(r'^ifww',tv.ifww),
    url(r'^csrf_get',tv.csrf_get),
    url(r"^csrf_post",tv.csrf_post),
    url(r'^game/',tv.tanchishe),

]
