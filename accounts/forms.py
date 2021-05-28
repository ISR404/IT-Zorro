from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
 )

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Этот пользователь не существует!")

            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль!")

            if not user.is_active:
                raise forms.ValidationError("Этот пользователь больше не активен")
        return super(UserLoginForm, self).  clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2'
        ]


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают!")
        return password