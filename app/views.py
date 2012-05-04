from django.http import HttpResponse
from django.shortcuts import render_to_response
from app.models import Project, Image
from django.template.context import RequestContext

def index(request):
    latest_project_list = Project.objects.all().order_by('-pub_date')[:5]
    return render_to_response('list.html', {'latest_project_list': latest_project_list})

def detail(request, project_id):
    images_list = Image.objects.all()
    return render_to_response('project.html', {'images_list': images_list})

