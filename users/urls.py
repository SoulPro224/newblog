from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileUpdateView,UserLoginView,ProfileDetailView,logout_view

app_name= 'user'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', logout_view, name='logout'),

]

