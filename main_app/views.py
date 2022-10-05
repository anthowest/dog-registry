from ast import Add
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Dog, History, Size
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sizes"] = Size.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"


class DogList(TemplateView):
    template_name = "dog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["dogs"] = Dog.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["dogs"] = Dog.objects.all()
            context["header"] = "Trending Dogs" 
        return context


class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'hypoallergenic']
    template_name = "dog_create.html"
    def get_succuss_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})


class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"


class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'hypoallergenic']
    template_name = "dog_update.html"
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})


class DogDelete(DeleteView):
    model = Dog 
    template_name = "dog_delete_confirmation.html"
    success_url = "/dogs/"

class HistoryCreate(View):
    def post(self, request, pk):
        nationality = request.POST.get("nationality")
        year_recognized = request.POST.get("year_recognized")
        dog = Dog.objects.get(pk=pk)
        History.objects.create(nationality=nationality, year_recognized=year_recognized, dog=dog)
        return redirect('dog_detail', pk=pk)