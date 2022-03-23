from django.urls import path

from myapp.views import template, Master

urlpatterns = [
    path('', Master.as_view()),
    path('bot', template,)
]