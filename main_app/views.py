from ast import Add
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Dog, History, Size
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sizes"] = Size.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"


@method_decorator(login_required, name='dispatch')
class DogList(TemplateView):
    template_name = "dog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["dogs"] = Dog.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["dogs"] = Dog.objects.filter(user=self.request.user)
            context["header"] = "Trending Dogs" 
        return context


class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'hypoallergenic']
    template_name = "dog_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DogCreate, self).form_valid(form)

    def get_succuss_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})


class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sizes"] = Size.objects.all()
        return context


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


class SizeDogAssoc(View):
    def get(self, request, pk, dog_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Size.objects.get(pk=pk).dogs.remove(dog_pk)
        if assoc =="add":
            Size.objects.get(pk=pk).dogs.add(dog_pk)
        return redirect('home')


class Signup(View):

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dog_list")
        else: 
            context = {"form": form}
            return render(request, "registration/signup.html", context)