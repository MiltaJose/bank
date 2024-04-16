from django.shortcuts import render,redirect
from .models import Branch1,District,City
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import get_object_or_404
from .forms import DerDrop
from django.http import JsonResponse
import json

# Create your views here.
def cities(request):
    data = json.loads(request.body)
    district_id = data["id"]
    print(district_id)
    cities = City.objects.filter(district__id=district_id)
    print(cities)
    return JsonResponse(list(cities.values("id", "name")),safe=False)

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('appln_btn')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def appln_btn(request):
    return render(request, 'appln_btn.html')
def appln(request):
    # city = City.objects.all()
    # obj = District.objects.all()
    f=DerDrop()
    if request.method == 'POST':
        f=DerDrop(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district_id = request.POST['district']
        city_id = request.POST['city']
        district = get_object_or_404(District, pk=district_id)
        city = get_object_or_404(City, pk=city_id)
        account_type = request.POST['account']
        material_provide = request.POST.getlist('material')
        branch1 = Branch1(first_name=first_name, last_name=last_name, district=district, city=city,date_of_birth=date_of_birth, age=age, gender=gender, phone_number=phone_number, email=email, address=address, account_type=account_type, material_provide=material_provide)
        branch1.save()
        return redirect('home')
    return render(request, 'appln.html',{'form':f})


def home(request):
    return render(request,'home.html')