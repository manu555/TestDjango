from django.shortcuts import render, get_object_or_404
from .models import Project
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import ProjectForm

# Create your views here.

def project_list(request):
    projects = Project.objects.filter(last_updated_date__lte=timezone.now()).order_by('last_updated_date')
    return render(request, 'testapp/project_list.html', {'projects' : projects})

def handler_projects(request, pk):
    handler = get_object_or_404(User, pk=pk)
    show_projects = Project.objects.filter(Handler=handler)
    return render(request, 'testapp/handler_projects.html', {"handler" : handler, "show_projects" : show_projects})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.Handler = request.user
            project.created_date = timezone.now()
            project.save()
    else:
        form = ProjectForm()
    return render(request, 'testapp/post_edit.html', {'form' : form})
