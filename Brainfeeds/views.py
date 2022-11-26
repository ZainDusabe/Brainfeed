
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.urls import reverse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Author, Books, Contact, Genre, Order,User

def index(request):
    author = Author.objects.all()
    genre=Genre.objects.all()
    contact = Contact.objects.all()
    mybooks = Books.objects.all()
    order = Order.objects.all()
    content={"genre":genre, "mybooks": mybooks, "contact": contact, "order":order, "author":author}
    return render(request,'index.html', content )

def myorders(request):
    author = Author.objects.all()
    genre=Genre.objects.all()
    contact = Contact.objects.all()
    mybooks = Books.objects.all()
    order = Order.objects.all()
    content={"genre":genre, 'mybooks': mybooks, "contact": contact, "order":order, "author":author}
    return render(request,'myorder.html', content)

def read(request):
    author = Author.objects.all()
    genre=Genre.objects.all()
    contact = Contact.objects.all()
    mybooks = Books.objects.all()
    order = Order.objects.all()
    content={"genre":genre, "mybooks": mybooks, "contact": contact, "order":order, "author":author}
    return render(request,'read.html', content)

def sample(request):
    author = Author.objects.all()
    genre=Genre.objects.all()
    contact = Contact.objects.all()
    mybooks = Books.objects.all()
    order = Order.objects.all()
    content={"Genre":genre, 'mybooks': mybooks, "contact": contact, "order":order, "author":author}
    return render(request,'sample.html', content)   

def register(request):
    msg =None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')  
        else:
           msg = 'form is not valid' 
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form':form, 'msg':msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None :
                form = login(request, user)
                messages.success(request, f' Welcome to Brainfeeds {username} !!')
                return redirect('index')

            else:
              messages.info(request, f'account does not exist plz Try again')
              return redirect('login_view')
    return render(request, 'login.html', {'form':form, 'title':'log in'})

                       

def homepage(request):
    
         return render(request, 'homepage.html')

def addbook(request):
    genre=Genre.objects.all()
    mybooks = Books.objects.all()
    author = Author.objects.all()
    order = Order.objects.all()
    contact = Contact.objects.all()
    
    if request.method == 'POST':
        Title = request.POST['Title']
        Pages = request.POST['Pages']
        Edition = request.POST['Edition']
        genre=Genre.objects.get(id=request.POST['genre'])
        writer=Author.objects.get(id=request.POST['author'])
        Username=User.objects.get(username=request.POST['Username'])
        Published_date=request.POST['Published_date']
        Price=request.POST['Price']
        Copies=request.POST['Copies']
        
        Poster = request.FILES['Poster']
        Filepath  = request.FILES['Filepath']

        b = Books( Title = Title, Pages = Pages, Edition=Edition, genre=genre,Author=writer,Username=Username,
        Published_date=Published_date,Price=Price,Copies=Copies, Poster=Poster,Filepath=Filepath )
        b.save()
        messages.success(request, f' Your book has been Published successfuly !!')
        return redirect('index')
       
    context={"genre":genre, "mybooks":mybooks, "author": author, "order": order, "contact":contact}
    return render(request,'addbook.html',context) 


def addauthor(request):
    genre=Genre.objects.all()
    mybooks = Books.objects.all()
    author = Author.objects.all()
    order = Order.objects.all()
    contact = Contact.objects.all()
    
    if request.method == 'POST':
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Gender = request.POST['Gender']
     
        Username=User.objects.get(username=request.POST['Username'])
        Dateofbirth=request.POST['Dateofbirth']
        Email=request.POST['Email']
        Region=request.POST['Region']

        a = Author( Firstname = Firstname, Lastname = Lastname, Gender=Gender, Username=Username,Date_of_Birth=Dateofbirth,
        Email=Email, Region=Region)
        a.save()
        
        return redirect('addbook')
       
    context={"genre":genre, "mybooks":mybooks, "author": author, "order": order, "contact":contact}
    return render(request,'addauthor.html',context) 



def transaction(request):
    genre=Genre.objects.all()
    mybooks = Books.objects.all()
    author = Author.objects.all()
    order= Order.objects.all()
    contact = Contact.objects.all()

    if request.method =='POST':
        user = User.objects.get(username=request.POST.get('username'))
        Title = Books.objects.get(id=request.POST.get('Title'))
        Writer=Author.objects.get(id=request.POST.get('Firstname'))
        Copies=request.POST['Copies']
        cardnumber=request.POST['cardnumber']
        cardholder=request.POST['cardholder']
        cvv =request.POST['cvv'] 
        Price=request.POST['Price']
        expiration =request.POST['expiration']
        
        
        pay = Order(user=user,Title=Title,Author=Writer,Copies=Copies,Cardnumber=cardnumber,
        cardholder=cardholder,cvv=cvv,Price=Price,Date=expiration)
        pay.save()
        messages.success(request, f' Thank you for making order!')
        return redirect('index')
       
    context={"genre":genre, "mybooks": mybooks, "author": author, "order": order, "contact":contact}
    return render(request,'payment.html',context)




def contact (request):
    genre=Genre.objects.all()
    mybooks = Books.objects.all()
    author = Author.objects.all()
    order = Order.objects.all()
    contact = Contact.objects.all()
    if request.method=='POST':
        username = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        cont=Contact(username=username,email=email,subject=subject,message=message)
        cont.save()
        messages.success(request, f' Your messsage has been sent successfully. Thank you!! {cont.username} !!')
        return redirect('index')

    context={"genre":genre, "mybooks":mybooks, "author": author, "order": order, "contact":contact}    
    return render(request,'index.html',context) 

def delete(request, id):
  book = Books.objects.get(id=id)
  book.delete()
  return HttpResponseRedirect(reverse('index'))
def signup(request):
    
    return render(request,'homepage.html')
def insert(request):
    if request.method=="POST":
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        if request.POST['type'] =="is_customer":
            is_customer=1
        else:
            is_customer=0
        if request.POST['type']=="is_author":
            is_author=1
        else:
            is_author=0
        user=User.objects.create_user(first_name=firstname, last_name=lastname, email=email,
        username=username,password=password,is_author=is_author,is_customer=is_customer)
        user.save()
    return redirect('/login/')

def search(request):
    if request.method =='POST':
        Title=request.POST['search']
    s=Books.objects.filter(Title=Title)

    return render(request,'search.html',{'s':s})

