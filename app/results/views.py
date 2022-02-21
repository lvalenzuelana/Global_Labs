from django.shortcuts import render
from teacher.models import papers
import ftplib
from django.http.response import HttpResponse

# → Displays the search results of the papers from the student view.
def results(request):
    input = request.session.get('input')
    context = {
         "search": input
    }
    HOSTNAME = "192.168.192.150"
    USERNAME = "ethics4u"
    PASSWORD = "password"
    ruta = '/home/ethics4u/Papers/'
    request.session['HOSTNAME'] = HOSTNAME
    request.session['USERNAME'] = USERNAME
    request.session['PASSWORD'] = PASSWORD
    request.session['RUTA'] = ruta
    return render(request,'results.html',context)
