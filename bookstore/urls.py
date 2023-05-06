
from django.urls import path
from . import views 
from django.contrib.auth import views as authViews


# views.home
urlpatterns = [
path('', views.home, name="home"),
path('book/', views.book , name="book"),
# path('customer/', views.customer ,name="customer"),
# path('customer/<str:pk>',views.customer,name="customer"),
path('create/', views.create , name="create"),
path('update/<str:pk>', views.update , name="update"),
path('delete/<str:pk>', views.delete , name="delete"),
path('create/<str:pk>', views.create , name="create"),# لتحديد يوزر معين يعني مفترض انا كمستخدم ما يضهرلي الا اسمي 
path('register/', views.register , name="register"),
path('login/', views.UserLogin , name="UserLogin"),
path('logout/', views.UserLogout , name="UserLogout"),
path('profileInfo/', views.profileInfo , name ="profileInfo"),
path('profile/', views.UserProfile , name = "UserProfile"),

#################
path('reset_password/', authViews.PasswordResetView.as_view() ,name ="reset_password") ,
path('reset_password_sent/', authViews.PasswordResetDoneView.as_view() ,name ="reset_password_done"),
path('reset/<uidb64>/<token>', authViews.PasswordResetConfirmView.as_view() ,name ="reset_password_confirm" ),
path('reset_password_complete/', authViews.PasswordResetCompleteView.as_view() ,name = "reset_password_complete" ),


]