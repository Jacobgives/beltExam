from django.db import models
import re, bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_user_r(self,post_data):
        response_to_views ={}
        TheUser=self.filter(uname=post_data['uname'])
        if TheUser:
            response_to_views['status']=False
            return response_to_views
        errors={}
        name_Match=re.compile(r'^[a-zA-Z ]{3,255}$')
        input_valid=True
        if not re.match(name_Match, post_data['name']):
            input_valid=False
            errors["name"] = "Name should be more than 2 characters."
        if not self.filter(uname=post_data['uname']) and not re.match(name_Match, post_data['uname']):
            input_valid=False
            errors["name"] = "Username should be more than 2 characters and unique."
        if len(post_data['p'])<8 or post_data['p']!= post_data['cp']:
            input_valid=False
            errors['pass'] = "Password must be at least 8 characters and must match."
        if input_valid:
            print('got here')
            new_user = self.create(
            name=post_data['name'],
            uname=post_data['uname'],
            password=bcrypt.hashpw(post_data['p'].encode(), bcrypt.gensalt())
            )
            response_to_views['status']=True
            response_to_views['id']=new_user.id
            return response_to_views
        response_to_views['status']=False
        return response_to_views
    def validate_user_l(self, post_data):
        response_to_views={}
        TheUser=self.filter(uname=post_data['luname'])
        if TheUser:
            if bcrypt.checkpw(post_data['lp'].encode(), TheUser[0].password.encode()):
                response_to_views['status']=True
                response_to_views['id']=TheUser[0].id
                return response_to_views
        response_to_views['status']=False
        return response_to_views

class User(models.Model):
    name = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
