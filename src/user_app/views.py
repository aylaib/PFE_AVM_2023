from django.shortcuts import render

from User_Aviation.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):

    return render(request, 'user_app/index.html')



