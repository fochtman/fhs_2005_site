from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from forms import *
from models import FHSUser
import stripe


class HomeView(TemplateView):
    template_name = "home.html"


class EventsView(TemplateView):
    template_name = "events.html"


class ShopView(TemplateView):
    template_name = "shop.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShopView, self).dispatch(*args, **kwargs)


class ConnectView(TemplateView):
    template_name = "connect.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ConnectView, self).dispatch(*args, **kwargs)


class SponsorsView(TemplateView):
    template_name = "sponsors.html"


class SuccessView(TemplateView):
    template_name = "success.html"

class DeclineView(TemplateView):
    template_name = "decline.html"

def register_render(request, form0):
    context = RequestContext(request, {'form': form0})
    return render_to_response('register.html', context)

def register(request):
    if request.method == 'POST':
        form = FHSUserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password0']
            username = email
            is_married = True if form.cleaned_data['is_married'] == 'YES' else False
            num_kids = int(form.cleaned_data['num_kids'])
            profession = form.cleaned_data['profession']
            current_city = form.cleaned_data['current_city']
            current_state = form.cleaned_data['current_state']

            User.objects.create_user(first_name=first_name,
                                     last_name=last_name,
                                     username=username,
                                     password=password,
                                     email=email)

            user = authenticate(username=username, password=password)
            login(request, user)

            fhs_user = FHSUser(user=user,
                               is_married=is_married,
                               num_kids=num_kids,
                               profession=profession,
                               num_ticket=0,
                               current_city=current_city,
                               current_state=current_state)
            fhs_user.save()

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect('/')
        else:
            return register_render(request, form)
    else:
        return register_render(request, FHSUserRegistrationForm())


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def charge(request):
    user = request.user
    if user.is_authenticated():
        fhs_user = FHSUser.objects.get(pk=user)
        amount = int(request.POST['oTotal']) * 100
        token = request.POST['stripeToken']
        if amount > 0:
            try:
                charge = stripe.Charge.create(
                    amount=amount,
                    currency='usd',
                    source=token,
                    description="Reunion Ticket",
                    receipt_email=fhs_user.user.email,
                )
                fhs_user.num_ticket += 1
                fhs_user.save()
                # TODO: send email receipt
            except stripe.CardError, e:
                return HttpResponseRedirect(reverse('home:decline'))
            else:
                return HttpResponseRedirect(reverse('home:success'))
        else:
            # amount to charge <= 0
            # return HttpResponseRedirect()
            return HttpResponseRedirect(reverse('home:decline'))


