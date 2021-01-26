from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Home,name='Home'),
    path('category/<int:cid>/',views.category,name='category'),
    path("contact/",views.contact,name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)