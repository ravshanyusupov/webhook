from django.urls import path

from myapp.views import Master, template

urlpatterns = [
    path('bot', Master.as_view()),
    path('', template,)
]