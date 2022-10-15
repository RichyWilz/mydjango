from django.urls import path
from . import views
app_name = 'books'

#These are the different urls for our "books" app. They contain what they'll show on a user's http request,
# the name of the view function or class that calls/responds to them as well as their names.

urlpatterns = [
    path("",views.book_overview,name="book_overview"),
    path("<int:pk>/",views.book_detail,name="book_detail"),
    path("<int:pk>/borrow/", views.borrow, name="borrow"),
    path("activity", views.activity, name="activity"),
    path("urlmessage", views.urlmessage, name="message"),
    path('search_book/', views.BookSearchView.as_view(), name= 'search_book'),
    ]