from django.db import models
#模型类要继承models.Model类
# Create your models here.

# 1对多  外键写在多那里
# 不需要定义主键 主键会在生成时自动生成 并且值为自动增加

class Grade(models.Model):
    # 类名对应一个数据表 类属性对应一个数据表中的字段
    name = models.CharField(max_length=20)
    date = models.DateField()
    girl_num = models.IntegerField()
    boy_num = models.IntegerField()
    # 这里面只有 True 和 False 没有none
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s' % (self.name)
    class Meta():
        db_table = 'grade'
        ordering = ['id']
    # 自定义模型管理器
    obj = models.Manager()

# 自定义管理器Manager
class StudentsManager(models.Manager):
    def get_queryset(self):
        # 原始查询集 过滤出没有被删除的数据
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)

    # 在管理器添加学生信息
    def createStudents(self,name,age,gender,introduce,grade,isDelete=False):
        # 获得一个模型类对象 这里是students类对象
        s = self.model()
        s.name = name
        s.age = age
        s.gender = gender
        s.introduce = introduce
        s.grade = grade
        return s

class Students(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    age = models.IntegerField()
    introduce = models.CharField(max_length=20)
    # 这个是设置为 关联外键
    grade = models.ForeignKey("Grade")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s===>>%s' % (self.name,self.grade)
    class Meta():
        db_table = 'students'  #设置数据表名
        ordering = ['id']  #根据id排序 默认升序 -就是降序
    # 自定义模型管理器
    obj = models.Manager()
    obj2 = StudentsManager()

    # 定义一个类方法创建对象
    @classmethod
    def createStudents(cls,name,age,gender,introduce,grade,isDelete=False):
        # cls表示本身这个类 就是学生类
        s = cls(name=name,age=age,gender=gender,introduce=introduce,grade=grade)
        # 返回创建的对象
        return s

    def getAttr(self):
        return str(self.age) + '==>>' + str(self.introduce) + '==>>' + str(self.grade)

from tinymce.models import HTMLField
class Text(models.Model):
    s = HTMLField()

