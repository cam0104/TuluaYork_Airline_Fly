from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render
from django.views.generic import RedirectView, TemplateView
from .forms import UserCreateForm


class singinView(TemplateView):
    template_name = 'login.html'



def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('Index')
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})


class LogoutView(RedirectView):
    pattern_name = 'Index'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


