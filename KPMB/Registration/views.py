from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from Registration.models import Course, Student


# Create your views here.
def index (request):
    return render (request, "index.html")

def new_course (request):
    if request.method =='POST':
        c_code=request.POST['code']
        c_desc=request.POST['desc']
        
        find_data=Course.objects.filter(code=c_code).values()
          
        if find_data.count()==0:
            data=Course(code=c_code, description=c_desc)
            data.save()
            dict={
                'message':"data save"
            }
        else:         
            dict={
                    'message':"Course " + find_data[0]['code'] + " already exsis"
                } 
    else:
        dict={
            'message':''
        }
    return render (request, "new_course.html", dict)

def course(request):
    data=0
    all_course=Course.objects.all().values()
    if all_course.count()!=0:
        data=1
        dict={
            'all_course':all_course,
            'data':data
        }
    else:
        dict={
             'data':data
        }
    
    return render(request,"course.html", dict)

def search_course(request):
    if request.method == 'GET':
        data = Course.objects.filter(code = request.GET.get("c_code"))
        dict={
                'data' : data,
            }      
        return render (request,"search_course.html",dict)  
    else:
        return render (request,"search_course.html")

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict={
        'data':data
    }
    return render(request, "update_course.html", dict)

def save_update_course (request,code):
    c_desc=request.POST['desc']
    data=Course.objects.get(code=code)
    data.description=c_desc
    data.save()
    return HttpResponseRedirect (reverse("course"))

def delete_course(request,code):
    data=Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect (reverse("course"))

def student(request):
    data=0
    all_student=Student.objects.all().values()
    if all_student.count()!=0:
        data=1
        dict={
            'all_student':all_student,
            'data':data
        }
    else:
        dict={
             'data':data
        }
    return render(request, "student.html", dict)

def new_student(request):
    all_course=Course.objects.all().values()
    if request.method =='POST':
        s_id=request.POST['id']
        s_name=request.POST['name']
        s_address=request.POST['address']
        s_phone=request.POST['phone']
        s_course=request.POST['c_course']
                
        find_data=Student.objects.filter(id=s_id).values()
          
        if find_data.count()==0:
            c_code=Course.objects.get(code=s_course)
            data=Student(id=s_id, name=s_name,address=s_address,phone=s_phone, course_code=c_code)
            data.save()
            dict={
                'message':"data save",
                'all_course':all_course
            }
        else:         
            dict={
                    'message':"Course " + find_data[0]['id'] + " already exsis",
                    'all_course':all_course
                } 
    else: 
        dict={
            'all_course':all_course
        }
    return render(request, "new_student.html",dict)

def update_student(request,s_id):
    all_course=Course.objects.all().values()
    data=Student.objects.get(id=s_id)

    dict={
        'data':data,
        'all_course':all_course
    }
    return render(request, "update_student.html", dict)

def save_update_student (request,s_id):
    s_name=request.POST['name']
    s_address=request.POST['address']
    s_phone=request.POST['phone']
    s_course=request.POST['c_course']
    data=Student.objects.get(id=s_id)
    data.name= s_name
    data.address=s_address
    data.phone=s_phone
    data.course_code_id=s_course
    data.save()
    return HttpResponseRedirect (reverse("student"))

def search_student(request):
    if request.method == 'GET':
        data = Student.objects.filter(id = request.GET.get("s_id"))
        dict={
                'data' : data,
            }      
        return render (request,"search_student.html",dict)  
    else:
        return render (request,"search_course.html")

def delete_student(request,s_id):
    data=Student.objects.get(id=s_id)
    data.delete()
    return HttpResponseRedirect (reverse("student"))
