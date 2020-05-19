from django.http import HttpResponse
from django.shortcuts import render
def show(request):
    #return HttpResponse("Hello World")
    return render(request,'index.html')
def showLogin(request):
    return render(request,'Login.html')
def showSignup(request):
        return render(request, 'Signup.html')
def showDashboard(request):
    u=request.POST['id']
    p=request.POST['psw']
    if request.method == "POST" and u=="rajatchoudhary310@gmail.com" and p=="123456":
        return render(request, 'dashboard.html')
    elif request.method == "POST" and u=="1611981295" and p=="123456":
        return render(request, 'studentDashboard.html')
    else:
        return render(request, 'Signup.html')
def showSubject(request):
    return render(request,'Subject.html')
def showStudent(request):
    return render(request,'Student.html')
def showExamination(request):
    return render(request,'Examination.html')
def showDepartment(request):
    return render(request,'Department.html')
def showQuestions(request):
    return render(request,'Questions.html')
def showstudentDashboard(request):
    return render(request,'studentDashboard.html')
def showstudentExamination(request):
    return render(request,'studentExamination.html')
def showstudentProfile(request):
    return render(request,'studentProfile.html')
def showstudentSubject(request):
    return render(request,'studentSubject.html')

