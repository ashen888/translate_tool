from django.contrib import admin

# Register your models here. auth是身份验证
from .models import Grade,Students

# student加两行  overrides 覆盖 就是重写方法 重写属性
class StudentsInfo(admin.TabularInline):  #StackedInline 表格和堆放
    model = Students
    extra = 2

# 注册
# 这个admin里面的modeladmin类是默认管理页面  然后我要自定义管理页面
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    # student加两行
    inlines = [StudentsInfo]
    # 列表页属性
    list_display = ['pk','name','date','girl_num','boy_num','isDelete'] #显示的字段
    list_filter = ['name']  #过滤器 过滤字段
    search_fields = ['id']  #搜索字段
    list_per_page = 5   #分页字段

    # 添加 修改页属性
    # fields = ['girl_num','boy_num','name','date','isDelete']   #规定属性的先后顺序
    # 里面每一个元素是一个元祖 元祖里第一个元素是一个分组名 第二个是字典 给他分了个顺序
    fieldsets = [("num",{"fields":['girl_num','boy_num']}),
                 ('base',{'fields':['name','date','isDelete']}),
                 ]    #给属性分组 这两个东西不能同时使用

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.gender:
            return '男'
        else:
            return '女'

    def isDelete(self):
        if not self.isDelete:  #如果不是空
            return '存在'
        else:
            return '已删'
        #设置页面列的名称
    gender.short_description = '性别'
    list_display = ['pk','name','age',gender,'introduce','grade',isDelete]
    list_filter = ['age']
    search_fields = ['id']
    list_per_page = 5

    #执行动作的位置
    actions_on_bottom = True
    actions_on_top = False
# admin.site.register(Grade,GradeAdmin)
# admin.site.register(Students,StudentsAdmin)

from .models import Text
admin.site.register(Text)