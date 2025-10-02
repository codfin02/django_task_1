from django.contrib.auth import get_user_model, login
from django.core import signing
from django.core.signing import TimestampSigner, SignatureExpired
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from users.forms import SignupForm, LoginForm
from utils.email import send_email

User = get_user_model()


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save()
        signer = TimestampSigner()
        signed_user_email = signer.sign(user.email)
        signer_dump = signing.dumps(signed_user_email)

        host = self.request.get_host() or 'testserver'
        url = f"{self.request.scheme}://{host}/users/verify/?code={signer_dump}"
        subject = f"[Pystagram] {user.email}님의 이메일 인증 링크입니다."
        message = f"""
아래의 링크를 클릭하여 이메일 인증을 완료해주세요.

{url}
"""
        send_email(subject=subject, message=message, from_email=None, to_email=user.email)

        return render(self.request, 'registration/signup_done.html', {'user': user})


def verify_email(request):
    code = request.GET.get('code', '')
    signer = TimestampSigner()
    try:
        decoded_user_email = signing.loads(code)
        user_email = signer.unsign(decoded_user_email, max_age=60 * 5)
    except (TypeError, SignatureExpired):
        return render(request, 'registration/verify_failed.html')

    user = get_object_or_404(User, email=user_email)
    user.is_active = True
    user.save()
    return render(request, 'registration/verify_success.html')


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user=user)
        return HttpResponseRedirect(self.get_success_url())
