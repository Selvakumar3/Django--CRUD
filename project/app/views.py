from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Details

# homepage function
def index(request):
    return render(request,'register.html')

# create function for CRUD
def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['birthday']
        gender=request.POST['gender']
        degree=request.POST['Degree']
        address=request.POST['address']
        image=request.FILES.get('image') 
        obj=Details.objects.create(name=name,age=age,gender=gender,degree=degree,address=address,image=image)
        obj.save()
        return redirect('retrieve')

# view function for CRUD
    
def retrieve(request):
    details=Details.objects.all()
    return render(request,'retrieve.html',{'details':details})

# edit function for CRUD
def edit(request,id):
    object=Details.objects.get(id=id)
    return render(request,'update.html',{'object': object})

# update function for CRUD  
def update(request,id):
    obj=Details.objects.get(id=id)
    if request.method=="POST":
        obj.name=request.POST['name']
        obj.age=request.POST['age']
        obj.gender=request.POST['gender']
        obj.degree=request.POST['degree']
        obj.address=request.POST['address']
        obj.image=request.POST['image']
        obj.save()
        return redirect('retrieve')   

# delete function for CRUD
def delete(request,id):
    object = Details.objects.get(id=id)
    object.delete()
    return redirect('retrieve')


