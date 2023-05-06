from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from .models import Customer 
from django.contrib.auth.models import Group



def customer_create_profile(sender , instance ,created , **kwargs ):

    if created:   
         group=Group.objects.get(name="costumers")
         instance.groups.add(group) 
         Customer.objects.create(
                                    user=instance
                                       ,name=instance.username)   


         print('customer profile created')


post_save.connect(customer_create_profile , sender=User)
 