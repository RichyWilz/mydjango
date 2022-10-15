from django.contrib import admin

# Register your models here.

#This is where the admin can be able to add "borrow", "book" models 
from .models import Book,Borrow
admin.site.site_header = 'LIBRARY ADMINISTRATION'
admin.site.register(Book)

class BorrowAdmin(admin.ModelAdmin):
    list_display = ['book_title','Fine']
    actions=['make_available']

    def make_available(self,request, queryset):
        queryset.book_title.status= 'Available'
        queryset.delete()


admin.site.register(Borrow,BorrowAdmin)





