from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
# → In this view users can register within our application. At the end, it redirects us to our home page.
def signup(request):
    User = get_user_model()
    if request.method == 'POST': 
        x = User.objects.create_user(username = request.POST['username'], first_name=request.POST['name'],last_name=request.POST['lname'],rol=request.POST['rol'] ,email=request.POST['email'],password=request.POST['pwd'])
        x.save()
        print("Usuario Creado")
        return redirect('/')
    else:
        return render(request,'signup.html')