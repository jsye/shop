"""
this is user models
                    --by zero

"""
from django.core import validators
from django.db import models


class Usermodel(models.Model):
    sex_list = ((1, '男'),
                (2, '女'),
                (3, '保密'))
    name = models.CharField(max_length=20, editable=True, help_text="请输入用户名",
                            unique=True, verbose_name="妮称")

    mobile = models.CharField(max_length=11,
                              help_text="请输入手机号码",
                              validators=[
                                  validators.RegexValidator(r'^1[3-9]\d{9}$',"手机号码格式错误")
                              ],
                              verbose_name="手机号码",
                              null=True,
                              blank=True)

    password = models.CharField(max_length=16, verbose_name='密码',
                                validators=[
                                    validators.MinLengthValidator(8)
                                ])

    sex = models.IntegerField(choices=sex_list, default=3, verbose_name='性别')

    school = models.CharField(max_length=100, verbose_name='学校', null=True, blank=True,
                              editable=True, help_text="请输入学校地址")

    address = models.CharField(max_length=200, verbose_name='地址', editable=True, help_text="地址",
                               null=True, blank=True)

    add_date = models.DateTimeField(verbose_name='添加时间', null=True, blank=True)

    update_date = models.DateTimeField(verbose_name='修改时间', null=True, blank=True)

    delete = models.BooleanField(default=False, verbose_name='删除')

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name
