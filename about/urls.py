from . import views
from views import about
from django.urls import path

urlpatterns = [
        path('about/', views.about(), name='about'),
]