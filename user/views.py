from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from .forms import City_Choice_Form
from .models import City
import math
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
def all_cities_view(request):
    if request.user.is_authenticated:
        obj=City.objects.all()
        context = {
        "City_List": obj
        }
        return render(request,"user/cities.html",context)

def input_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            client_cities=City_Choice_Form(request.POST)
            if client_cities.is_valid():
                n = client_cities.cleaned_data.get("citi")
                k=client_cities.cleaned_data.get('k')
                cnt_citi=len(n)
                weights=[[0 for i in range(cnt_citi)] for j in range(cnt_citi)]
                axl=[]
                ayl=[]
                print(n)
                for i in n:
                   a=City.objects.get(id=i)
                   ax=a.x_coordinate
                   ay=a.y_coordinate
                   axl.append(ax)
                   ayl.append(ay)
                print(axl)
                #now create the adj matrix
                for i in range(cnt_citi):
                    for j in range(cnt_citi):
                        weights[i][j]=math.sqrt(pow((axl[i]-axl[j]),2)+pow((ayl[i]-ayl[j]),2)) 
                dist = [0]*cnt_citi
                centers = []
            
                for i in range(cnt_citi):
                    dist[i] = 10**9
                # index of city having the
                # maximum distance to it's
                # closest center
                max = int(n[0])
                # max=0
                print(max)
                for i in range(k):
                    centers.append(max)
                    for j in range(cnt_citi):
                        dist[j] = min(dist[j], weights[max][j])
                    # max = maxindex(dist, cnt_citi)
                    max = 0
                    for p in range(cnt_citi):
                        if (dist[p] > dist[max]):
                            max = p
                # print(dist[max])
                context={}
                warehouse_list=[]
                context['max_dist']=dist[max]
                print(centers)
                # print(n[centers])
                for i in centers:        
                    # warehouse_list.append(n[i])
                    warehouse_list.append(City.objects.get(id=n[i]))
                    print(warehouse_list)
                context['warehouse_list']=warehouse_list
                    # print(i, end = " ")

                return render(request,'user/output.html',context)
        else:
            # context={}
            form= City_Choice_Form()
            context={
                "name":request.user,
                'city_names':[],
                'form':form,
            }
            form = City_Choice_Form(request.POST or None)
            if form.is_valid():
                form.save()
            return render(request, "user/input.html", context)
    else:
        return redirect('user-home')


