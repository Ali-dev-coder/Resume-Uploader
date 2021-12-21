from django.shortcuts import render,HttpResponseRedirect
from .forms import  Resumeform
from .models import Resumemodel
# Create your views here.
def resumeviews(request):
    if request.method=="POST":
        fm = Resumeform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')

    else:
        fm = Resumeform()
    stu = Resumemodel.objects.all()          
    return render(request, 'home.html',{'form':fm,'candidates':stu})

def resumedetailviews(request,pk):
    stu = Resumemodel.objects.get(pk=pk)
    return render(request, 'detail_resume.html',{'candidatedetail':stu})
