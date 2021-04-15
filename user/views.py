from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from .forms import City_Choice_Form
from .models import City
from .utils import Lat_Lon,calc_weights,get_center_coordinates
import math
from django.shortcuts import get_object_or_404
import folium
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


# def input_view(request):
#     Lat_Lon()
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             client_cities=City_Choice_Form(request.POST)
#             if client_cities.is_valid():
#                 n = client_cities.cleaned_data.get("citi")
#                 k=client_cities.cleaned_data.get('k')
#                 cnt_citi=len(n)

#                 weights=calc_weights()
#                 dist = [0]*cnt_citi
#                 centers = []

#                
#                 # user chosen cities (n)marker
#                 for i in n:
#                     c=City.objects.get(id=i)
#                     folium.Marker(
#                         [c.x_coordinate,c.y_coordinate], popup=c.name, tooltip="Your selected cities",icon=folium.Icon(color="purple")
#                     ).add_to(m)

#                 m=m._repr_html_()
#                 for i in range(cnt_citi):
#                     dist[i] = 10**9
#                 # index of city having the
#                 # maximum distance to it's
#                 # closest center
#                 max = int(n[0])
#                 for i in range(k):
#                     centers.append(max)
#                     for j in range(cnt_citi):
#                         dist[j] = min(dist[j], weights[max][j])
#                     # max = maxindex(dist, cnt_citi)
#                     max = 0
#                     for p in range(cnt_citi):
#                         if (dist[p] > dist[max]):
#                             max = p
#                 # print(dist[max])
#                 context={}
#                 context['map']=m
#                 warehouse_list=[]
#                 context['max_dist']=dist[max]
        
#                 for i in centers:        
#                     warehouse_list.append(City.objects.get(id=n[i]))

#                 context['warehouse_list']=warehouse_list

#                 return render(request,'user/output.html',context)
#         else:
#             # context={}
#             form= City_Choice_Form()
#             context={
#                 "name":request.user,
#                 'city_names':[],
#                 'form':form,
#             }
#             form = City_Choice_Form(request.POST or None)
#             if form.is_valid():
#                 form.save()
#             return render(request, "user/input.html", context)
#     else:
#         return redirect('user-home')

def input_view(request):
    Lat_Lon()
    if request.user.is_authenticated:
        if request.method == 'POST':
            client_cities=City_Choice_Form(request.POST)
            if client_cities.is_valid():
                n = client_cities.cleaned_data.get("citi")
                k=client_cities.cleaned_data.get('k')
                cnt_citi=len(n)
                weights=calc_weights()
               
                #now create the adj matrix

                dist = [0]*cnt_citi
                centers = []

                x1=City.objects.get(name='Mumbai').x_coordinate
                y1=City.objects.get(name='Mumbai').y_coordinate

                x2=City.objects.get(name='Kolkata').x_coordinate
                y2=City.objects.get(name='Kolkata').y_coordinate

                #initial folium map
                m=folium.Map(width=1600,height=500,location=get_center_coordinates(x1,y1,x2,y2),zoom_start=8)

                # user chosen cities (n)marker
                for i in n:
                    c=City.objects.get(id=i)
                    folium.Marker(
                        [c.x_coordinate,c.y_coordinate], popup=c.name, tooltip="Your selected cities(Stores location)",icon=folium.Icon(color="purple")
                    ).add_to(m)

            
                for i in range(cnt_citi):
                    dist[i] = 10**9
                # index of city having the
                # maximum distance to it's
                # closest center
                max = int(n[0])
                print(max)
                for i in range(k):
                    centers.append(max)
                    for j in range(cnt_citi):
                        dist[j] = min(dist[j], weights[max][j])
                    max = 0
                    for p in range(cnt_citi):
                        if (dist[p] > dist[max]):
                            max = p
                context={}
                warehouse_list=[]
                context['max_dist']=dist[max]
                for i in centers:        
                    # warehouse_list.append(n[i])
                    warehouse_list.append(City.objects.get(id=n[i]).name)
                    # print(warehouse_list)
                context['warehouse_list']=warehouse_list

                for i in warehouse_list:
                    #warehouse marker
                    c=City.objects.get(name=i)
                    folium.Marker(
                        [c.x_coordinate,c.y_coordinate], popup=c.name, tooltip="Warehouse location",icon=folium.Icon(color="red")
                    ).add_to(m)

                    
                l=[]
                for i in n:
                    c1=City.objects.get(id=i)
                    l.append(c1.name)

                for i in warehouse_list:
                    if i in l:
                        l.remove(i)

                for i in l:
                    for j in warehouse_list:
                        c1=City.objects.get(name=i)
                        c2=City.objects.get(name=j)
                        pointA=(c1.x_coordinate,c1.y_coordinate)
                        pointB=(c2.x_coordinate,c2.y_coordinate)
                        line = folium.PolyLine(locations=[pointA, pointB], weight=4, color='blue')
                        m.add_child(line)
                
                m=m._repr_html_()
                context['map']=m
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
