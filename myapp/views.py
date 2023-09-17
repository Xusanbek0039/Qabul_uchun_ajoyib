
from django.shortcuts import render
from django.views.generic import TemplateView



# TemplateView bu teplatesni korsat degani name esa htmlga yoldur 
class HomePageView(TemplateView):
    template_name = 'index.html'


class ContacView(TemplateView):
    template_name = 'contact.html'


class Loginview(TemplateView):
    template_name = 'login.html'


class ErrorView(TemplateView):
    template_name = '404.html'


class PasresertView(TemplateView):
    template_name = 'password-reset.html'


class Registerview(TemplateView):
    template_name='register.html'

class SoatView(TemplateView):
    template_name='soat.html'