from django.shortcuts import render

# Create your views here.
def Todo_Home(request):
    return render(request, "todo.html")