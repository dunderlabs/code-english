from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

from codeandenglish.users.models import User, Interest


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        m = super().save(commit=False)
        m.set_password(self.cleaned_data.get('password'))

        if commit:
            m.save()

        return m


class UserLoginForm(AuthenticationForm):
    pass


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['full_name', 'country']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})


class InterestForm(forms.ModelForm):

    class Meta:
        model = Interest
        fields = ['subject', 'iam', 'level']

    def __init__(self, *args, **kwargs):
        super(InterestForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['iam'].widget.attrs.update({'class': 'form-control'})
        self.fields['level'].widget.attrs.update({'class': 'form-control'})
