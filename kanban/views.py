from django.shortcuts import render


def index(request):
    return render(request, "kanban/index.html")


def home(request):
    return render(request, "kanban/home.html")
