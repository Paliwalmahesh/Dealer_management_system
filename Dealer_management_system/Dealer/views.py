from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import OrderForm,Product_inForm,Product_in_Form
from .models import Order,Product_in

def Dealer_Signin(request):
	if request.method=='POST':
		username = request.POST['usernames']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('Dealer_home')
		else:
			return render(request,'Dealer/Dealer_Signin.html',{'i':'Invalid username or Password'})

	else:
		return render(request,'Dealer/Dealer_Signin.html')
	

def Dealer_Signup(request):
	if request.method == 'POST':
		first_name = request.POST['First_name']
		last_name = request.POST['Last_name']
		username = request.POST['username']
		email = request.POST['Email']
		password1 = request.POST['Password']
		password2 = request.POST['Password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				return render(request,'Dealer/Dealer_Signup.html',{'i':'user already exsist'})
			else:
				users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
				group = Group.objects.get(name= 'Dealer')
				group.user_set.add(users)
				users.save()
				return redirect('Dealer_Signin')
		else:
			 return render(request,'Dealer/Dealer_Signup.html',{'i':'Passwords are not same'})
	else:
		 return render(request,'Dealer/Dealer_Signup.html')
def Dealer_home(request):
	return render(request,'Dealer/Dealer_home.html')

def Dealer_order(request):
	Cost=0
	username = request.user
	Order_add=Order(cost=Cost,user_order=username)
	Order_add.save()
	
	print(Order_add.order_id)
	return redirect("Dealer_add_product",Order_add.order_id)

def Dealer_delete_product(request, pk):
	product_in_delete= Product_in.objects.get(Product_in_id=pk)
	if request.method == "POST":
		Id = product_in_delete.order_in.order_id
		product_in_delete.delete()
		return redirect("Dealer_add_product",Id)
	context = {'product_in_delete':product_in_delete}
	return render(request, 'Dealer/Dealer_delete_product.html', context)

def Dealer_update_product(request,pk):
	product_in_update = Product_in.objects.get(Product_in_id=pk)
	form = Product_in_Form(instance=product_in_update)
	if request.method == 'POST':
		Id = product_in_update.order_in.order_id
		form = Product_in_Form(request.POST,instance=product_in_update)
		if form.is_valid():
			product_in_update=form.save(commit=False)
			product_in_update.Total_cost=(product_in_update.Quantity*product_in_update.Product_in_def.Cost)
			product_in_update.save()
			return redirect("Dealer_add_product",Id)

	context = {'form':form}
	return render(request, 'Dealer/Dealer_update_product_form.html', context)

def Dealer_add_product(request,pk):
	order=Order.objects.get(order_id=pk)
	product_in_show=Product_in.objects.filter(order_in=order)
	form=Product_inForm()
	grand_total=0

	if request.method=='POST':
		context={
			'form':form,
			'order':order,
			'product_in_show':product_in_show,
		}
		form=Product_inForm(request.POST)
		if form.is_valid():
			product_in_add=form.save(commit=False)
			product_in_add.order_in=order
			product_in_add.Total_cost=(product_in_add.Quantity*product_in_add.Product_in_def.Cost)
			product_in_add.save()
			for i in product_in_show:
				grand_total+=i.Total_cost
			order.cost=grand_total
			return render(request,'Dealer/Dealer_order_view.html',context)
	else:
		for i in product_in_show:
			grand_total+=i.Total_cost
			order.cost=grand_total
		context={
		'form':form,
		'order':order,
		'product_in_show':product_in_show,
		}
		return render(request,'Dealer/Dealer_order_view.html',context)