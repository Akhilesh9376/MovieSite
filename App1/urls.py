from django.urls import path
from .import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('category/<int:cid>/',views.category,name='category'),
    path("contact/",views.contact,name='contact'),
]