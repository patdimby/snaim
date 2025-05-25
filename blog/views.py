from django.shortcuts import render

# Create your views here.
def home(request):
    """" Home page"""
    return render(request, 'pages/index.html')

def about(request):
    """" About page"""
    return render(request, 'pages/about.html')

def causes(request):
    """" Causes page"""
    return render(request, 'pages/causes.html')

def team(request):
    """" Team page"""
    return render(request, 'pages/team.html')

def service(request):
    """" Service page"""
    return render(request, 'pages/service.html')

def testimonial(request):
    """" Testimonial page"""
    return render(request, 'pages/testimonial.html')

def donate(request):
    """" Donate page"""
    return render(request, 'pages/donate.html')

def contact(request):
    """" Contact page"""
    return render(request, 'pages/contact.html')

def get404(request):
    """" Contact page"""
    return render(request, 'pages/404.html')