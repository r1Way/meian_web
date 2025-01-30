from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(label='用户', max_length=32,widget=forms.TextInput(
        attrs={'class':'input','placeholder':'用户名'}
    ))#第一个参数是label，第二个参数是最大长度
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(
        attrs={'class':'input','placeholder':'密码'}
    ))#第三个参数用来非明文输入

    #调用view.py中使用is_valid()时会调用clean_<field_name>方法，如果验证成功，返回cleaned_data字典，否则返回None
    def clean_password(self):#验证密码
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username ==password:
            raise  forms.ValidationError('用户名和密码不能相同!')
        return password


class RegisterForm(forms.ModelForm):

    username = forms.CharField(label='用户', min_length=6, widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': '用户名'}
    ))
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': '密码'}
    ))
    password1 = forms.CharField(label='再次输入密码', min_length=6, widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': '再次输入密码'}
    ))
    class Meta:
        model= User
        fields = ['username','password']

    def clean_username(self):
        #验证用户名是否存在
        usernameGet = self.cleaned_data.get('username')
        exsits= User.objects.filter(username=usernameGet).exists()#判断用户名是否存在
        if exsits:
            raise forms.ValidationError('用户名已存在')
        return usernameGet

    # 验证两次密码是否一致
    def clean_password1(self):
        passwordGet = self.cleaned_data.get('password')
        password1Get = self.cleaned_data.get('password1')
        print('passwordGet:',passwordGet)
        print('password1Get:',password1Get)
        if passwordGet != password1Get:  # 判断两次密码是否相同
            raise forms.ValidationError('两次密码不一致')
        return  password1Get