from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views import generic 
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm, UserProfileForm
from .models import Profile
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# from articles.models import Article

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        Profile.objects.create(user=user)
        login(self.request, user)
        return response

class ProfileUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('user:profile')

    def get_object(self):
        return self.request.user.profile

class UserLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('article:list_article')


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile
    
def logout_view(request):
    logout(request)
    return redirect('user:login')
    
# class UserLogoutView(LoginRequiredMixin,LogoutView):
#     logout(self.request)
#     def get_succes_url(self):
#         return redirect('user:login')
