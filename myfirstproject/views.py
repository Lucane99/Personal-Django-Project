from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .form import userForm
from typing import Dict,Any
from service.models import Topics
from news.models import News
from django.core.paginator import Paginator
from contactenquiry.models import contactEnquiry
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


def homepage(request):

    # subject='Testing Mail'
    # from_email='lucaneryr123@gmail.com'
    # message='<p>Arsenal<b>FC!</b></p>'
    # to_email='lucaneryr123@gmail.com'
    # email=EmailMultiAlternatives(subject,message,from_email,[to_email])
    # email.content_subtype='html'
    # email.send()







#     send_mail(
#     "Testing Mail",
#     "Arsenal.",
#     "lucaneryr123@gmail.com",
#     ["lucaneryr123@gmail.com"],
#     fail_silently=False,
# )
    newsData=News.objects.all()
    # data={
    #     'title':'Arsenal',
    #     'bdata':'Gwa Wan My Familam',
    #     'clist':['php','java','django'],
    #     'numbers':[1,2,3,4,5],
    #     'student_details':[
    #         {'name':'pradeep','phone':11111},
    #         {'name':'testing','phone':44444}
    #     ]
    # }
    # return render(request,"index.html",data)
    # topicData=Topics.objects.all().order_by('id')
    # topicData=Topics.objects.all().order_by('id')[0:2]
    topicData=Topics.objects.all()
    paginator=Paginator(topicData,1)
    page_number=request.GET.get('page')
    topicDatafinal=paginator.get_page(page_number)
    totalpage=topicDatafinal.paginator.num_pages

    if request.method=="GET":
        tt=request.GET.get('topicname')
        if tt!=None:
            # topicData=Topics.objects.filter(topic_title=tt)
            topicDatafinal=Topics.objects.filter(topic_title__icontains=tt)



    # for tabledata in topicData:
    #     print(tabledata.topic_icon)

    # print(topicData)
    data={
        'topicData':topicData,
        'topicDatafinal':topicDatafinal,
        'lastpage':totalpage,
        'totalPageList':[n+1 for n in range(totalpage)],
        'newsData':newsData
    }
    return render(request,"index.html",data)
# def newsDetails(request,newsid):
def newsDetails(request,slug):
    # print(newsid)
    newsDetail=News.objects.get(news_slug=slug)
    data={
        'newsDetails':newsDetail
    }
    return render(request,"newsdetail.html",data)


def contact(request):
    if request.method=='GET':
        output=request.GET.get('output')
    return render(request,"contact.html",{'output':output})

def saveEnquiry(request):
    sucess=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        project=request.POST.get('message')
        data=contactEnquiry(name=name,email=email,subject=subject,project=project)
        data.save()
        sucess='Data inserted Sucessfully'



    return render(request,"contact.html",{'sucess':sucess})



def topicDetail(request):
    return render(request,"topics-detail.html")

def topicListing(request):
    return render(request,"topics-listing.html")

def userform(request):
    finalans=0
    fn=userForm()
    data={'form':fn}
    
    
    try:
        if request.method=="POST":
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
            # n1=int(request.GET.get('num1'))
            n1=int(request.POST.get('num1'))
            # n2=int(request.GET.get('num2'))
            n2=int(request.POST.get('num2'))
        # print(n1+n2)
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'form':fn,
                'output':finalans
            }
            url="/contact/?output={}".format(finalans)

            # return HttpResponseRedirect(url)
            return redirect(url)
            
            
         
    except:
        pass

    return render(request,"userform.html",data)


def submitform(request):
    finalans=0
    data={}
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1')) 
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            return HttpResponse(finalans)
    except:
        pass

def calculator(request):
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                output=n1+n2
            elif opr=="-":
                output=n1-n2
            elif opr=="*":
                output=n1*n2
            else:
                output=n1/n2
            

             
    except:
        output="Invalid Operation"
    print(output) 
    return render(request,"calculator.html",{'output':output,'n1':n1,'n2':n2})

def evenodd(request):
    output=""
    try:
        if request.method=="POST":
            if request.POST.get('num')=='':
                return render(request,"evenodd.html",{'error':True})
            n=int(request.POST.get('num'))
            if (n % 2)==0:
                output="Even"
            else:
                output="Odd"
    except:
        output="Invalid"
    return render(request,"evenodd.html",{'output':output})

def marksheet(request):
    if request.method=="POST":
            m1=eval(request.POST.get('eng'))
            m2=eval(request.POST.get('maths'))
            m3=eval(request.POST.get('sci'))
            m4=eval(request.POST.get('comp'))
            total=(m1+m2+m3+m4)*100
            percentage=total/400
            print(percentage)
            if percentage>=80:
                output="Distinction"
            elif 70<=percentage<=79:
                output="First Division"
            elif 60<=percentage<=69:
                output="Second Division"
            elif 40<=percentage<=59:
                output="Third Division"
            else:
                output="Fail"
            data={'m1':m1,
          'm2':m2,
          'm3':m3,
          'm4':m4,
          'percentage':percentage,
          'output':output}
            return render(request,"marksheet.html",data)
    return render(request,"marksheet.html",data)


   
    
   
   
        





# def aboutUS(request):
#     return HttpResponse("<b>Gwa Wan</b>")

# def courses(request):
#     return HttpResponse("My G!")

# def coursesDetails(request,courseid):
#     return HttpResponse(courseid)




