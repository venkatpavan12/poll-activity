from django.shortcuts import render,redirect
# Create your views here.
from .models import User
from django.views import generic
from django.contrib.auth import login, logout,authenticate
from .forms import NewUserForm
from django.urls import reverse
from poll.models import Poll
def Register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not request.user.is_authenticated:
                login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect(reverse('home'))
    else:
        form = NewUserForm()
    return render(request, 'registration/register.html', {'form': form})
def Profile(request):
    queryset=Poll.objects.filter(createdby=request.user)
    return render(request,"profile.html",context={'polls':queryset})