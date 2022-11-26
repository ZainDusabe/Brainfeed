from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Is_admin', default=False)
    is_author = models.BooleanField('Is_author', default=False)
    is_customer = models.BooleanField('Is_customer', default=False)
    
class Genre(models.Model):
    name=models.CharField(max_length=200)

    def _str_(self):
        return self.name

class Author(models.Model):
    Gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Others'),
    )
    id = models.IntegerField(primary_key=True)
    Firstname = models.CharField(max_length=254)
    Lastname = models.CharField(max_length=254)
    Gender = models.CharField(max_length=5, choices=Gender_choices)
    Username =models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    Date_of_Birth = models.DateField(max_length=254)
    Email = models.EmailField(max_length=254)
    Region = models.CharField(max_length=254)
    

class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=254)
    Pages = models.CharField(max_length=254)
    Edition = models.CharField(max_length=254)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    Author =models.ForeignKey(Author,on_delete=models.CASCADE, default=1)
    Username =models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    Published_date = models.DateTimeField(auto_now=True)
    Price = models.CharField(max_length=254)
    Copies = models.CharField(max_length=254)
    Poster = models.ImageField(default='avatar.jpg',upload_to="static/images")
    Filepath = models.FileField(upload_to='files/', null=True, verbose_name="")
   
class Order(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.ForeignKey(Books,on_delete=models.CASCADE)
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    Copies =models.IntegerField() 
    Cardnumber = models.IntegerField()
    cardholder = models.CharField(max_length=254)
    cvv = models.IntegerField()
    Price = models.IntegerField()
    Date = models.DateField()

class Contact(models.Model):
    username = models.CharField(max_length=200, default = "Customer")
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    def _str_(self):
        return self.email



