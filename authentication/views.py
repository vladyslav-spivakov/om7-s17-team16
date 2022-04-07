from django.shortcuts import render
from .models import CustomUser

# Create your views here.


def user_list(request):
    users = list(CustomUser.get_all())
    context = {
        'is_empty': not bool(users),
        'users': users,
    }

    return render(request, 'user_list.html', context)

def user_post(request, id=0):


    context = {}
    return render(request, 'user_list.html', context)