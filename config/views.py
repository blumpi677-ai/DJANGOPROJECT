from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

def jobs_page(request):
    return render(request, 'jobs.html')

def dashboard(request):
    return render(request, 'dashboard.html')
def post_job(request):
    return render(request, 'post_job.html')