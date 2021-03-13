from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.signals import post_save
import datetime as dt
from django.contrib.gis.db import models  
class Location(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
# class Locate(models.Model):                                                   
#         name = models.CharField(max_length = 100, blank = True)                 
#         coords = models.PointField()

#         def __str__(self):
#             return self.name  
class Insurance(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Pharmacy(models.Model):
    name=models.CharField(max_length=100)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    insurance = models.ManyToManyField(Insurance)
    direction = models.CharField(max_length=255)
    contact = models.PositiveIntegerField()
    pharm_pic=models.ImageField(upload_to='pictures/',default='pictures/default.png')

    def create_pharm(self):
        self.save()

    def delete_pharm(self):
        self.delete()

    @classmethod
    def find_pharm(cls, pharm_id):
        paharm= cls.objects.get(id=pharm_id)
        return pharm

    def __str__(self):
        return self.name
    location = models.CharField(max_length=255)
    contact = models.PositiveIntegerField()

    def create_pharm(self):
        self.save()

    def delete_pharm(self):
        self.delete()

    @classmethod
    def find_pharm(cls, pharm_id):
        paharm= cls.objects.get(id=pharm_id)
        return pharm

    def __str__(self):
        return self.name

class Drug(models.Model):
    name=models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    pic=models.ImageField(upload_to='pictures/')
    pharmacy=models.ManyToManyField(Pharmacy)

    def save_drug(self):
        self.save()

    def delete_drug(self):
        self.delete()

    @classmethod
    def search(cls,searchterm):
        search = Drug.objects.filter(Q(name__icontains=searchterm)).first()
        return search

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='pictures/',default='profiles/default.png')
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    # locate = models.ForeignKey(Locate, blank = True, null = True, on_delete=models.CASCADE) 
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        db_table = 'profile'

    # @receiver(post_save, sender=User)
    def update_create_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


    def save_profile(self):
        self.save()

# class Activity(models.Model):                                                   
#         owner = models.ForeignKey(User,blank = True, null = True, on_delete=models.CASCADE)               
#         name = models.CharField(max_length = 100,blank = False)                 
#         about = models.TextField(max_length = 500, blank = False)               
#         location = models.ForeignKey(Location, blank = True, null = True, on_delete=models.CASCADE)       
#         pharmacy = models.ManyToManyField(Pharmacy, blank = True)               
#         status = models.BooleanField(default = False)                           
#         deleted = models.BooleanField(default = False)                          
#         createdAt = models.DateTimeField(auto_now_add=True)                     

#         def __unicode__(self):                                                  
#                 return self.name