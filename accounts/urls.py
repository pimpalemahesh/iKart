from django.urls import path
from accounts.views import login_page,register_page, profile
from django.contrib.auth.views import LogoutView


urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('register/' , register_page , name="register"),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('profile/', profile, name='profile'),
   # path('activate/<email_token>/' , activate_email , name="activate_email"),
]
