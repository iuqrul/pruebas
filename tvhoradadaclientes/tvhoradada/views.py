#encoding:utf-8
from django.views.generic import TemplateView, FormView
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = "/"
    initial = {
        'username': '',
        'password': ''
    }

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            auth_login(request, form.get_user())
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(TemplateView):

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect('/login')


class IndexView(TemplateView):
    template_name = 'index.html'
