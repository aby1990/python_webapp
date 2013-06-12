#from django.template import Context, loader
from django import http
#from OpenLabs.models import details

#from django.http import HttpResponse
#from OpenLabs.models import details
#from django.http import Http404
#from django.db import transaction
#from django.shortcuts import render
from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect
#from OpenLabs.forms import detailsForm
#from models import details
from OpenLabs.models import details
#from django.db.models import Q
from django.core.context_processors import csrf
#from django.shortcuts import render_to_response

def home(request):
    return render_to_response('index.html')


def submit(request):
  
    if request.method == 'POST':
        name = request.POST.get('name')
        bdate = request.POST.get('bdate')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        qual = request.POST.get('qual')
        skill = request.POST.get('skill')
        
        if name and bdate and email and mobile and qual and skill:
            data = details.objects.create(
                  name=request.cleaned_data['name'], bdate=request.cleaned_data['bdate'], 
                  email=request.cleaned_data['email'], mobile=request.cleaned_data['mobile'], 
                  qual=request.cleaned_data['qual'], skill=request.cleaned_data['skill']
           )
            data.save()
        return http.HttpResponseRedirect("/welcome/")
    
    

#def submit(request):
#    if request.method == 'POST': 
#        # If the form has been submitted...
#        form = detailsForm(request.POST) # A form bound to the POST data
#        if form.is_valid(): # All validation rules pass
#            form.save()
#            # Process the data in form.cleaned_data
            # ...
#    return render(request, 'page.html', {'form': detailsForm()})

#def submit(request):
#    query = request.GET.get('q', '')

#    if query:
#        qset = (
#                Q(name__icontains=query) |
#                Q(bdate__icontains=query) |
#                Q(email__icontains=query) |
#                Q(mobile__icontains=query) |
#                Q(qual__icontains=query) |
#                Q(skill__icontains=query)
#                )
#        results = details.objects.filter(qset).distinct()
#    else:
#        results = []
#        return render_to_response("index.html", {
#"results": results, 
#
#"query": query
#})

#@transaction.commit_on_success
#def submit(request, n, b, e, m, q, s):
#    try:
#        new_sbmsn = details(name = n, bdate = b, email = e, mobile = m, qual = q, skill = s)
#        new_sbmsn.save()
#
#   except details.DoesNotExist:
#        raise Http404
#    return render_to_response("templates/index.html")
    


