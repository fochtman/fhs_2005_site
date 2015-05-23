from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import render_to_response

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
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

def register2(request):
    if request.method == 'POST':
        form = FHSUserRegistrationForm(request.POST)
        # after we validate the form data with .is_valid()
        # we can access the data via form.cleaned_data[<fieldname>]
        if form.is_valid():
            '''
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)

            is_married = form.cleaned_data['is_married']
            current_city = form.cleaned_data['current_city']
            current_state = form.cleaned_data['current_state']

            fhs_user = FHSUser(user=user, is_married=is_married, ticket_num=0, current_city=current_city, current_state=current_state)
            fhs_user.save()
            '''

            '''
            class FHSUser(models.Model):
            user = models.OneToOneField(User)
            is_married = models.BooleanField(default=False)
            ticket_num = models.IntegerField(default=0)
            current_city = models.CharField(max_length=50)
            current_state = models.CharField(max_length=50)
            '''
            messages.add_message(request, messages.SUCCESS, 'Your account was successfully created.')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'There was an error while creating account.')
            context = RequestContext(request, {'form': form})
            return render_to_response('register2.html', context)
    else:
        context = RequestContext(request, {'form': FHSUserRegistrationForm()})
        return render_to_response('register2.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR, 'There was an error while creating account.')
            context = RequestContext(request, {'form': form})
            return render_to_response('register.html', context)
        else:
            # take care of building user object first
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            '''
            is_married = models.BooleanField(default=False)
            ticket_num = models.IntegerField(default=0)
            current_city = models.CharField(max_length=50)
            current_state = models.CharField(max_length=50)
            '''


            messages.add_message(request, messages.SUCCESS, 'Your account was successfully created.')
            return HttpResponseRedirect('/')
    else:
        context = RequestContext(request,  {'form': RegistrationForm()})
        return render_to_response('register.html', context)

def sign_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(request.GET['next'])
                    else:
                        return HttpResponseRedirect('/')
                else:
                    messages.add_message(request, messages.ERROR, 'Your account is deactivated.')
                    context = RequestContext(request)
                    return render_to_response('sign_in.html', context)
            else:
                messages.add_message(request, messages.ERROR, 'Username or password invalid.')
                context = RequestContext(request)
                return render_to_response('sign_in.html', context)
        else:
            context = RequestContext(request)
            return render_to_response('sign_in.html', context)


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/')

'''
def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            #return a successful response
        else:
            # display some kind of error and try again
    else:
        # state that user doesn't exist
        # redirect to sign-up page

        # ...

def sign_out(request):
    logout(request)
'''

'''
def charge(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
'''

# eventually add product and cust. info returned in the form,
# which will require adding models


def charge(request):
    '''
    print 'values'
    print request.POST.values()
    print 'keys'
    print request.POST.keys()
    '''

    meta = {}

    num_tickets = 'Number of tickets'
    meta[num_tickets] = request.POST['tk0']

    num_ts0 = 'Number of ts0'
    meta[num_ts0] = int(request.POST['ts0'])

    if meta[num_ts0] > 0:
        tso_size = 'ts0_size'
        meta[tso_size] = request.POST[tso_size]

    amount = int(request.POST['oTotal']) * 100

    # print meta
    # customer=customer.id,
    # TODO: send email receipt

    token = request.POST['stripeToken']

    if amount > 0:
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description="Reunion Purchase",
                metadata=meta
            )
        except stripe.CardError, e:
            # the card has been declined
            # redisplay shopping page with js alert or something
            # return render(request, 'home/shop.html', {
            #   'error_msg' : ...
            # })
            pass
        else:
            # logs = {'ok': True}
            # url = reverse('notamember', kwargs={'classname': classname})
            # return HttpResponseRedirect(url)
            # url = reverse('home:shop', kwargs={'ok': True})
            # return HttpResponseRedirect(url)
            # return render(request, 'home:shop', logs)
            # return render(reverse('home:success', logs))

            return HttpResponseRedirect(reverse('home:success'))

