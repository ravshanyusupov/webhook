from django.urls import path

from myapp.views import Master

urlpatterns = [
    path('', Master.as_view())
]