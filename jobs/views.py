from django.shortcuts import render
from .models import job1 #1.access items from the database

# Create your views here.
def home1(request):
    jobs = job1.objects #2.access items from the database (data base objects->Python objects)
    return render(request, 'jobs/home.html', {'jobs':jobs}) #3. "jobspy" pass forward as a dictionary

    # Portfolio-projects/jobs/templates/jobs/home.html
