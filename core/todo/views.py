from django.shortcuts import render
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from .models import TodoModel
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Profile
from django.shortcuts import get_object_or_404

class IndexView(LoginRequiredMixin,ListView):
    model = TodoModel
    fields = ['title','text','complete','category']

    template_name = 'todo/index.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return TodoModel.objects.filter(author__user=self.request.user)
    


class IndexCreated(LoginRequiredMixin,CreateView):
    template_name = 'todo/todo_form.html'
    model = TodoModel
    fields = ['title','text','complete','category']
    success_url = '/todo/'
    
    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

class IndexUpdate(LoginRequiredMixin,UpdateView):
    model=TodoModel
    fields =['title','text','complete','category']
    template_name='todo/todo_form.html'
    success_url = '/todo/'

class IndexDelete(LoginRequiredMixin,DeleteView):
    model = TodoModel
    template_name = 'todo/todo_confirm_delete.html'
    success_url = '/todo/'
    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return TodoModel.objects.filter(author=profile)