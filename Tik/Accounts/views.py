from django.shortcuts import render,reverse,get_object_or_404
from django.views.generic import View
from .forms import UserForm,UserProfileForm,UpdateProfileForm,UpdateUserForm,PasswordChangeForm,ContactForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import UserProfile as UserModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
class Login(View):
    template_name='Accounts/login.html'
    form_class=AuthenticationForm
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    def post(self,request):
            username=self.request.POST['username']
            password=self.request.POST['password']
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request,'You are now logged in')
                return redirect('home')
            else:
                messages.error(request,'Invalid Credentials')
                return redirect('login')


class Register(View):
    template_name='Accounts/registration.html'
    user_form=UserForm
    profile_form=UserProfileForm
    def get(self,request):
        return render(request,self.template_name,{'user_form':self.user_form,'profile_form':self.profile_form })

    def post(self,request):
        user_form=UserForm(request.POST)
        profile_form=UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            if user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
                user=user_form.save() # saving user_form to the database
                user.set_password(user.password)#hashing the pwd
                user.save() #save changes to the user

                profile=profile_form.save(commit=False)
                profile.user=user

                if 'profile_pic' in request.FILES:
                    profile.profile_pic=request.FILES['profile_pic']

                    profile.save()
                return redirect('login')
            else:
                messages.error(request,'Passwords do not match')
                return redirect('register')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('register')

class Logout(View):
    def get(self,request):
        logout(request)
        messages.success(request,'Logged Out Successfully')
        return redirect('home')

class UserProfileView(View):
    template_name='Accounts/user_profile.html'
    def get(self,request,username):
        user=get_object_or_404(User,username=username)
        profile=get_object_or_404(UserModel,user=user)
        return render(request,self.template_name,{'user':user,'profile':profile})

class UpdateProfileView(LoginRequiredMixin,View):
    template_name='Accounts/update_profile.html'
    def get(self,request):
        user_form=UpdateUserForm(instance=request.user)
        profile_form=UpdateProfileForm(instance=request.user.userprofile)
        return render(request,self.template_name,{'user_form':user_form,'profile_form':profile_form})
    def post(self,request):
        user_form=UpdateUserForm(request.POST,instance=request.user)
        profile_form=UpdateProfileForm(request.POST,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            profile=profile_form.save()
            messages.success(request,'Profile Successfully Updated')
            return redirect('home')

class PasswordChangeView(View):
    template_name='Accounts/password_change.html'
    form_class=PasswordChangeForm
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    def post(self,request):
        bound_form=PasswordChangeForm(request.POST,instance=request.user)
        if bound_form.is_valid():
            if bound_form.cleaned_data['password'] == bound_form.cleaned_data['confirm_password'] :
                user=bound_form.save()
                user.set_password(user.password)
                user.save()
                messages.success(request,'Password Changed Successfully, Login again ')
                return redirect('login')
            else:
                messages.error(request,'Passwords do not Match')
                return render(request,self.template_name,{'form':bound_form})
        else:
            messages.error(request,'Invalid Password Supplied')
            return render(request,self.template_name,{'form':bound_form})


class ContactUs(View):
    template_name='Tik/contact.html'
    form_class=ContactForm
    def get(self,request):
        return render(request,self.template_name,{'form':ContactForm})
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            mail_sent=bound_form.send_mail()
            if mail_sent:
                messages.success(request,'Email Successfully Sent')
                return redirect('home')
        return render(request,self.template_name,{'form':form_class()})
