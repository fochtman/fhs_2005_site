from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
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

    amnt = 100000

    # customer=customer.id,
    # TODO: send email receipt

    token = request.POST['stripeToken']

    try:
        charge = stripe.Charge.create(
            amount=amnt,
            currency='usd',
            source=token,
            description="Reunion Ticket"
        )
    except stripe.CardError, e:
        # the card has been declined
        # redisplay shopping page with js alert or something
        # return render(request, 'home/shop.html', {
        #   'error_msg' : ...
        # })
        pass
    else:
        return HttpResponseRedirect(reverse('home:shop'))

