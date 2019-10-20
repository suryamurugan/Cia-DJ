from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField




from datetime import datetime  



class UserType(models.Model):
    ut_id = models.IntegerField(primary_key=True)
    ut_name= models.CharField(max_length=255, null=False, default='type')
    def __str__(self):
        return "{} - {}".format(self.ut_id, self.ut_name)

class UserTypeRegister(models.Model):
    ut_id = models.IntegerField(primary_key=True)
    ut_name= models.CharField(max_length=255, null=False, default='type')
    def __str__(self):
        return "{} - {}".format(self.ut_id, self.ut_name)


class Dept(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=30,null=False,blank=True,default='dept_name')
    def __str__(self):
        return "{} - {}".format(self.dept_id, self.dept_name)


class User(AbstractUser):
    #u_id= models.IntegerField(primary_key=True)
    u_id= models.AutoField(primary_key=True)
    usn = models.TextField(max_length=10, blank=True)
    #dept = models.ForeignKey(Dept,on_delete=models.CASCADE,null=True,blank=True)
    dept = models.IntegerField(default=1,blank=True,null=True)
    phone_number = PhoneNumberField(blank=True)
    #user_t = models.ForeignKey(UserType,on_delete=models.CASCADE,null=True,blank=True)
    ut_id = models.IntegerField(default=1,blank=True,null=True)
    #ut = models.IntegerField(blank=True,default=1)
    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {}".format(self.u_id, self.usn,self.username,self.dept,self.email,self.phone_number,self.ut_id)
 


class Events(models.Model):
    # song title - s
    #"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    e_id = models.AutoField(primary_key=True)
    e_state = models.BooleanField(default=True)
    e_title = models.CharField(max_length=255, null=False, default='title')
    e_date = models.DateField('Event Date', default=datetime.now, blank=True)
    e_start_time = models.TimeField(default='12:00:00')
    e_end_time = models.TimeField(default='12:00:00',null=True,blank=True)
    e_venue = models.CharField(max_length=120,null=False, default='Venue')
    #e_organizer = models.CharField(max_length=255, null=False,default='Organizer')
    e_organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    e_description = models.TextField(blank=True)
    e_score = models.IntegerField()
    e_registration_link = models.CharField(max_length=255, null=True, blank=True)
    e_photos_link = models.CharField(max_length=255, null=True,blank=True)
    e_medium_link = models.CharField(max_length=255, null=True,blank=True)
    e_code = models.CharField(max_length=255, null=True,blank=True)
    
    # name of artist or group/band
    def __str__(self):
        return "{} - {}".format(self.e_id, self.e_title)

class AttendRegister(models.Model):
    arid = models.AutoField(primary_key=True)
    e_id = models.ForeignKey(Events, on_delete=models.CASCADE)
   # e_score = models.For
    u_id = models.ForeignKey(User,on_delete=models.CASCADE)
    a_datetime = models.DateTimeField(default=datetime.now(), blank=True)
    
    
    def __str__(self):
        return "{} - {}".format(self.arid, self.e_id)



class News(models.Model):
    # song title - s
    #"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    n_id = models.IntegerField(primary_key=True)
    n_title = models.CharField(max_length=255, null=False, default='title')
    n_desc = models.CharField(max_length=500, null=False, default='title')
    n_author = models.ForeignKey(User,on_delete=models.CASCADE)
    n_datetime = models.DateTimeField(default=datetime.now(), blank=True)
    n_image = models.ImageField(upload_to = 'images/news/', default = 'news/no-img.jpg')
    n_link = models.CharField(max_length=255,null=False, blank=True)
    def __str__(self):
        return "{} - {}".format(self.n_id, self.n_title)
##########################################################################

class Project(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_state = models.BooleanField(default=True)
    p_title = models.CharField(max_length=100, null=False, default='title')
    p_image = models.ImageField(upload_to = 'images/projects/', default = 'projects/no-img.jpg')
    u_id = models.ForeignKey(User,on_delete=models.CASCADE)
    p_datetime = models.DateTimeField(default=datetime.now(), blank=True)
    p_desc = models.CharField(max_length=500, null=False, default='description')
    p_medium_link = models.CharField(max_length=250, null=False, default='https://www.medium.com')
    p_github_link = models.CharField(max_length=250, null=False, default='https://www.github.com')
    p_apply_link = models.CharField(max_length=250, null=False, default='https://www.google.com')

