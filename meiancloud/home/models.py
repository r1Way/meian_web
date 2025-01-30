from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='用户')#包含基础的User，如用户名和密码

    email = models.EmailField('邮箱',max_length=254,unique=True,blank=True,null=True,default='')
    nike_name = models.CharField('昵称',max_length=20,blank=True,default='')#昵称
    # USER_GENDER_TYPE=(
    #     ('0','请选择'),('male','男'),('female','女'),('others','其他'),)
    # gender=models.CharField('性别',max_length=8,choices=USER_GENDER_TYPE,default='0')
    birthday=models.DateField('生日',null=True,blank=True)
    prof=models.TextField('个人简介',max_length=200,blank=True,default='')#个人简介
    image=models.ImageField(verbose_name='头像',upload_to='user_img/%Y/%m',default='user_img/default.png',max_length=100,)

class Comment(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='comment_user')  # 修改这里
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title