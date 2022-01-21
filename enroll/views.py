from http.client import HTTPResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import addtech, user1, addgit as  adgit 
# from .forms import regi
# from .forms import update


# Create your views here.
def index(request):
    """
    if request.method =='POST':
        fm = regi(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = regi()
    """
    if request.method == "POST":
        pname, members, ptech, deadline, vcont, cicd = request.POST.get('pname',False),  request.POST.get('members',False), request.POST.get('ptech', False),request.POST.get('deadline', False),request.POST.get('vcont', False),request.POST.get('cicd', False),
        user1.objects.create(pname=pname,members=members,ptech=ptech,deadline=deadline,vcont=vcont,cicd=cicd).save()
        # print(name, email, password)
        # print(request.POST)
      
          
    params = {
        "user1s":user1.objects.all(),
        }
    return render(request,'index.html',params)
    # return HTTPResponse("<h1>lgkhj</h1>")

def update(request):
    """
    form = updt()
    form1 = regi(request.POST)
    if request.method=='POST':
        print('printing post', request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form1}
    """
    # if request.method == "get":
    #     pass
        # id
        # var = user1.objects.filter(id)
    return render (request,'update.html') 


   #addtech
def adtech(request):
    if request.method == "POST":
        techname=request.POST.get('techname',False)
        addtech.objects.create(techname=techname).save()
    def __str__(self):
        return str(self.tech)
        # print(addtech)
    pams = {
        "adtec":addtech.objects.all(),
        }
    return render (request,'addtech.html')

def home(request):
    return render(request,'homee.html')

def tech(request):
    return render(request,'tech.html')

def git(request):
    return render(request,'git.html',{"gits":adgit.objects.all()})

def addgit(request):
    if request.method == "POST":
        git1=request.POST.get('git2',False)
        adgit.objects.create(gitplat=git1).save()
        # if addgit:
        #     message = "Git platform added succesfully"
            # print(message)
        messages.success(request,f"Success {git1}")
    return render(request,'addgit.html',{"adgit":adgit.objects.all()})

def style(request):
    return render(request,'styling.html')

#update project
def update_project(request,id):
    old_project = None
    try:
        old_project = Projects.objects.get(id=id)
    except:
        pass
    if old_project:
        if request.method == 'POST':
            form = AddProjectForm(request.POST,request.FILES,instance=old_project)
            if form.is_valid():
                form.save()
                messages.success(request,update_success_message('project'))
                return redirect('home_page')
            else:
                print(form.errors)
                messages.warning(request,INVALID_DATA_MESSAGE)
        else:
            form = AddProjectForm(instance=old_project)
        context = {
            PAGE_HEADING:'Update project','form': form
        }
    else:
        messages.warning(request,entry_not_found_message('Project'))
        return redirect('home_page')
    return render(request, 'employees/common_add_detail_form_template.html', context=context)
