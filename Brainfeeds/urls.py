from django.urls import path,include
from . import views
from django.contrib.auth import views as auth
urlpatterns = [
    # path('homepage/',views.homepage,name='homepage'),
    path('login/', views.login_view, name='login_view'),
    path('register/',views.register, name='register'),
    path('addbook/',views.addbook, name='addbook'),
    path('addauthor/',views.addauthor, name='addauthor'),
    path('add',views.addbook, name='addbook'),
    path('',views.index, name='index'),
    path('read/',views.read, name='read'),
    path('transaction/search/',views.search,name='search'),
    path('search/',views.search,name='search'),
     path('sample',views.sample, name='sample'),
     path('payment/',views.transaction, name='transaction'),
     path('transaction/index',views.index, name='index'),
      path('Signup/',views.signup, name='signup'),
      path('insert',views.insert, name='insert'),
     path('contact',views.contact, name='contact'),
    path('myorders', views.myorders, name='myorders'),
      path('delete/<int:id>', views.delete, name='delete'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
]