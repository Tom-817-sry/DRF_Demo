from django.urls import include,path
from django.views import View
from .views import DjangoView

urlpatterns = [
    path(r"",DjangoView.as_view())
]