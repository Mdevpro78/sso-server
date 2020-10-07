from django.views.generic import CreateView
from django.urls import reverse_lazy


from .forms import SignupForm


class SignupView(CreateView):
	form_class = SignupForm
	success_url = reverse_lazy('login')
	template_name = 'users/registeraion/signup.html'

