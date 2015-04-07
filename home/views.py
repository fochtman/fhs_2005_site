from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class ShopView(TemplateView):
    template_name = "shop.html"
