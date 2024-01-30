from django.shortcuts import render
from django.contrib import messages
from careers_web.models import Careers_hub
from careers_web.models import Career_feedback


def home(request):
    career_records=Careers_hub.objects.all()
    feedback_records=Career_feedback.objects.filter(status="Approved")
    context={'feedback_records':feedback_records,'career_records':career_records}
    if request.method=="POST":
        f_name=request.POST.get('f_name')
        f_email=request.POST.get('f_email')
        f_rating=int(request.POST.get('f_rating'))
        feedback=request.POST.get('feedback')
        obj=Career_feedback(fullname=f_name,email=f_email,rating=f_rating,feedback=feedback)
        obj.save()
        messages.info(request,'Feedback inserted successfully')
        return render(request,'index.html',context)

    return render(request,'index.html',context)