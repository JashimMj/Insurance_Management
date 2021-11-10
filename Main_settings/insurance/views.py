from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request,'dashboard.html')

def maindashboardV(request):
    return render(request,'pages/maindashboard.html')

def admindashboardV(request):
    return render(request,'pages/admin/admindashboard.html')

def companyandbranchV(request):
    Coinfo=BranchInformationM.objects.all()[:1]
    return render(request,'pages/admin/forms/companyandbranch.html',{'Coinfo':Coinfo})

def CompanySaveV(request):

    if request.method == 'POST' and request.FILES:
        cname = request.POST.get('cname')
        names = request.POST.get('bname')
        addresss = request.POST.get('baddress')
        snames = request.POST.get('sname')
        phones = request.POST.get('pnumber')
        faxs = request.POST.get('fnumber')
        emails = request.POST.get('enumber')
        bcodes = request.POST.get('bcode')
        image = request.FILES['clogo']
        store = FileSystemStorage()
        filename = store.save(image.name, image)
        profile_pic_url = store.url(filename)
        data = BranchInformationM(Branch_Name=names, Address=addresss, Short_Name=snames, Phone=phones, Fax=faxs,
                                  Email=emails, Branch_Code=bcodes, BranchLogo=filename, Company_Name=cname)
        data.save()
        messages.info(request, 'Data Saved')
    else:
        cname = request.POST.get('cname')
        names = request.POST.get('bname')
        addresss = request.POST.get('baddress')
        snames = request.POST.get('sname')
        phones = request.POST.get('pnumber')
        faxs = request.POST.get('fnumber')
        emails = request.POST.get('enumber')
        bcodes = request.POST.get('bcode')
        data = BranchInformationM(Branch_Name=names, Address=addresss, Short_Name=snames, Phone=phones, Fax=faxs,
                                  Email=emails, Branch_Code=bcodes, Company_Name=cname)
        data.save()
        messages.info(request, 'Data Saved')

    Coinfo = BranchInformationM.objects.all()[:1]
    return render(request,'pages/admin/report/company.html',{'Coinfo':Coinfo})

    # return HttpResponse('abc')



