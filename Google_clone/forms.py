from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from . import models


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250, widget=forms.EmailInput(
        attrs={'class': 'email', 'placeholder': 'Enter your dummy email...', 'name': 'email'}), label=False, required=True)
    first_name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'name': 'first_name'}), label=False, required=True)
    last_name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name', 'name': 'last_name'}), label=False, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


class ProfileForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request')
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['residential_address'].initial = self.request.user.profile.residential_address
    #     self.fields['date_of_birth'].initial = self.request.user.profile.date_of_birth
    #     self.fields['photo'].initial = self.request.user.profile.photo
    #     self.fields['state_of_origin'].initial = self.request.user.profile.state_of_origin
    #     self.fields['favorite_food'].initial = self.request.user.profile.favorite_food
    #     self.fields['about'].initial = self.request.user.profile.about
    residential_address = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={'class': 'edits', 'name': 'address'}), required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'edits', 'name': 'birthday', 'type': 'date'}))
    photo = forms.FileField(widget=forms.FileInput(
        attrs={'name': 'photo'}), required=False)
    state_of_origin = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'edits', 'name': 'state_of_origin'}), required=False)
    favorite_food = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'edits', 'name': 'favorite_food'}), required=False)
    about = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'about_me', 'Placeholder': 'More about yourself...', 'name': 'about'}), label=False)

    class Meta:
        model = models.Profile
        fields = ['photo', 'date_of_birth', 'residential_address',
                  'state_of_origin', 'favorite_food', 'about']

# THE CODE BELOW SHOULD BE IMPLEMENTED WHEN A CLASS BASED VIEW IS USED
    # def save(self, commit=True):
    #     prof = super(ProfileForm, self).save(commit=False)
    #     prof.photo = self.cleaned_data['photo']
    #     prof.date_of_birth = self.cleaned_data['date_of_birth']
    #     prof.residential_address = self.cleaned_data['residential_address']
    #     prof.state_of_origin = self.cleaned_data['state_of_origin']
    #     prof.favorite_food = self.cleaned_data['favorite_food']
    #     prof.about = self.cleaned_data['about']

    #     if commit:
    #         prof.save()

    #     return prof


class EditProfileForm(UserChangeForm):
    username = forms.CharField(
        max_length=250, widget=forms.TextInput(attrs={'class': 'edits', 'name': 'username'}))
    email = forms.EmailField(max_length=250, widget=forms.EmailInput(
        attrs={'class': 'edits', 'name': 'email'}), required=True)
    first_name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': 'edits', 'name': 'first_name'}), required=True)
    last_name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': 'edits', 'name': 'last_name'}), required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')

    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']

    #     if commit:
    #         user.save()

    #     return user


class ChangeUserPasswordForm(PasswordChangeForm):
    # ['old_password', 'new_password1', 'new_password2']
    # old_password = forms.CharField(strip=False, widget=forms.PasswordInput(
    #     attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'passwrd_inputs', 'name': 'old_password'}),)
    # new_password1 = forms.CharField(strip=False, widget=forms.PasswordInput(
    #     attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'passwrd_inputs', 'name': 'new_password1'}),)
    # new_password2 = forms.CharField(strip=False, widget=forms.PasswordInput(
    #     attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'passwrd_inputs', 'name': 'new_password2'}),)

    class Meta:
        model = User
        fields = '__all__'
