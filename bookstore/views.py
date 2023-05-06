from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import*
# from .forms import OrderForm
from .forms import OrderForm , CreateNewUser,CustomerForm
from .filters import OrderFilter
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .decorators import NotLoggedUser ,allowedUsers ,forAdmins
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout 
from django.contrib.auth.decorators import login_required # to save my function
from django.contrib.auth.models import Group

import requests
from django.conf import settings


######################################################################

# @login_required(login_url='UserLogin')
# @allowedUsers(allowedGroups=['admin'])
# @forAdmins
def home(request ): 

    customer=Customer.objects.all()
    order=Order.objects.all()   
    t_order=order.count()
    p_order=order.filter(status='Pending').count()
    d_order=order.filter(status='Delivered').count()
    in_order=order.filter(status='in progress').count()
    out_order=order.filter(status='out of order').count()
    context={'reqcustomer':customer,
             'reqorder':order,
             't_order':t_order,
             'p_order':p_order,
             'd_order':d_order,
             'in_order':in_order,
             'out_order':out_order}
    return render(request ,'bookstore/dashboard.html',context)


######################################
# حمل الداتا بعدا ارسلها لصفحه الكتب _ هاد رح يطلب نعمل متغير يستقبل الداتا ويعطيها للفورم 
# @forAdmins
def book(request ): 
    books=Book.objects.all()
    return render(request ,'bookstore/book.html',{'reqbook': books})

#####################################
    
def customer(request,pk): 
    customer=Customer.objects.get(id=pk)
    order=customer.order_set.all()
    num_order=order.count()
    searchfilter=OrderFilter(request.GET , queryset=order )
    order = searchfilter.qs #الكوري الى رح ترجعلي لازم على اساس السيرش الى موجود
    context={'reqcustomer':customer,
             'reqorder':order,
              'num_order':num_order,
               'searchfilter':searchfilter
            }
    return render(request ,'bookstore/customer.html',context)

def create(request):
    form=OrderForm()
    if request.method=='POST':
        # print (request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # print("succsus")
            return redirect('/')
        
    context={'formset':form}
    return render(request ,'bookstore/order_form.html',context  )

#######################################

# def create(request ,pk):
#     orderformset=inlineformset_factory(Customer,Order,fields=('book','status')) ## need models and the fields i want 
#     customer=Customer.objects.get(id=pk)
#     formset=orderformset( queryset= Order.objects.none() , instance=customer)
#     # form=OrderForm()
#     if request.method=='POST':
#         # print (request.POST)
#         formset=orderformset(request.POST ,instance=customer )
#         if formset.is_valid():
#             formset.save()
#             # print("succsus")
#             return redirect('/')
        
#     context={'formset':formset}
#     return render(request ,'bookstore/order_form.html',context  )

######################################



def update(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        # print (request.POST)
        form=OrderForm(request.POST ,pk, instance=order)
        if form.is_valid():
            form.save()
            # print("succsus")
            return redirect('/')      
    context={'form':form}
    return render(request ,'bookstore/order_form.html',context)


####################################
# @login_required(login_url='login')

def delete(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
            # print("succsus")
        return redirect('/')  
    context={'order':order}
    return render(request ,'bookstore/delete_form.html',context)
 
#####################################
# @NotLoggedUser 
#########
# def register(request):
#         # form=UserCreationForm()    
#     form=CreateNewUser()
#     if request.method=='POST':
#         form =CreateNewUser(request.POST)    
#         if form.is_valid():
#             user=form.cleaned_data.get('username')
#             form.save()
#             messages.success(request, user + ' Created Successfully ! ')
#     context={'form' : form}   

#     return render(request ,'bookstore/register.html' , context)
def register(request):   
             if request.user.is_authenticated :

                return redirect('/')
               
             else:
                form = CreateNewUser()
                if request.method == 'POST': 
                    form = CreateNewUser(request.POST)
                    if form.is_valid():

                        recaptcha_response = request.POST.get('g-recaptcha-response')
                        data = {
                            'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                            'response' : recaptcha_response
                        }
                        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
                        result = r.json()
                        if result['success']:
                            user=form.save()
                            username = form.cleaned_data.get('username')
                            # group=Group.objects.get(name="costumers")
                            # user.groups.add(group) ما عدت احتجتو مع استخدام post_save 
                            messages.success(request , username + ' Created Successfully !')
                            return redirect('login')
                        else:
                            messages.error(request ,  ' invalid Recaptcha please try again!')  
    
        
             context = {'form':form}

             return render(request , 'bookstore/register.html', context )


##############################################
# @NotLoggedUser
##############################################
def UserLogin(request) : 
    # form=CreateNewUser()
   
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username ,password=password )
            if user is not None: 
               login(request , user) 
               return redirect('/')
            else:
                messages.info(request, 'Credentials error !! ')

        context={}

        return render(request ,'bookstore/login.html' ,context)

##########################################
def UserLogout(request) : 
    logout(request)
    return redirect('/')



##########################################
# @login_required(login_url='login')
# @allowedUsers(allowedGroups=['costumer'])
def UserProfile(request) : 

    orders=request.user.customer.order_set.all()
    t_order=orders.count()
    p_order=orders.filter(status='Pending').count()
    d_order=orders.filter(status='Delivered').count()
    in_order=orders.filter(status='in progress').count()
    out_order=orders.filter(status='out of order').count()
    context={'reqcustomer':customer,
             'orders':orders,
             't_order':t_order,
             'p_order':p_order,
             'd_order':d_order,
             'in_order':in_order,
             'out_order':out_order}

    return render(request ,'bookstore/profile.html' ,context)


##########################################


# @login_required(login_url='login')
# @allowedUsers(allowedGroups=['costumer'])
def profileInfo(request) : 
    customer= request.user.customer
    form= CustomerForm(instance=customer)
    if request.method == 'POST':
        form =CustomerForm(request.POST ,request.FILES ,instance=customer )
        if form.is_valid():
            form.save()

    context={'form':form}

    return render(request ,'bookstore/profile_info.html' ,context)

