from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('firstpage')
            # Redirect to a success page.
            
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('login in sot success please try again to login...'))
            return redirect('login')
        
    else:
        return render(request, 'authentication/login.html', {})