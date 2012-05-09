from django.http import HttpResponseRedirect
from app.models import Project, Image, ImageForm
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_project_list = Project.objects.all().order_by('-pub_date')[:5]
    return render_to_response('list.html', {'latest_project_list': latest_project_list})

def detail(request, project_id):
    images_list = Image.objects.all()
    return render_to_response('project.html', {
	    'images_list': images_list,
	    'project_id': project_id,
	    })

def upload(request, project_id):
    image = get_object_or_404(Image, pk=project_id)
    if request.method == 'POST': # If the form has been submitted...
        form = ImageForm(request.POST, request.FILES, instance=image) # A form bound to the POST data
        #form.project = project_id
	if form.is_valid(): # All validation rules pass
            form.save()
	    return HttpResponseRedirect('/p/%s/'%project_id) # Redirect after POST
    
    form = ImageForm() # An unbound form

    return render_to_response('upload.html', {'form': form, 'project_id': project_id,}, context_instance=RequestContext(request))
		
