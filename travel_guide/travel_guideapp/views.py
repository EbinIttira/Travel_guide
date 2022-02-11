from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import myplaces
from.forms import updateform

def home(request):
    places=myplaces.objects.all()
    return render(request,'Home.html',{'placeskey':places})

def addplace(request):
    if request.method=='POST':
        district=request.POST.get('district')
        name=request.POST.get('place')
        desc=request.POST.get('desc')
        image=request.FILES['image']
        dbdata=myplaces(district=district,place=name,desc=desc,img=image)
        dbdata.save()
    return render(request,"addplace.html")

def placedetail(request,place_id):
    place=myplaces.objects.get(id=place_id)
    return render(request,"place_detail.html",{'placekey':place})

def update(request,place_id):
    place=myplaces.objects.get(id=place_id)
    form = updateform(request.POST or None,request.FILES,instance=place)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'place':place})