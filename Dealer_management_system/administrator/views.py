from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from Dealer.models import Order,Product_in
from django.db.models import Q
from .models import Product
from Dealer.forms import OrderForm,Product_inForm

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
			return redirect('administrator_home')
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


def administrator_home(request):
	Pending_order=Order.objects.filter(Order_Status='Pending').count()
	Send_back_order=Order.objects.filter(Order_Status='Send_back').count()
	Approved_order=Order.objects.filter(Q(Order_Status = 'Approved') | Q(Order_Status = 'delivering')).count()
	delivered_order=Order.objects.filter(Order_Status='delivered').count()
	context={
		'Pending_order':Pending_order,
		'Send_back_order':Send_back_order,
		'Approved_order':Approved_order,
		'delivered_order':delivered_order,
		}
	return render(request,'administrator/administrator_home.html',context)

def administrator_Send_back_order_view(request):
	order=Order.objects.filter(Order_Status='Send_back')
	count_o=order.count()
	if(count_o==0):
		context={
			'warning':'No orders',
		}
	else:
		context={
		'order':order,
		
		}
	return render(request,'administrator/administrator_order_view.html',context)

def administrator_Approved_order_view(request):

	order=Order.objects.filter(Q(Order_Status = 'Approved') | Q(Order_Status = 'delivering'))
	 

	count_o=order.count()
	if(count_o==0):
		context={
			'warning':'No orders',
		}
	else:
		context={
		'order':order,
		
		}
	return render(request,'administrator/administrator_order_view.html',context)

def administrator_delivered_order_view(request):
	order=Order.objects.filter(Order_Status='delivered')
	count_o=order.count()
	if(count_o==0):
		context={
			'warning':'No orders',
		}
	else:
		context={
		'order':order,
		
		}
	return render(request,'administrator/administrator_order_view.html',context)

def administrator_Pending_order_view(request):
	order=Order.objects.filter(Order_Status='Pending')
	count_o=order.count()
	if(count_o==0):
		context={
			'warning':'No orders',
		}
	else:
		context={
		'order':order,
		
		}
	return render(request,'administrator/administrator_order_view.html',context)

def administrator_Get_details(request,pk):
	order_d=Order.objects.get(order_id=pk)
	Product_s=Product_in.objects.filter(order_in=order_d)
	form = OrderForm(instance=order_d)
	if request.method == 'POST':
		form = OrderForm(request.POST,instance=order_d)
		if form.is_valid():
			form.save()
			return redirect('administrator_home')

	context = {'form':form,
	'Product_s':Product_s,
	'order_d':order_d,}
	return render(request, 'administrator/administrator_order_update&details.html', context)
	
