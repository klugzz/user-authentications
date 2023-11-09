from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def index(request):
	return render(request,'apps/index.html')
def home(request):
	return render(request,'apps/services.html')
@login_required
def service(request):
	return render(request,'apps/services.html')
def gallery(request):
	return render(request,'apps/gallery.html')
def contact(request):
	return render(request,'apps/contact.html')
# Create your views here.
