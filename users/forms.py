from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginModelForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')


class SignupModelForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
