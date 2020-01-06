from django.urls import include,path
from .views import Book,BookView

urlpatterns = [
    path(r"book",BookView.as_view()),
]