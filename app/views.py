from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from app.models import Project, Image, ImageForm
from django.template.context import RequestContext

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
    if request.method == 'POST': # If the form has been submitted...
        form = ImageForm(request.POST, request.FILES) # A form bound to the POST data
	print 'xxx'
        #if form.is_valid(): # All validation rules pass
        print form.errors
	print request.POST
	form.save()
	print 'xxx2'
	
	return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ImageForm() # An unbound form

    return render_to_response('upload.html', {'form': form, 'project_id': project_id,}, context_instance=RequestContext(request))
		
