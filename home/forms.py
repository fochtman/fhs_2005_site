from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

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
    email           = forms.EmailField(label="EMAIL", validators=valid_email)
    password0       = forms.CharField(widget=forms.PasswordInput(), label="PASSWORD")
    password1       = forms.CharField(widget=forms.PasswordInput(), label="CONFIRM PASSWORD")
    is_married      = forms.ChoiceField(label="HITCHED?", choices=[(0, 'NO'), (1, 'YES')])
    num_kids        = forms.ChoiceField(label="HOW MANY KIDS DO YOU HAVE?", choices=[(x, x) for x in range(11)])
    profession      = forms.CharField(label="PROFESSION")
    current_city    = forms.CharField(label="CITY")
    current_state   = forms.CharField(label="STATE")
    #ticket_num = models.IntegerField(default=0)


'''
class FHSUserSignInForm(forms.Form):
    import sys
    print >> sys.stderr, 'In user sign-in'

    username = forms.EmailField(label="USERNAME/EMAIL", validators=valid_email)
    password = forms.CharField(widget=forms.PasswordInput(), label="PASSWORD")
'''
