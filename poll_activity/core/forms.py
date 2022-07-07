from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Create your forms here.
User=get_user_model()
class NewUserForm(UserCreationForm):
	phone=forms.CharField()

	class Meta:
		model = User
		fields=['username','first_name','last_name','email','phone']