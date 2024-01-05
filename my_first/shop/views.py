from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil

# Create your views here.
def page(request):
     # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}

    return render(request,'index.html',params)
def contact(request):
    #getting the data from form
    if(request.method=="POST"):
       name=request.POST.get("name","")
       email=request.POST.get("eamil","")
       phone=request.POST.get("phone","")
       desc=request.POST.get("desc","")
       #writing into database
       contact=Contact(name=name,email=email,phone=phone,desc=desc)
       contact.save()
    return render(request,"contact.html")

def about(request):
    return render(request,"about1.html")
def viewproduct(request, myid):
    # fetch the product using the id
   products= Product.objects.filter(id=myid)


   return render(request,"viewproduct.html",{"product":products[0]})
def checkout(request):
    return render(request,"checkout.html")
