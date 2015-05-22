from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def is_username_forbidden(value):
    forbidden_usernames = ['admin', 'settings', 'news', 'about', 'help', 'signin', 'signup',
        'signout', 'terms', 'privacy', 'cookie', 'new', 'login', 'logout', 'administrator',
        'join', 'account', 'username', 'root', 'blog', 'user', 'users', 'billing', 'subscribe',
        'reviews', 'review', 'blog', 'blogs', 'edit', 'mail', 'email', 'home', 'job', 'jobs',
        'contribute', 'newsletter', 'shop', 'profile', 'register', 'auth', 'authentication',
        'campaign', 'config', 'delete', 'remove', 'forum', 'forums', 'download', 'downloads',
        'contact', 'blogs', 'feed', 'faq', 'intranet', 'log', 'registration', 'search',
        'explore', 'rss', 'support', 'status', 'static', 'media', 'setting', 'css', 'js',
        'follow', 'activity']
    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')

def is_username_invalid(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Enter a valid username.')

def is_email_unique(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('That email is taken.')

def is_username_unique(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('That name is taken.')

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm your password.")
    email = forms.CharField(required=True)

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(is_username_forbidden)
        self.fields['username'].validators.append(is_username_invalid)
        self.fields['username'].validators.append(is_email_unique)
        self.fields['email'].validators.append(is_username_unique)

    def clean(self):
        super(RegistrationForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(['The passwords do not match.'])
        return self.cleaned_data
