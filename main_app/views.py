from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Dog:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

dogs = [
    Dog("English Bulldog", "https://media.cnn.com/api/v1/images/stellar/prod/220615105053-unhealthy-english-bulldogs.jpg", "The Bulldog is a British breed of dog of mastiff type. It may also be known as the English Bulldog or British Bulldog. It is of medium size, a muscular, hefty dog with a wrinkled face and a distinctive pushed-in nose."),
    Dog("French Bulldog", "https://cdn.britannica.com/44/233844-050-A0F9F39C/French-bulldog.jpg", "The French Bulldog, French: Bouledogue Français, is a French breed of companion dog or toy dog. It appeared in Paris in the mid-nineteenth century, apparently the result of cross-breeding of Toy Bulldogs imported from England and local Parisian ratters."),
    Dog("Boxer", "https://media-be.chewy.com/wp-content/uploads/2021/04/16140537/Boxer_Feature-Image-1024x615.jpg", "The Boxer is a medium to large, short-haired dog breed of mastiff-type, developed in Germany. The coat is smooth and tight-fitting; colors are fawn, brindled, or white, with or without white markings."),
]

class DogList(TemplateView):
    template_name = "dog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dogs"] = dogs 
        return context