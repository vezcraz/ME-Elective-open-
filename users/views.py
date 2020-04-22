from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student_Info
from .forms import electives
from form.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect
from .authenticate_backend import LDAPAuthBackend 
from users.tools.export import *
@login_required
def profile(request):
	template_name = 'users/profile.html'
	print("YES")
	if request.method == 'GET':
		
		ID = request.user.username
		print("In users/views, GET request")
		regfor=regSem.objects.all()[0]
		year=int(regfor.Academic_year_start)-int(ID[0:4])+1
		sem=int(regfor.Registration_for_sem)
		temp=[]
		coursesForBranch=courseList.objects.filter(BranchCode=ID[4:8], Type='CDC')

		for course in coursesForBranch:
			for x in cdc.objects.filter(Year=year, Sem=sem):
				if x.CourseCode==course.CourseCode:
					temp.append({'CourseNo':x.CourseCode, 'CourseName':x.CourseName})
					break
		validCourses=[]
		flag=1
		for course in courseOffered.objects.filter(Tag=ID[4:8]+'EL'):
			flag=1
			for x in stuCourseData.objects.filter(CampusID=ID):
				if course.CourseCode == x.CourseCode:
					flag=0
					break
			if flag==1:
				validCourses.append({'CourseCode':course.CourseCode,'CourseName':course.CourseName})
		isFinal=['0']
		if len(temp)==0:
			isFinal=['1']
		print(isFinal)
		context={
		'final':isFinal,
		'cdc': temp,
		'courses_offered':validCourses,
		'stuList':stuCourseData.objects.filter(CampusID=ID)
		}

		return render(request, template_name,context)
	if request.method == 'POST':
		# form = electives(request.POST) #now i have all the details of the form: form.elective1 etc.
		# if form.is_valid():
		student_info = Student_Info()

		for x in Student_Info.objects.all():
			if x.user==request.user:
				student_info=x

			# f=form.cleaned_data.get(f) // what the f*** is this?
		ID=request.user.username
		student_info.user = request.user
		student_info.Identity=ID
		for data in stuCourseData.objects.filter(CampusID=ID):
			student_info.user.first_name=data.Name
			break
		student_info.name=student_info.user.first_name

		pref_dict=request.POST
		print(pref_dict)
		student_info.p=""
		temp=""
		test_list=[]
		for pref_no,option in pref_dict.items():
			if pref_no[0]=='P':
				temp=temp+f"{pref_no}|{option}**" # '|' separates preference number and options and '**' separates 2 preferences from each other
				test_list.append(option)
		student_info.p=temp
		print(student_info.p)
		print(test_list)
		if len(test_list)==0:
			messages.warning(request, f'You are required to fill all the fields')
			return redirect('profile')
		for x in test_list:
			if x == "---":
				messages.warning(request, f'You are required to fill all the fields')
				return redirect('profile')
		true_list=[]
		for val in test_list:
			if val!="---":
				true_list.append(val)
		print(true_list)
		if len(set(true_list)) != len(true_list):
			messages.warning(request, f'Please Fill Unique Preferences')
			return redirect('profile')
		student_info.save()
		student_info=Student_Info()
		return redirect('pref')

def exp(request):
	if request.method=='GET':
		return render(request, 'users/export.html')
	if request.method=='POST':
		if request.user.is_superuser:
			print(request.POST['type'])
			response=getFile(request, int(request.POST['type']))
		else:
			response=HttpResponse("You don't have acces to this page")
	return response
@login_required
def pref(request):
	ID = request.user.username
	x= Student_Info.objects.filter(user=request.user)[0]
	final=[]
	temp={}
	pref_list=x.p.split('**')
	for preference in pref_list:
	    if preference!='':
	        print(preference.split('|'))
	        pno=preference.split('|')[0][-1]
	        opn=preference.split('|')[-1]
	        temp['a']=pno
	        temp['b']=opn
	        final.append(temp)
	        temp={}
	print(final) # a list of dictionary containing preference no. and preference of the requested user
	context={
	'studentInfo':final
	
	}
	return render(request, 'users/pref.html',context)
			


@csrf_protect
def loginform(request):

    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/admin')
        else:
            return redirect('profile')

    if request.POST:
        u = request.POST.get('username')
        password = request.POST.get('password')
        username="f"+ u[0:4]+ u[8:-1]
        print(username)
	
        ldap = LDAPAuthBackend()
        user = ldap.authenticate(request, username=username, password=password, x=u)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin')
            else:
                return redirect('profile')
        else:
            messages.add_message(request, messages.INFO,  "Incorrect username or password", extra_Codes='red')
            print('Not able to authenticate')

    return render(request, "users/login.html", {})
