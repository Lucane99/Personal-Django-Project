"""
URL configuration for myfirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myfirstproject import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='home'),
    path('contact/', views.contact,name='contact'),
    path('topic-detail/', views.topicDetail,name='topicdetail'),
    path('topic-listing/', views.topicListing,name='topiclisting'),
    path('userform/', views.userform,name='userform'),
    path('submitform/', views.submitform,name='submitform'),
    path('calculator/', views.calculator,name='calculator'),
    path('evenodd/', views.evenodd,name='evenodd'),
    path('marksheet/', views.marksheet,name='marksheet'),
    # path('newsdetail/<newsid>', views.newsDetails,name='newsdetail'),
    path('newsdetail/<slug>', views.newsDetails,name='newsdetail'),
    path('saveform/', views.saveEnquiry,name='saveenquiry'),
   
    # path('about-us/', views.aboutUS),
    # path('courses/', views.courses),
    # path('courses/<slug:courseid>', views.coursesDetails),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
