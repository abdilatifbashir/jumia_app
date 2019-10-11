from django.shortcuts import render, redirect
from .forms import UserEditForm, UserRegistrationForm, ProfileEditForm, LoginForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
        else:
            messages.error(request, 'We encountered an error,please check your details and try again')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profiles,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('account:profile')
            # messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profiles)
    return render(request, 'account/edit.html', {'user_form': user_form,
                                                 'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account:dashboard')
                else:
                    messages.error(request, 'Your username and password didn\'t match. please try again')

            else:
                messages.error(request, 'We didn\'t find account matching your details')

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def dashboard(request):
    return render(request, 'account/dashboard.html')

