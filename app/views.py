from django.http import HttpResponseRedirect
from app.models import Project, Image, ImageForm
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect

def home(request):
    return redirect('/p/1/')

def index(request):
    latest_project_list = Project.objects.all().order_by('-pub_date')[:5]
    return render_to_response('list.html', {'latest_project_list': latest_project_list})

def detail(request, project_id):
    images_list = Image.objects.all()
    project_name = Project.objects.get(pk=project_id).project_name
    return render_to_response('project.html', {
	    'images_list': images_list,
	    'project_id': project_id,
        'project_name': project_name,
	    })

def darkroom(request, project_id, image_id):
    image = Image.objects.get(pk=image_id)
    return render_to_response('darkroom.html', {
	    'image': image,
	    })

def upload(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    img_new = Image(project=project)
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES, instance=img_new)
        if form.is_valid(): 
            form.save()
	    return HttpResponseRedirect('/p/%s/'%project_id)
    
    form = ImageForm()

    return render_to_response('upload.html', {'form': form, 'project_id': project_id,}, context_instance=RequestContext(request))
		
