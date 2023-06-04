from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect
from app1.models import Table,Use
from app1.form import tbf,regfor
from app1.form import rf
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required

# Create your views here.

 
def home(request): 
    return render(request,'index.html')

def likepost(request, pk):
    use = get_object_or_404(Use, id=request.POST.get('post_id'))
    use.likes.add(request.user)
    return HttpResponseRedirect('/tabview/{}/'.format(pk))

def abt(request): 
    return render(request,'abt.html')


def tview(request): 
    Tab = Table.objects.all()
    sort = request.GET.get('sort')
    if sort == 'option1':
        Tab = Table.objects.filter(status=False).order_by('title')
    elif sort == 'option2':
        Tab = Table.objects.filter(status=True).order_by('title')
    else:
        Tab = Table.objects.all().order_by('-id')
    return render(request,'tview.html',{'Tab':Tab})

def logo(request): 
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def log(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            name=request.POST.get('username')
            pas=request.POST.get('password')
            user=authenticate(request,username=name,password=pas)
            if user is not None:
                login(request,user)
                messages.success(request,"successfullty logged in")
                return tview(request)
            else:
                return redirect('/Login/')
        return render(request,'login.html')

def reg(request):
    form=regfor()
    if request.method == 'POST':
        form=regfor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Login') 
    return render(request,'reg.html',{'form':form})

def tab(request):
    tab=Table.objects.all()
    use=Use.objects.all()
    if request.method == "GET":
        name=request.GET.get('search')
        if name:
            tabl=Table.objects.filter(title__icontains=name)
            if tabl:
                return render(request,'tab.html',{'table':tabl})
            else:
                a="not found"
                return render(request,'tab.html',{'a':a})
        else:
            a="provide the keyword"
            return render(request,'tab.html',{'a':a})
    return render(request,'tab.html',{'table':tab,'user':use})


def tabview(request,desc):
    tabv = get_object_or_404(Table, pk=desc)
    use = tabv.replies.all()
    rpf=rf()    
    if request.user.username and request.user.username == tabv.username:
        if request.method == 'POST':
            sta = request.POST.get('status')
            if sta == 'True':
                tabv.status = True
            elif sta == 'False':
                tabv.status = False
 
            checkb= request.POST.get('check')
            if checkb == 'True':
                tabv.checkbox = True
            elif checkb == 'False':
                tabv.checkbox = False
            tabv.save()
            
    else:
        pass    
    if request.method == 'POST' and not tabv.status:
        user = request.user.username
        message = request.POST.get('message')
        users = Use(user=user, table=tabv, message=message)
        users.save()
    return render(request, 'tablv.html', {'tabv': tabv,'user':use,'rf':rpf})

def rais(request):
    b = tbf()
    if request.method == 'POST':
        b = tbf(request.POST)
        if b.is_valid():
            instance = b.save(commit=False)
            instance.username = request.user.username
            instance.save()
            return tview(request)
    else:
        b = tbf(initial={'Username': request.user.username})

    return render(request,'raise.html',{'tbf':b})
    
