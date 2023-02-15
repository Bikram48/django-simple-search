from django.shortcuts import render

# Create your views here.
def create_login_view(request):
    return render(request, 'accounts/login.html', {})