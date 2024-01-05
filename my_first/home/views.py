from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
   #return render(request,"hello.html",{"name":"laiba"})
 file=open("home/1.txt","r+")
 c=file.read()
 return HttpResponse(c)

def feedback(request):
   #get the text
   djtext=request.POST.get("text","default")
   print(djtext)
   # for remove  punctuation
   punctuate=".,?!:;“”'()[]{}...-—/'&%$@#*+_=<>|~`"
   analyze=""
   COUNT=0
   for char in djtext:
    if char not in punctuate:
      analyze=analyze+char
    # for upper case
      analyze= djtext.upper()
   # for same line
    elif char!="/n":
      analyze=analyze+char
   # for space remover
    elif char!=" ":
      analyze=analyze+char
    COUNT=len(''.join(djtext.split()))  # ''.jointhis means you're concatenating the list of words without spaces.
   
   params={"purpose":"punctuate", "text":analyze ,"COUNT":COUNT}
   return render(request,"feedback.html",params)
def about(request):
   # return HttpResponse(" about page <a href='/'>back</a>")
   return render(request,"about.html")
