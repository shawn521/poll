from django.shortcuts import render
from django.views.generic import ListView,DetailView,RedirectView
from .models import *
class PollList(ListView):
    model = Poll
class PollDetail(DetailView):
    model=Poll
    def get_comtext_data(self,**kwargs):
        context=super().get_cintext_data(**kwargs)
        option=Option.object.fillter(poll_id=self.kwargs['pk'])
        context['options']=options
        return context


class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id=self.kwargs['pk'])
        option.count += 1   
        option.save()     
        return "/poll/"+str(option.poll_id)+"/"

       