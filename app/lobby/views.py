from django.shortcuts import render

# → You are returned to the main page of the Ethics4EU application.
def home(request):
    return render(request,'lobby.html')