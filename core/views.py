from django.shortcuts import render
from core.models import *


def index(request):
    data = {}
    try:
        namespace_id = request.GET["namespace_id"]
    except:
        namespace_id = -1
    if namespace_id == -1:
        namespace = Namespace.objects.all().first()
    else:
        namespace = Namespace.objects.all().filter(id=namespace_id)
    data["namespace"] = namespace
    data["users"] = namespace.users.all()
    return render(request, "core/home.html", data)


def current_projects(request):
    data = {}
    projects = Project.objects.all()
    data["projects"] = projects
    return render(request, "core/projects.html", data)
