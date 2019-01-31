from django.db import models

# Create your models here.
class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)
    # 系统默认给加的  teacher_set 这个是关系 teacher_set.all()
    #my_manager = models.OneToOneField("Manager")


    # 这个是类里面的特殊函数 也叫魔法函数 实现的是 一实例化类就出现名字
    def __str__(self):
        return self.school_name

class Manager(models.Model):
    manager_id = models.IntegerField()
    manager_name = models.CharField(max_length=20)

    my_school = models.OneToOneField("School")  #一对一

    def __str__(self):
        return self.manager_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    my_school = models.ForeignKey("School")  #一对多

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    teachers = models.ManyToManyField("Teacher")   #多对多
