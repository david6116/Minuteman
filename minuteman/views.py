from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from minuteman.models import *

@login_required(redirect_field_name='/login/')
def dashboard(request):

    if request.method == 'POST':

        contractor_id = request.POST['contractor']
        contractor = Contractor.objects.get(pk=int(contractor_id))

        project_id = request.POST['project']
        project = Project.objects.get(pk=int(project_id))

        if 'start' in request.POST:
            try:
                current_project = Log.objects.get(contractor=contractor, stop=None).project
                if current_project == project:
                    messages.warning(request,
                        "Are you working too hard or just playing on facebook, you're already 'working' on %s." % current_project
                    )

                else:
                    messages.warning(request,
                        "We would all like to get paid twice as much, but this isn't the way to do. End %s first." % current_project
                    )

            except Log.DoesNotExist:
                log = Log(contractor=contractor, project=project, start=datetime.now(), stop=None)
                log.save()
                messages.success(request,
                    'Use your abilities at this time to stay focused on your goals. Log recorded'
                )

        elif 'stop' in request.POST:
            try:
                current_log = Log.objects.get(contractor=contractor, stop=None)
                if current_log.project == project:
                    current_log.stop = datetime.now()
                    current_log.save()
                    messages.success(request,
                        'I made you cookie, but i eated it already.'
                    )
                else:
                    messages.warning(request,
                        "Um... I'm pretty sure you meant to end %s. Try again." % current_log.project
                )

            except Log.DoesNotExist:
                messages.warning(request,
                    'Whoa! You worked so fast you forgot to hit start first, try again.'
                )

        return HttpResponseRedirect('/dashboard/')

    try:
        current_log = Log.objects.get(contractor=request.user.contractor, stop=None)
    except Log.DoesNotExist:
        current_log = None

    lastfive = Log.objects.filter(contractor__user=request.user)
    lastfive = lastfive.reverse()[1:6]
    contractors = Contractor.objects.all()
    projects = Project.objects.all()

    context = {
        'projects': projects,
        'contractors': contractors,
        'current_log' : current_log,
        "lastfive" : lastfive,
    }

    return render_to_response('minuteman/dashboard.html', context,
                              context_instance=RequestContext(request))
