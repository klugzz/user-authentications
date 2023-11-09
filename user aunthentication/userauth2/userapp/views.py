from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userapp.forms import SignUpForm
from django.http import HttpResponseRedirect
def index(request):
	return render(request,'apps/index.html')
def home(request):
	return render(request,'apps/home.html')
@login_required
def service(request):
	return render(request,'apps/service.html')
def gallery(request):
	return render(request,'apps/gallery.html')
def contact(request):
	return render(request,'apps/contact.html')
def logout(request):
	return render(request,'apps/logout.html')
def signup_view(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'apps/signup.html',{'form':form})


# Create your views here.
