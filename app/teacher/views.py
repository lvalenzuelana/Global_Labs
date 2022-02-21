from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.template import RequestContext
from teacher.models import papers
from django.contrib import auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import random
import ftplib
import socket
import time
# → Here the view will be defined where teachers will fill in fields to be able to upload a paper to the database.
def teacher(request):
    # → Credentials to be able to store the PDF in an FTP server. Keep these credentials hidden in a production environment. 
    HOSTNAME = "192.168.192.150"
    USERNAME = "ethics4u"
    PASSWORD = "password"
    ruta = '/home/ethics4u/Papers/'
    # → If a post occurs, we upload the PDF that the teacher preloaded to an FTP server that was previously declared.
    if request.method == 'POST':
        archive = request.FILES['pdf']
        filename = request.POST['title']+".pdf"
        uploaded_file_url = "ftp://"+HOSTNAME+"/Papers/"+filename
        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd(ruta)
        ftp_server.storbinary(f"STOR {filename}", archive)
        ftp_server.quit()
        time.sleep(5)        
        # → Once with the paper on the FTP server, we connect with the computer that hosts the ML algorithm to obtain the Keywords and categories of the paper.
        MLHost = '192.168.192.123'
        MLPort = 5000
        client_socket = socket.socket()
        client_socket.connect((MLHost, MLPort))
        message = filename
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        client_socket.close()
        keywords = data.split()
        # → Here the categories are determined. At the moment they are only simulated. When the ML model is trained, the true categories will be received.
        categories = []
        for z in range (0,13):
            categories.append(0)
        for d in range (0,3):
            place = random.randint(0,len(categories))
            categories[place] = 1
        # → The paper is stored in the database.
        paper = papers(title=request.POST['title'],p_id=request.POST['p_id'],authors=request.POST['authors'],file=uploaded_file_url)
        paper.save()
        request.session['paper_id'] = request.POST['p_id']
        request.session['category'] = categories
        request.session['keywords'] = keywords
        return redirect('/categories/categories')
    else:
        return render(request,'teacher.html')