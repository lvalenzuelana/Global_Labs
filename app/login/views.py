from django.contrib.auth import get_user_model
from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login as auth_login
# → Here the application authentication is configured. 
# # Verify that the user is in the database. 
# # If the user is found, it checks the role to redirect them to their corresponding view.
def login(request):
    if request.method == 'POST':
        x = auth.authenticate(username=request.POST['username'], password = request.POST['pwd'])
        if x is None:
            return redirect('/login/login')
        else:
            auth_login(request,x)
            if x.rol == 'Teacher':
                return redirect('/teacher/teacher')
            else:
                return redirect('/student/student')
    else:
        return render(request,'login.html')