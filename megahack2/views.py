from django.shortcuts import render, redirect
from .forms import contact
from .models import contactForm, sponsor, speaker, gallery, youtube_link , code_of_conduct, rule, view_poster,registration_five, registration_one, registration_two, registration_three, registration_four,step_one,step_two,step_three
# Create your views here.
def index(request):
    spnsr=sponsor.objects.filter(available=True)
    form = contact()
    spkr=speaker.objects.filter(available=True)
    galry=gallery.objects.filter(available=True)
    utube_lnk=youtube_link.objects.filter(available=True)
    coc=code_of_conduct.objects.filter(available=True)
    rul=rule.objects.filter(available=True)
    vp=view_poster.objects.filter(available=True)
    if request.method=="POST":
        form=contact(request.POST)
        if form.is_valid():
            myform=contactForm(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                query=form.cleaned_data['query'],
                message=form.cleaned_data['message'],
                mobile_number=form.cleaned_data['mobile_number'],
            )
            myform.save()
    context={
        'form':form,
        'sponsor':spnsr,
        'gallery':galry,
        'youtube':utube_lnk,
        'speaker':spkr,
        'code_of_conduct':coc,
        'rule':rul,
        'view_poster':vp,
    }            
    return render(request,"index.html",context)

def team(request):
    return render(request,"team.html")

def register(request):
    r1=registration_one.objects.filter(available=True)
    r2=registration_two.objects.filter(available=True)
    r3=registration_three.objects.filter(available=True)
    r4=registration_four.objects.filter(available=True)
    r5=registration_five.objects.filter(available=True)
    s1=step_one.objects.filter(available=True)
    s2=step_two.objects.filter(available=True)
    s3=step_three.objects.filter(available=True)
    context={
        'r1':r1,
        'r2':r2,
        'r3':r3,
        'r4':r4,
        'r5':r5,
        's1':s1,
        's2':s2,
        's3':s3,
    }
    return render(request,"register.html",context)    