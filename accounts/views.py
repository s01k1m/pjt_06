from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm






##################### koko part ##############################

@require_http_methods(['POST'])
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    user = get_user_model().objects.get(username=username)
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_user_model().objects.get(pk=user_pk)
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    else:
        return redirect('accounts:login')


##################### koko part #############################