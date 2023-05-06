import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
       
        fields = ['book', 'status']
         # fields = '__all__' كلشي 
        #exclude = ['book'] هون كلشي عدا الكتاب 