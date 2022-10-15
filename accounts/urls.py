
from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns =[ 
    path('',views.welcome, name="welcome"),
    path('login/',views.login_user, name="login"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout', views.logout_user, name="logout"),
    ]
    
    
