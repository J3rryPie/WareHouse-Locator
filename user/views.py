from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from .forms import City_Choice_Form
from .models import City
# from .models import City_Dist
from django.shortcuts import get_object_or_404
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

# def input_view(request,*args,**kwargst):
#     cities=
#     if request.user.is_authenticated():
#         context={
#             "name": request.user,
#             "all_cities"=['Mumbai','Pune','Nashik','Nagpur','Thane','Dapoli','Alibaugh']
#         }
#     return render(request,"user/input.html",context) 
# def output_view(request,*args,**kwargst):
#     return render(request,"user\output.html",{}) 

def all_cities_view(request):
    if request.user.is_authenticated():
        obj=City.object.all()
        context = {
        "City_List": obj
        }
        return (request,"user\cities.html",context)

def input_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            client_cities=City_Choice_Form(request.POST)
            if client_cities.is_valid():
                c = client_cities.cleaned_data.get("citi")
                # c_d=City_Dist.objects.all()                
                weights ={}
                axl=[]
                ayl=[]
                for i in c:
                   a=City.objects.get(id=i)
                   ax=a.x_coordinate
                   ay=a.y_coordinate
                   axl.append(ax)
                   ayl.append(ay)
                #now create the adj matrix
                
                    
                
        else:
            context={}
            context={
                "name":request.user,
            }
            form = City_Choice_Form(request.POST or None)
            if form.is_valid():
                form.save()
            context['form']= form
            return render(request, "user\input.html", context)
    else:
        return render(request,"home.html",context)

