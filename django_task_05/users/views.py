from django.conf import settings
from django.contrib.auth import login as django_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        django_login(request, form.get_user())
        # next 지원
        nxt = request.GET.get('next')
        if nxt:
            return redirect(nxt)
        return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'registration/login.html', {'form': form})

