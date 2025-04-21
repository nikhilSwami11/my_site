from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page, name ="starting_page"),
    path("post", views.posts, name = "post-page"),
    path("posts/<slug:slug>", views.post_detail, name ="post-details-page") # post/my-first-post
]
