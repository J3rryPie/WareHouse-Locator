from django.shortcuts import render,redirect
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request,'user/home.html')

def signup(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'user/signup.html',{'form':form})

def about(request):
    return render(request,'user/about.html')

def project(request):
    return render(request,'user/project.html')


