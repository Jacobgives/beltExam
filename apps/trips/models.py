from django.db import models
from ..login.models import User
import re, bcrypt
import time

# Create your models here.
class TripManager(models.Manager):
    def validate_trip_c(self,post_data, u, p, s, e):
        response_to_views ={}
        TheTrip=post_data['newtrip']
        if not TheTrip:
            response_to_views['status']=False
            return response_to_views
        name_Match=re.compile(r'^[a-zA-Z ]{3,255}$')
        input_valid=True
        if not re.match(name_Match, post_data['newtrip']):
            input_valid=False
            print('input not valid')
            errors['trip']='Trip must be greater than three characters.'
        if not p:
            errors['plan']='Please include a plan.'
        if not e > s:
            errors['time']='You cannot end a trip before you begin it.'
        if input_valid:
            new_trip = Trip.objects.create(
            name=post_data['newtrip'],
            uusers=u,
            plan=p,
            s_date=s,
            e_date=e
            )
            User.objects.get(id=u.id).ltrips.add(new_trip.id)
            response_to_views['status']=True
            response_to_views['trip']=new_trip.id
            return response_to_views
        response_to_views['status']=False
        return response_to_views

class Trip(models.Model):
    name= models.CharField(max_length=255)
    uusers=models.ForeignKey(User, related_name="utrips")
    lusers=models.ManyToManyField(User, related_name="ltrips")
    plan= models.TextField(default = 'Many Guds will be got.')
    s_date=models.DateTimeField()
    e_date=models.DateTimeField()
    c_date = models.DateTimeField(auto_now_add=True)
    u_date = models.DateTimeField(auto_now=True)
    objects = TripManager()
