from django.shortcuts import render
from django.contrib import messages, auth
from accounts.forms import UserRegistrationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
