from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.backends import AllowAllUsersModelBackend


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            backend = AllowAllUsersModelBackend()
            self.user_cache = backend.authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "Please confirm your email so you can log in.",
                code='inactive',
            )


class LoginViewSet(LoginView):
    authentication_form = LoginForm
    template_name = 'dashboard/accounts/login.html'

    def form_valid(self, form):
        return super().form_valid(form) 

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
    
    def get_success_url_allowed_hosts(self):
        return super().get_success_url_allowed_hosts()