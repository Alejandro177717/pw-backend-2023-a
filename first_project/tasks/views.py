from django.shortcuts import render

# Creando una variable global
tasks = ["foo", "bar", "baz"]
# Create your views here.
def index(request):
		# Mandarmos entregar la vista con el contexto
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")