from django.shortcuts import render
from projects.models import Project

# Create your views here.


def project_index(request):

    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project_index.html', context)


def project_details(request, project_id):

    project = Project.objects.get(id=project_id)
    context = {'project': project}
    return render(request, 'projects/project_details.html', context)
