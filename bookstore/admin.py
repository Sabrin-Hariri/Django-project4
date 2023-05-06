from django.contrib import admin

# Register your models here.
# from .models import Book, Customer, Order , Tag
# sabrin - 123123123
from .models import *

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Tag)


admin.site.site_header="QUIAN"
admin.site.site_title="sabrin"

