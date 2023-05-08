from django.urls import path
from. import views

#http://127.0.0.1:8000/ 
#http://127.0.0.1:8000/movies
#http://127.0.0.1:8000/movies/3
#http://127.0.0.1:8000/movies/walking-dead


urlpattens=[
   path("", views.home)
]