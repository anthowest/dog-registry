from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('dogs/', views.DogList.as_view(), name="dog_list"),
    path('dogs/new', views.DogCreate.as_view(), name="dog_create"),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name="dog_detail"),
    path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name="dog_update"),
    path('dogs/<int:pk>/delete', views.DogDelete.as_view(), name="dog_delete"),
    path('dogs/<int:pk>/history/new/', views.HistoryCreate.as_view(), name="history_create"),
    path('sizes/<int:pk>/dogs/<int:dog_pk>/', views.SizeDogAssoc.as_view(), name="size_dog_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]