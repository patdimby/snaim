from django.shortcuts import render

# Create your views here.
def home(request):
    """" Home page."""
    return render(request, 'blog/index.html')