from django import forms
from django.contrib.auth.models import User
from .models import Profile, Statistic, Trophy

class UserRegistrationForm(forms.ModelForm):
    """Регистрация пользователя"""
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        """Проверка пароля"""
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    """Форма логина"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    """Изменение своих данных, хранящихся во встроенной пользовательской модели."""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    """Редактирование доп.данных"""
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo', 'gender', 'relationship', 'fish_sum', 'fish_kg','karas','sazan','lech','other_fish')


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ('place', 'date', 'description', 'fish_name', 'fish_sum', 'fish_kg', 'vodka', 'beer', 'prikorm')

class TrophyForm(forms.ModelForm):
    class Meta:
        model = Trophy
        fields = ('name', 'description', 'phase')


class CommentForm(forms.Form):
    your_name = forms.CharField(max_length=20)
    comment_text = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"

class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)
