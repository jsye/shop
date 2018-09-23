"""
this is user App model forms
                            --by zero
"""
from django import forms

from user.helper import set_password
from user.models import Usermodel


# 注册验证表单
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Usermodel
        fields = ['mobile', 'password']

        # 使用Django的表单对前端表单的重写  注：widgets 一定要在class Meta里面
        widgets = {
            "mobile": forms.TextInput(attrs={"class": "login-name", "placeholder": "请输入手机号"}),
            "password": forms.PasswordInput(attrs={"class": "login-password", "placeholder": "请输入密码"})
        }

        # 自定义错误信息
        error_messages = {
            "mobile": {
                'required': "手机号码必填！"
            },
            "password": {
                'required': "请填写密码！",
                'min_length': '密码至少为8位！'
            }
        }

    # 验证手机号码是否已被注册（单个字段的校验）
    def clean_mobile(self):
        # 获取提交的手机号码
        mobile = self.cleaned_data.get('mobile')

        # 从数据库中查找
        res = Usermodel.objects.filter(mobile=mobile).exists()
        if res:
            raise forms.ValidationError("该手机号码已经被注册！")
        return mobile

    # 新建一个字段验证两次密码是否正确

    repassword = forms.CharField(max_length=16, min_length=6,
                                 error_messages={
                                     "required": "请填写确认密码！"
                                 },

                                 widget=forms.PasswordInput(
                                     attrs={"class": "login-password", "placeholder": "请输入确认密码"}))

    # 综合验证
    def clean(self):
        # 所有清洗后的数据
        clean_data = super().clean()
        pwd1 = clean_data.get('password')
        pwd2 = clean_data.get('repassword')
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise forms.ValidationError({"repassword": '两次密码不一至！'})
        else:
            # 密码一致，则对密码进行加密
            clean_data['password'] = set_password(pwd1)
        # 返回清洗后的数据
        return clean_data


# 登录表单
class LoginForm(forms.ModelForm):
    # 登录form
    class Meta:
        model = Usermodel
        fields = ['mobile', 'password']

        # 使用Django的表单对前端表单的重写  注：widgets 一定要在class Meta里面
        widgets = {
            "mobile": forms.TextInput(attrs={"class": "login-name", 'placeholder': '请输入用户名/手机号'}),
            "password": forms.PasswordInput(attrs={"class": "login-password", 'placeholder': '请输入密码'})
        }

        # 自定义错误信息
        error_messages = {
            "mobile": {
                "required": '这个字段必填！'
            },
            "password": {
                "required": '这个字段必填！'
            }
        }

    def clean(self):
        clean_data = super().clean()
        # 获取用户输入的数据
        phone = clean_data.get('mobile')
        pwds = clean_data.get('password', '')
        # 通过手机号码查询数据，如果存在再验证密码 ，如果不存在则直接报错
        user = Usermodel.objects.filter(mobile=phone).first()
        if user is None:
            raise forms.ValidationError({"phone": "该手机号码没有注册！"})
        else:
            # 手机号码存在，验证密码是否正解
            password_in_db = user.password  # 数据库中已加密的密码
            passwd = set_password(pwds)
            if password_in_db != passwd:
                raise forms.ValidationError({"password": "密码错误！"})
            else:
                # 密码验证成功，返回clean_data 并顺便将上面查询出来的user对象带回到login view中
                clean_data['user'] = user
                return clean_data


# 个人中心表单
class InfoForm(forms.ModelForm):
    class Meta:
        model = Usermodel
        fields = ['name', 'mobile', 'sex', 'bthday', 'school', 'address', 'fromshome']

        # 使用django自带的表单对前台的表单替换
        widgets = {
            "name": forms.TextInput(attrs={"class": "infor-tele", 'placeholder': '默契'}),
            "bthday": forms.TextInput(attrs={"class": "infor-tele", 'placeholder': '生日'}),
            "school": forms.TextInput(attrs={"class": "infor-tele", 'placeholder': '就读于哪个学校'}),
            "address": forms.TextInput(attrs={"class": "infor-tele", 'placeholder': '详细地址'}),
            "fromshome": forms.TextInput(attrs={"class": "infor-tele", 'placeholder': '来自哪里'}),
        }
