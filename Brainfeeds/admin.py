from django.contrib import admin

from .models import Contact, Genre, User,Author,Books,Order

# Register your models here.
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Order)
admin.site.register(Genre)
admin.site.register(Contact)