from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings

def is_name_forbidden(value):
    forbidden_names = ['admin', 'settings', 'news', 'about', 'help', 'signin', 'signup',
        'signout', 'terms', 'privacy', 'cookie', 'new', 'login', 'logout', 'administrator',
        'join', 'account', 'username', 'root', 'blog', 'user', 'users', 'billing', 'subscribe',
        'reviews', 'review', 'blog', 'blogs', 'edit', 'mail', 'email', 'home', 'job', 'jobs',
        'contribute', 'newsletter', 'shop', 'profile', 'register', 'auth', 'authentication',
        'campaign', 'config', 'delete', 'remove', 'forum', 'forums', 'download', 'downloads',
        'contact', 'blogs', 'feed', 'faq', 'intranet', 'log', 'registration', 'search',
        'explore', 'rss', 'support', 'status', 'static', 'media', 'setting', 'css', 'js',
        'follow', 'activity']
    if value.lower() in forbidden_names:
        raise ValidationError('This is a reserved word.')

def is_name_invalid(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Enter a valid username.')

def is_email_unique(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('That email is taken.')

def is_username_unique(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('That name is taken.')

def is_bulldog_id(value):
    if value != settings.BULL_DOG_ID:
        raise ValidationError('Incorrect ID.')

class FHSUserRegistrationForm(forms.Form):
    valid_name = [is_name_forbidden, is_name_invalid]
    valid_email = [is_email_unique]
    yes_no = [(True, 'yes'), (False, 'no')]

    def clean(self):
        password1 = self.cleaned_data.get('password0')
        password2 = self.cleaned_data.get('password1')
        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

    first_name      = forms.CharField(label="FIRST NAME", validators=valid_name)
    last_name       = forms.CharField(label="LAST NAME", validators=valid_name)
    maiden_name     = forms.CharField(label="MAIDEN NAME", validators=valid_name)
    email           = forms.EmailField(label="EMAIL", validators=valid_email)
    password0       = forms.CharField(widget=forms.PasswordInput(), label="PASSWORD")
    password1       = forms.CharField(widget=forms.PasswordInput(), label="CONFIRM PASSWORD")
    is_married      = forms.ChoiceField(label="HITCHED?", choices=[(0, 'NO'), (1, 'YES')])
    num_kids        = forms.ChoiceField(label="HOW MANY KIDS DO YOU HAVE?", choices=[(x, x) for x in range(11)])
    profession      = forms.CharField(label="PROFESSION", min_length=3, validators=[is_name_invalid])
    current_city    = forms.CharField(label="CITY", min_length=2, validators=[is_name_invalid])
    current_state   = forms.CharField(label="STATE", min_length=2, validators=[is_name_invalid])
    #verification    = forms.CharField(label="BULL DOG ID", min_length=10, max_length=10, validators=[is_bulldog_id])


from django.contrib.auth import authenticate

class FHSUserLoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid username or password.")
        return self.cleaned_data

    def fhs_user_login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class ImageForm(forms.Form):
    image = forms.ImageField('UPLOAD IMAGE')
