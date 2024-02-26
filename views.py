from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'welcome.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def login(request):
    if request.method=="POST":
        un=request.POST['fname']
        pwd=request.POST['1name']
        print("username=",un)
        print("username=",pwd)
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        fn=request.POST['firstname']
        mn=request.POST['middlename']
        ln=request.POST['lastname']
        phn=request.POST['phone']
        em=request.POST['email']
        ps=request.POST['pass']
        print("firstname=",fn)
        print("middlename=",mn)
        print("lastname=",ln)
        print("phone=",phn)
        print("email=",em)
        print("password=",ps)
    return render(request,'reg.html')
     