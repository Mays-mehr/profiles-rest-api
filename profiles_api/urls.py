from django.urls import path
from profiles_api import views


urlpatterns = [
    path('' , views.HelloApiView2.as_view() ),
    path('hello-view/' , views.HelloApiView.as_view() ),
]
