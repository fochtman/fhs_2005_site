from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

import stripe


class HomeView(TemplateView):
    template_name = "home.html"


class EventsView(TemplateView):
    template_name = "events.html"


class ShopView(TemplateView):
    template_name = "shop.html"


class ConnectView(TemplateView):
    template_name = "connect.html"


class SponsorsView(TemplateView):
    template_name = "sponsors.html"


class SuccessView(TemplateView):
    template_name = "success.html"

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

