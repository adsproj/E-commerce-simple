from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.welcome_page,name='welcome_page'),
    path('login_page',views.login_page,name='login_page'),
    path('signup_page',views.signup_page,name='signup_page'),
    path('mobile_page',views.mobile_page,name='mobile_page'),
    path('fashion_page',views.fashion_page,name='fashion_page'),
    path('userpage',views.userpage,name='userpage'),

    path('usercreate/',views.usercreate,name="usercreate"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout")
]