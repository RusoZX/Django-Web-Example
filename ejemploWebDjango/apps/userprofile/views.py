from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from apps.notification.utilities import create_notification

from .forms import UserProfileForm

# Create your views here.
def userprofile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user' : user
    }
    return render(request, 'userprofile/userprofile.html', context)

@login_required
def like_user(request, username):
    user = get_object_or_404(User, username=username)
    request.user.userprofile.likes.add(user.userprofile)
    create_notification(request, user, 'like')

    return redirect('userprofile', username=username)

@login_required
def unlike_user(request, username):
    user = get_object_or_404(User, username=username)
    request.user.userprofile.likes.remove(user.userprofile)

    return redirect('userprofile', username=username)

def likesreceived(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'userprofile/likesreceived.html', {'user': user})

def likesgiven(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'userprofile/likesgiven.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance= request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('userprofile', username= request.user.username)
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    context ={
        'user': request.user,
        'form':form
    }
    return render(request, 'userprofile/edit_profile.html', context)


