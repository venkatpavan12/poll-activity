from django.urls import reverse
from django.shortcuts import render,redirect

from .models import Poll,Answers
from core.models import User
from django.views import generic
from django.db.models import F
# Create your views here.
def Homepage(request):
    queryset=Poll.objects.all()
    return render(request,"homepage.html",context={'polls':queryset})

class CreatePoll(generic.CreateView):
    model=Poll
    template_name="create_poll.html"
    fields=['question','option1','option2','option3','option4']
    def form_valid(self,form):

        poll = form.save(commit=False)
        user=self.request.user
        poll.createdby=user
        user.noPolls+=1
        user.save()
        poll.save()
        return redirect(reverse('home'))

def PollDetail(request,id):
    if request.method=='POST':
        poll=Poll.objects.filter(id=int(request.POST.get('pollid'))).first()
        option=request.POST.get('option')
        user=request.user
        Answers.objects.create(user=user,poll=poll,option=option)
        return redirect(reverse('home'))
    else:
        poll=Poll.objects.filter(id=id).first()
        return render(request,"poll.html",context={'poll':poll})
