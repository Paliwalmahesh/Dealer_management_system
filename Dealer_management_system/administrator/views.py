from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'administrator/home.html')

    
def administrator_Signin(request):
	if request.method=='POST':
		username = request.POST['usernames']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('Doctor_done')
		else:
			return render(request,'administrator/administrator_Signin.html',{'i':'Invalid username or Password'})

	else:
		return render(request,'administrator/administrator_Signin.html')
	

def administrator_Signup(request):
	if request.method == 'POST':
		first_name = request.POST['First_name']
		last_name = request.POST['Last_name']
		username = request.POST['username']
		email = request.POST['Email']
		password1 = request.POST['Password']
		password2 = request.POST['Password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				return render(request,'administrator/administrator_Signup.html',{'i':'user already exsist'})
			else:
				users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
				group = Group.objects.get(name= 'Administrator')
				group.user_set.add(users)
				users.save()
				return redirect('administrator_Signin')
		else:
			 return render(request,'administrator/administrator_Signup.html',{'i':'Passwords are not same'})
	else:
		 return render(request,'administrator/administrator_Signup.html')
