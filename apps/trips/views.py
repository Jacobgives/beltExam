from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from ..login.models import User
from .models import Trip
def index(request):
    context={
    'tripsu':Trip.objects.filter(lusers=User.objects.get(id=request.session['user_id'])),
    'tripso':Trip.objects.exclude(uusers=User.objects.get(id=request.session['user_id']))
        }
    for a in context['tripsu']:
        print a
    return render(request, 'trips/index.html', context)
def show(request, id):
    context={
        'name':Trip.objects.get(id=id).name,
        'users':User.objects.filter(ltrips=Trip.objects.get(id=id)),
        'uuser':Trip.objects.get(id=id).uusers,
        'plan':Trip.objects.get(id=id).plan,
        'e_date':Trip.objects.get(id=id).e_date,
        's_date':Trip.objects.get(id=id).s_date,
        }
    return render(request, 'trips/show.html', context)
def create(request):
    return render(request, 'trips/create.html')
def createa(request):
    print request.POST
    if request.method!= 'POST':
        return redirect('/')
    Trip.objects.validate_trip_c(request.POST, User.objects.get(id=request.session['user_id']), request.POST['plan'],request.POST['s_date'],request.POST['e_date'])
    return redirect('trips:index')
def add(request, id):
    User.objects.get(id=request.session['user_id']).ltrips.add(Trip.objects.get(id=id))
    return redirect('trips:index')
