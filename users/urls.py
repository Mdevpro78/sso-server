from django.urls import path
from django.contrib.auth.views import LoginView


from .views import SignupView


app_name = 'users'


urlpatterns = [

	path('signup/', SignupView.as_view(), name='singup'),
	path('login/', LoginView.as_view(), name='login'),
]
