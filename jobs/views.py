from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Application

@login_required
def jobpage_view(request):
    applications = []

    applicaiton_query = Application.objects.filter(user=request.user)
    applicaiton_query = applicaiton_query.order_by('-application_date')

    for application in applicaiton_query:
        print(application.followed_up)
        applications.append({
            'company_name': application.company_name,
            'url': application.url,
            'location': application.location,
            'email': application.email,
            'position': application.position,
            'followed_up': application.followed_up,
            'application_date': application.application_date.strftime('%B %d, %Y'),
            'id': application.id
        })

    return render(request, 'job.html', {
        'applications': applications
    })

@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user  # Set the currently logged-in user
            application.save()
            return redirect('jobpage')  # Redirect to some view after saving
    else:
        form = JobForm()
    return render(request, 'job_create.html', {'form': form})

@login_required
def job_toggle(request, id):
    application = Application.objects.filter(user=request.user).get(id=id)
    if application.followed_up:
        application.followed_up = False
    else:
        application.followed_up = True
    print(application.followed_up)
    application.save()
    return redirect('/jobs')

